from datetime import datetime

class Customer():
    """
    Represents the Customer object.

    Attributes:
        name (private variable) - customer's name
        add (private variable) - customer's address
        dob (private variable) - customer's date of birth in datetime format (DD-MMM-YYYY)
        list_acct (private variable) - list of accounts a customer can have, maximum is 2. Savings and/or Current account/s

    Methods:
        __init__ - constructor for Customer class
        __str__ - returns string representation of the Customer object detailing the name, address and date of birth
        owns - adds an Account object to customer's list of account objects
        get_name - get's customer's name
        get_list_acct - gets customer's list of accounts
        get_add - gets customer's address
        get_dob - gets customer's date of birth
    """
    def __init__(self, name, add, dob):
        self.__name = name # customer's name
        self.__add = add # customer's address
        self.__dob = datetime.strptime(dob, "%d-%b-%Y") # customer's date of birth
        self.__list_acct = [] # list of Account objects

    def __str__(self):
        return f"Customer [Name is {self.get_name()}, Address is {self.get_add()}, Date of birth is {self.get_dob().strftime('%d-%b-%Y')}]"
    
    # Adds an Account object to the list of Account objects
    def owns(self, acct_obj): 
        if len(self.get_list_acct())<2: # checks that customer has maximum 2 accounts
            self.get_list_acct().append(acct_obj)
        else:
            print("Customer already has 2 accounts")
    
    # Getter for customer's name
    def get_name(self):
        return self.__name
    
    # Getter for list of accounts
    def get_list_acct(self):
        return self.__list_acct
        
    # Getter for customer's address
    def get_add(self):
        return self.__add
    
    # Getter for customer's date of birth
    def get_dob(self):
        return self.__dob       
