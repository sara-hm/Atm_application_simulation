import additional_exceptions

def atm_app(atm_obj):
    """
    Simulation menu for the ATM.

    Inputs:
        atm_obj -- ATM object
    """
    while True:
        print("\nAvailable options:")
        print("1. Insert ATM card")
        print("2. Quit Simulation")
        opt = input("Enter an option: ")
        if opt == "1":
            atm_card_no = input("Enter a ATM card number: ")
            try:
                atm_obj.check_card(atm_card_no) # checks if the atm card is valid
                pin_no = input("Enter a Pin Number: ")
                atm_obj.check_pin(pin_no) # checks if the pin number is valid
                atm_menu_sys(atm_obj) # if card and pin is valid, moves on to ATM Menu
            
            except additional_exceptions.InvalidATMCard as e: # Invalid ATM card
                print(f"{e}. Please take your card.")

            except additional_exceptions.InvalidPinNumber as e: # Invalid Pin number
                print(f"{e}. Card returned. Please take your card.")
        
        elif opt == "2":
            return
        
        else:
            print("Invalid option entered. Please enter a valid option number.")

def atm_menu_sys(atm_obj):
    """
    Simulates ATM functionalities such as check balance, withdraw funds, transfer funds and returns card.

    Inputs:
        atm_obj -- ATM object
    """
    while True:
        print("\nAvailable options:")
        print("1. Check balance")
        print("2. Withdraw Funds")
        print("3. Transfer Funds")
        print("4. Return Card")
        trans_opt = input("Enter a transaction option: ")
        cust_accts = atm_obj.check_accts() # Checks if the user has 1 or 2 accounts       
        if cust_accts == False: # user has 1 account only ("savings" account is the default)
            acct_typ = "savings"

        # Check balance
        if trans_opt == "1":
            if cust_accts == True: # user has 2 accounts
                print("\nChoose Account:")
                print("1. Current Account")
                print("2. Savings Account")
                acct_opt = input("Enter an account option: ")
                if acct_opt == "1":
                    acct_typ = "current" # sets the type of account to current if option 1 is chosen
                elif acct_opt == "2":
                    acct_typ = "savings" # sets the type of account to savings if option 2 is chosen
                else:
                    print("Invalid account option entered.")
                    continue
            print(atm_obj.show_balance(acct_typ))
            
        # Withdraw funds - allows the user to withdraw funds from their Account
        elif trans_opt == "2":
            if cust_accts == True: # user has 2 accounts
                print("\nChoose Account:")
                print("1. Current Account")
                print("2. Savings Account")
                acct_opt = input("Enter an account option: ")
                if acct_opt == "1":
                    acct_typ = "current" # sets the type of account to current if option 1 is chosen
                elif acct_opt == "2":
                    acct_typ = "savings" # sets the type of account to savings if option 2 is chosen
                else:
                    print("Invalid account option entered.")
                    continue
            count = 0 # User attempt counter. Will exit current choice selection and return to ATM menu after maximum 3 attempts
            while True:
                amt = input("Enter an amount to withdraw: ") 
                if count < 2:
                    try:
                        atm_obj.transactions("withdrawal", amt, acct_typ)
                        print("Card Returned")
                        print(atm_obj.show_balance(acct_typ))
                        return
                    except ValueError: # Amount is invalid.
                        count = count + 1
                        print(f"Amount is invalid. Please re-enter withdrawal amount. Remaining attempts: {3-count}")
                    except additional_exceptions.InsufficientFunds as e: # Insufficient funds in account balance to withdraw
                        print (f"{e}. Please re-select from ATM Menu.")
                        break
                elif count == 2: # last attempt for user 
                    try:
                        atm_obj.transactions("withdrawal", amt, acct_typ)
                        print("Card Returned")
                        print(atm_obj.show_balance(acct_typ))
                        return
                    except ValueError: # Amount is invalid.
                        print (f"Amount is invalid. Maximum number of attempts entered. Please re-select from ATM Menu.")
                        break  
                    except additional_exceptions.InsufficientFunds as e: # Insufficient funds in account balance to withdraw
                        print(f"{e}. Please re-select from ATM Menu.")
                        break                                          

        # Transfer Funds - allows the user to transfer funds from their Account
        elif trans_opt == "3":
            if cust_accts == True: # user has 2 accounts
                print("\nChoose Account:")
                print("1. Current Account")
                print("2. Savings Account")
                acct_opt = input("Enter an account option: ")
                if acct_opt == "1":
                    acct_typ = "current" # sets the type of account to current if option 1 is chosen
                elif acct_opt == "2":
                    acct_typ = "savings" # sets the type of account to savings if option 2 is chosen
                else:
                    print("Invalid account option entered.")
                    continue            
            # Checks first whether the transfer account number exists and is valid
            count = 0 # User attempt counter. Will exit current choice selection and return to ATM menu after maximum 3 attempts
            while True:   
                if count < 2:
                    transfer_acct_no = input ("Enter the account number to transfer funds to: ")
                    try:
                        atm_obj.transactions("transfer", 0, acct_typ, transfer_acct_no) # default transfer amount of $0.00 is input to test for transfer account number               
                    except additional_exceptions.AccountNotFound as e: # Account not found in bank system
                        count = count + 1
                        print(f"{e}. Please re-enter account number. Remaining attempts: {3-count}")
                        continue
                    except additional_exceptions.InvalidAccount as e: # Invalid account number
                        count = count + 1
                        print(f"{e}. Sender and Receiver account number are the same. Please re-enter account number. Remaining attempts: {3-count}")
                        continue
                    except ValueError: # Since only testing for transfer account number, continue on to ask user for amount to transfer
                        pass
                    # Checks next whether the transfer amount is valid 
                    while True:
                        amt = input("Enter an amount to transfer: ")
                        if count < 2:
                            try: 
                                atm_obj.transactions("transfer", amt, acct_typ, transfer_acct_no)
                                print("Card Returned")
                                print(atm_obj.show_balance(acct_typ))
                                return
                            except ValueError: # Amount is invalid
                                count = count + 1
                                print(f"Amount is invalid. Please re-enter transfer amount. Remaining attempts: {3-count}")
                            except additional_exceptions.InsufficientFunds as e: # Insufficient funds in account balance
                                count = 3
                                print(f"{e}. Please re-select from ATM Menu.")
                                break
                        elif count == 2: # last attempt for user
                            count = count + 1
                            try: 
                                atm_obj.transactions("transfer", amt, acct_typ, transfer_acct_no)
                                print("Card Returned")
                                print(atm_obj.show_balance(acct_typ))
                                return
                            except ValueError: # Amount is invalid
                                print(f"Amount is invalid. Maximum number of attempts entered. Please re-select from ATM Menu.")
                                break
                            except additional_exceptions.InsufficientFunds as e: # Insufficient funds in account balance
                                print(f"{e}. Please re-select from ATM Menu.")
                                break                     
                elif count == 2: # last attempt for user
                    transfer_acct_no = input ("Enter the account number to transfer funds to: ")
                    try:
                        atm_obj.transactions("transfer", 0, acct_typ, transfer_acct_no) # default transfer amount of $0.00 is entered to test for transfer account number
                    except additional_exceptions.AccountNotFound as e: # Account not found in bank system
                        print(f"{e}. Maximum number of attempts entered. Please re-select from ATM Menu.")
                        break
                    except additional_exceptions.InvalidAccount as e: # Invalid account number
                        print(f"{e}. Sender and Receiver account number are the same. Maximum number of attempts entered. Please re-select from ATM Menu.")
                        break
                    except ValueError: # Since only testing for transfer account number, continue on to ask user for amount to transfer
                        pass
                    # Checks next whether the transfer amount is valid
                    amt = input("Enter an amount to transfer: ")
                    try:
                        atm_obj.transactions("transfer", amt, acct_typ, transfer_acct_no)
                        print("Card Returned")
                        print(atm_obj.show_balance(acct_typ))
                        return
                    except ValueError: # Amount is invalid
                        print(f"Amount is invalid. Maximum number of attempts entered. Please re-select from ATM Menu.")
                        break
                    except additional_exceptions.InsufficientFunds as e: # Insufficient funds in account balance
                        print(f"{e}. Please re-select from ATM Menu.")
                        break
                else:
                    break
              
        # Return card
        elif trans_opt == "4":
            print("Card Returned")
            return

        # Requests user to enter a valid ATM menu option
        else:
            print("Invalid transaction option entered. Please enter a valid option.")

