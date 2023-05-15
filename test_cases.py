from bank import Bank # from bank.py import Bank class
from atm import ATM
from account import Savings_Account, Current_Account
from atm_card import ATM_Card
from customer import Customer
from main_app import atm_app # from main_app.py import atm_app function

# set up the bank objects.
bank_01 = Bank("POSB01", "51 Sunset lane")
# set up atm object
atm_01 = ATM("tannery lane 78", bank_01)
# bank_01 has 1 atm
bank_01.maintains(atm_01)

# set up customer object.
# customer 1 has 1 savings acct with 8k and 1 current acct with 5k with
bank_01
cust_01 = Customer('Tom', 'abc lane', '15-may-1987')
save_01 = Savings_Account("458-96252", cust_01)
curr_01 = Current_Account("124-87592", cust_01)
cust_01.owns(save_01)
cust_01.owns(curr_01)
# adding money to acct
save_01.credit(8000)
curr_01.credit(5000)
# ATM card
dc_01 = ATM_Card("589-5955-874-6941", cust_01)
bank_01.manages(dc_01)
bank_01.add_customer(cust_01, "1234")

# customer 2 has 1 savings acct with 6k with bank_01
cust_02 = Customer('Kim', 'blank lane', '05-dec-1999')
save_02 = Savings_Account("874-15268", cust_02)
cust_02.owns(save_02)

# adding money to acct
save_02.credit(6000)
# ATM card
dc_02 = ATM_Card("847-9521-248-8451", cust_02)
bank_01.manages(dc_02)
bank_01.add_customer(cust_02, "8745")

#print customer info
print(cust_01)
print(dc_01)
print()
print(cust_02)
print(dc_02)

#start running the ATM using the atm_app function you created in main_app.py
atm_app(atm_01)
