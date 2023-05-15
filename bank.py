import random
from additional_exceptions import InvalidPinNumber, AccountNotFound

class Bank():
    """
    Represents the Bank object.

    Attributes:
        bank_code (private variable) - a bank code 
        bank_add (private variable) - bank's address
        list_ATM - list of ATM objects
        list_cust - list of Customer records
        list_atmcards - list of ATM_Card objects

    Methods:
        __init__ - constructor for Bank class
        add_customer - adds a Customer object and their pin number. Stored as a dictionary.
        manages - accepts an ATM_Card object and stores it in the list of ATM cards
        maintains - accepts an ATM object and stores it in the list of ATMs
        authorize_pin - accepts a Customer's object and pin number, checks that the customer's pin number is valid
        get_acct - accepts an account number and check if the account number is valid
    """
    # Represents the Bank object
    def __init__(self, bank_code, bank_add):
        self.__bank_code = bank_code # bank's code
        self.__bank_add = bank_add # bank's address
        self.list_ATM = [] # list of ATM objects
        self.list_cust = [] # list of customer records
        self.list_atmcards = [] # list of ATM card objects
    
    # Adds a Customer object and corresponding pin number as a customer record to a list
    def add_customer(self, owner_obj, pin_no):
        random.seed() # seeds from current time
        rand_no = str(random.randint(1000,9999)) 
        cust_id = owner_obj.get_name() + rand_no # generates unique customer id
        cust_rec = {"customer_id":cust_id, "cust_obj":owner_obj, "cust_pin_no":pin_no} # creates customer record (dictionary format with keys "customer_id", "cust_obj" and "cust_pin_no")
        self.list_cust.append(cust_rec)

    # Adds an ATM_card object to a list of ATM cards
    def manages(self, atm_card_obj):
        self.list_atmcards.append(atm_card_obj)

    # Adds an ATM object to a list of ATMs
    def maintains(self, atm_obj):
        self.list_ATM.append(atm_obj)

    # Checks if pin number is a valid pin number in bank system
    def authorize_pin(self, owner_obj, pin_no): 
        for cust_rec in self.list_cust:
            # checks if the pin number entered matches the pin number of the customer stored in bank system
            if cust_rec["cust_obj"] == owner_obj and cust_rec["cust_pin_no"] == pin_no:
                return True
        raise InvalidPinNumber(pin_no)

    # Checks if account number is a valid account number in bank system
    def get_acct(self, acct_num):
        for cust_rec in self.list_cust: # checks each customer record in bank system
            cust = cust_rec["cust_obj"]
            for acct_obj in cust.get_list_acct(): # checks the accounts of each customer
                if acct_obj.get_acct_num() == acct_num: # checks the account number stored in bank system
                    return acct_obj
        raise AccountNotFound(acct_num)
