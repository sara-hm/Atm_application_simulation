from atm_transaction import Withdrawal, Transfer
from additional_exceptions import InvalidAccount, InvalidATMCard

class ATM():
    """
    Represents the ATM object.

    Attributes:
        atm_add - location/address of the ATM
        managed_b - the bank (Bank object) that manages the ATM
        curr_card (private variable) - current ATM card that is "inserted" by the user of the ATM

    Methods:
        __init__ - constructor for ATM class
        get_curr_card - gets current ATM card
        set_curr_card - sets the current ATM card
        transactions - process the requested transaction according to the transaction type
        check_accts - checks if the user has 1 or 2 accounts
        check_pin - checks a user's pin number with the bank if it is valid
        check_card - checks a ATM card number with the bank if the card is a valid card. If it is valid, sets the current ATM card to this ATM_Card object
        show_balance - accepts an account type and returns a string message detailing the current balance of the requested account of that customer
    """
    def __init__(self, atm_add, bank_obj):
        self.atm_loc = atm_add # location/ address of the ATM
        self.managed_by = bank_obj # the bank that manages the ATM
        self.__curr_card = None # current ATM card that is "inserted" by the user of the ATM

    # Getter for current ATM card
    def get_curr_card(self):
        return self.__curr_card

    # Sets the current ATM card
    def set_curr_card(self, new_curr_card):
        self.__curr_card = new_curr_card

    # Process the requested transaction according to the transaction type, either "withdrawal" or "transfer"
    def transactions(self, trans_typ, amt, acct_typ, transfer_acct_no = None):
        acct_obj = self.get_curr_card().access(acct_typ.lower()) # gets the Account object from the account type of the ATM_Card object
        if trans_typ.lower() == "withdrawal":
            return Withdrawal(amt).withdraw(acct_obj) # executes withdrawal transaction
        elif trans_typ.lower() == "transfer":
            if acct_obj.get_acct_num() == transfer_acct_no: # raise InvalidAccount exception if sender and receiver are same account numbers
                raise InvalidAccount(transfer_acct_no)
            else:
                transfer_acct_obj = self.managed_by.get_acct(transfer_acct_no) # gets the transfer Account object from transfer account number
                return Transfer(amt).update(acct_obj, amt, transfer_acct_obj) # executes transfer transaction
    
    # Checks if the user has 1 or 2 accounts. Note: Each customer of the bank by default has a 'savings' account.
    def check_accts(self):
        if len(self.get_curr_card().get_acct_types()) == 2:
            return True
        else:
            return False

    # Checks with the bank if pin number is valid
    def check_pin(self, pin_no):
        owner_obj = self.get_curr_card().get_owner() # gets the Customer object of the ATM card
        return self.managed_by.authorize_pin(owner_obj, pin_no)

    # Checks with the bank if ATM card number is valid
    def check_card(self, atm_card_no):
        for atm_card_obj in self.managed_by.list_atmcards: # checks for the ATM card in the list of ATM cards in the bank system
            if atm_card_obj.get_atm_card_no() == atm_card_no:
                self.set_curr_card(atm_card_obj)
                return True
        raise InvalidATMCard(atm_card_no)

    # Checks and shows the current balance of the requested account of that customer
    def show_balance(self, acct_typ):
        acct_obj = self.get_curr_card().access(acct_typ.lower()) # gets the Account object from the account type of the ATM card object
        if self.get_curr_card().get_owner() == acct_obj.get_owner():
            return f"Your {acct_typ.lower()} account has a balance of ${acct_obj.check_balance():.2f}."

