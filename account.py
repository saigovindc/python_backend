from bank import *

class account(bank):
    
        def __init__ (self,no,name,amount):
            self.acc_no = no
            self.acc_name = name
            self.acc_amount = amount

        def open_account(self):
            print ('Account Opened Successfully')

        def deposit_amount(self):
            pass

        def cal_bal(self):
             print('account class - cal_Bal')

a1=account(101,'Sai',5000)
print(a1.__dict__)