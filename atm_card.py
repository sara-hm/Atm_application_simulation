class ATM_Card():
    """
    Represents the ATM_Card object. A customer can only own one ATM card per bank.
    Used by the ATM to access the customer's accounts.

    Attributes:
        atm_card_no (private variable) - ATM card's number 
        owned_by (private variable) - Customer object

    Methods:
        __init__ - constructor for ATM_Card class
        get_acct_types - returns a list of the account types available for the customer
        access - accepts an account type and returns the Account object of the customer
        __str__ - returns string representation of the ATM_Card object detailing the card's number and owner's name
    """
    def __init__(self, atm_card_no, owner_obj):
        self.__atm_card_no = atm_card_no # ATM card number
        self.__owned_by = owner_obj # Customer object

    def __str__(self):
        return f"ATM Card [Card Number is {self.get_atm_card_no()}, Customer name is {self.get_owner().get_name()}]"

    # Returns a list of account types ('savings' and/ or 'current') available for the customer
    def get_acct_types(self):
        list_acct_obj = self.get_owner().get_list_acct() # Returns list of Account objects for the customer
        list_acct_typ = []
        for acct_obj in list_acct_obj: # Returns the account types available for the customer
            list_acct_typ.append(acct_obj.get_acct_typ()) 
        return list_acct_typ

    # Returns the Account object of the customer from account type
    def access(self, acct_typ):
        list_acct_obj = self.get_owner().get_list_acct() # Returns list of Account objects for the customer
        for acct_obj in list_acct_obj:
            if acct_obj.get_acct_typ() == acct_typ.lower():
                return acct_obj

    # Getter for ATM card number
    def get_atm_card_no(self):
        return self.__atm_card_no

    # Getter for ATM card owner (Customer object)
    def get_owner(self):
        return self.__owned_by

