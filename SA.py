from account import * 

class SA(account):
    #static variable
    min_bal  = 500
    def __init__(self,no,name,amount):
        super().__init__(no,name,amount)
        self.acc_amount = amount

    def get_min_Bal(self):
        return self.min_bal

    def deposit_amount(self,amount):
        self.acc_amount = self.acc_amount + amount 

    def cal_bal(self):
        return self.acc_amount - self.min_bal
    
    
a2=SA(102,'Govind',10000)
a2.deposit_amount(1500)
print(a2.__dict__)
print(a2.cal_bal())