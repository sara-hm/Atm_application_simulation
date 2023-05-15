# Defines the custom exceptions created for ATM simulation

class InvalidAccount(Exception):
    """
    Exception raised when account number of the Sender and Receiver are the same.

    Attributes:
        acct_num - account number of the sender/ receiver  
        message - explanation of the error
    """
    def __init__(self, acct_num, message='Invalid account number'):
        self.acct_num = acct_num
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f'{self.message} {self.acct_num}'

class AccountNotFound(Exception):
    """
    Exception raised when account number is not valid, i.e. cannot be found in the system.

    Attributes:
        acct_num - account number of the sender/ receiver
        message - explanation of the error
    """
    def __init__(self, acct_num, message='Account not found in bank system'):
        self.acct_num = acct_num
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f'{self.message} for account number {self.acct_num}'

class InsufficientFunds(Exception):  
    """
    Exception raised when insufficient funds in the bank balance for withdrawal or transfer.

    Attributes:
        amt - amount to be debited from account
        message - explanation of the error
    """
    def __init__(self, amt, message='Insufficient funds in account balance'):
        self.amt = float(amt)
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f'{self.message} to withdraw ${self.amt:.2f}'

class InvalidATMCard(Exception):
    """
    Exception raised when ATM card is invalid based on ATM card number.

    Attributes:
        atm_card_no - ATM card number
        message - explanation of the error
    """
    def __init__(self, atm_card_no, message='Invalid Card'):
        self.atm_card_no = atm_card_no
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f'{self.message}'

class InvalidPinNumber(Exception):
    """
    Exception raised when pin number is not valid.

    Attributes:
        pin_no - pin number
        message - explanation of the error
    """
    def __init__(self, pin_no, message='Invalid Pin number'):
        self.pin_no = pin_no
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f'{self.message}'

