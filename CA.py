from account import * 

class CA(account):
    #static variable
    min_bal  = 5000
    def __init__(self,no,name,amount):
        super().__init__(no,name,amount)
        self.acc_amount = amount

    def get_min_Bal(self):
        return self.min_bal

    def deposit_amount(self,amount):
        self.acc_amount = self.acc_amount + amount
        print('Amount Deposited Successfully !!')
        print("Deposited Amount Is :",amount)
    
    def cal_bal(self):
        return self.acc_amount - self.min_bal
    
    
a3=CA(103,'Moni',10000)
a3.deposit_amount(1500)
print(a3.__dict__)
print(a3.cal_bal())
