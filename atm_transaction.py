from abc import *
from datetime import datetime

class ATM_Transaction(ABC):
    """
    Represents the ATM_transaction object (Parent) that the ATM can perform.
    Abstract class.

    Attributes:
        trans_id (static variable) - keeps track of all transactions that has taken place
        trans_datetime (public variable) - stores the date and time of current transaction, type datetime
        trans_typ (protected variable) - type of transaction, either 'withdrawal' or 'transfer'
        amt (protected variable) - monetary amount used for the transaction

    Methods:
        __init__ - constructor for ATM_Transaction class
        update (abstractmethod) - accepts the customer's Account object, amount and transfer Account object. Implementation done by child classes.
        
    Child classes:
        Withdrawal - represents the Withdrawal transaction object (Child) that the ATM can perform
        Transfer - represents the Transfer transaction object (Child) that the ATM can perform
    """
    trans_id = 0

    def __init__(self, trans_datetime, trans_typ, amt=0):
        self.trans_datetime = trans_datetime # stores the date and time of current transaction, type datetime
        self._trans_typ = trans_typ # type of transaction, either 'withdrawal' or 'transfer'
        self._amt = amt # monetary amount used for the transaction

        ATM_Transaction.trans_id = ATM_Transaction.trans_id + 1 # keeps track of all transactions that have taken place

    # Updates the customer's Account object according to the transaction type
    @abstractmethod
    def update(self, acct_obj, amt, transfer_acct_obj = None):
        pass

class Withdrawal(ATM_Transaction):
    """
    Represents the Withdrawal transaction object (Child) that the ATM can perform.

    Attributes:
        None

    Methods:
        __init__ - constructor for Withdrawal class
        withdraw - calls the update() function with the appropriate parameters
        update - updates the customer's Account object with the funds to be withdrawn
    """  
    def __init__(self, amt):
        super().__init__(datetime.now(), "withdrawal", amt)

    # Calls the update() function with the appropriate parameters
    def withdraw(self, acct_obj):
        return self.update(acct_obj, self._amt)

    # Updates the customer's Account object with the funds to be withdrawn
    def update(self, acct_obj, amt, transfer_acct_obj = None):
        return acct_obj.debit(amt)

class Transfer(ATM_Transaction):
    """
    Represents the Transfer transaction object (Child) that the ATM can perform.

    Attributes:
        None

    Methods:
        __init__ - constructor for Transfer class
        update - updates the customer's Account object with the funds to be withdrawn
    """
    def __init__(self, amt):
        super().__init__(datetime.now(), "transfer", amt)

    # Updates the customer's Account object with the funds to be withdrawn
    def update(self, acct_obj, amt, transfer_acct_obj = None):
        debit_trans = acct_obj.debit(self._amt)
        credit_trans = transfer_acct_obj.credit(self._amt)
        if debit_trans and credit_trans:
            return True