from additional_exceptions import InsufficientFunds

class Account():
    """
    Represents the Account object (Parent) of each customer of the bank.

    Attributes:
        acct_typ (protected variable) - customer's account type, either 'savings' or 'current' 
        owner_obj (private variable) - Customer object
        balance (private variable) - account balance

    Methods:
        __init__ - constructor for Account class
        check_balance - returns the current balance of the account
        set_balance - sets the current balance of the account
        get_owner - gets owner object (Customer object)
        get_acct_typ - gets customer's account type
        debit - accepts an amount, checks it then subtracts it from the balance
        credit - accepts an amount, checks it then adds it to the balance
        validate_amount (private method) - accepts a monetary amount, converts it to type float and checks if the amount is <= 0 or has more than 2 decimal places
    
    Child classes:
        Savings_Account - represents the Savings Account object (Child) of each customer of the bank
        Current_Account - represents the Current Account object (Child) of each customer of the bank
    """    
    def __init__(self, acct_typ, owner_obj):
        self._acct_typ = acct_typ # Values are either 'savings' or 'current'
        self.__owner = owner_obj # Customer object
        self.__balance = 0 # account balance

    # Getter for current account balance
    def check_balance(self):
        return self.__balance

    # Sets the current balance of the account
    def set_balance(self, new_balance):
        self.__balance = new_balance

    # Getter for owner (Customer object) of the account
    def get_owner(self):
        return self.__owner

    # Getter for account type
    def get_acct_typ(self):
        return self._acct_typ

    # Checks and debits an input amount from the account balance
    def debit(self, amt): 
        self.__validate_amount(amt)
        if float(amt) <= self.check_balance():
            self.set_balance(self.check_balance() - float(amt))
            return True
        else:
            raise InsufficientFunds(amt)
    
    # Credits an input amount to the account balance
    def credit(self, amt): 
        check = self.__validate_amount(amt)
        if check == True:
            self.set_balance(self.check_balance() + float(amt))
            return True

    # Checks that the amount entered is valid     
    def __validate_amount(self,amt): 
        amt = float(amt)
        str_amt = str(amt).split(".") # Converts the amount entered to a string and splits the string be separator "."
        if amt <= 0 or len(str_amt[-1])>2: # Checks for no. of digits after decimal point
            raise ValueError("Amount is invalid")
        else:
            return True

class Savings_Account(Account):
    """
    Represents the Savings Account object (Child) of each customer of the bank.

    Attributes:
        acct_num (private variable) - account number of the respective account 
        owner_obj (private variable) - Customer object
        acct_typ (protected variable) - customer's account type, value is 'savings'

    Methods:
        __init__ - constructor for Savings_Account class
        get_acct_num - gets account number
    """  
    def __init__(self, acct_num, owner_obj):
        super().__init__("savings", owner_obj) # account type is 'savings'
        self.__acct_num = acct_num # account number of the respective account
    
    # Getter for account number
    def get_acct_num(self):
        return self.__acct_num

class Current_Account(Account): 
    """
    Represents the Current Account object (Child) of each customer of the bank.

    Attributes:
        acct_num (private variable) - account number of the respective account 
        owner_obj (private variable) - Customer object
        acct_typ (protected variable) - customer's account type, value is 'current'

    Methods:
        __init__ - constructor for Current_Account class
        get_acct_num - gets account number
    """ 
    def __init__(self, acct_num, owner_obj):
        super().__init__("current", owner_obj) # account type is 'current'
        self.__acct_num = acct_num # account number of the respective account
    
    # Getter for account number
    def get_acct_num(self):
        return self.__acct_num




