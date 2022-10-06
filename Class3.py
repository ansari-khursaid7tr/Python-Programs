class Account:
    def __init__(self, accno, accname, obal, acctype):
        self.accno = accno
        self.accname = accname
        self.obal = obal
        self.acctype = acctype
    
    def deposit(self,amount):
        self.obal += amount
        return self.obal

    def withdraw(self, amount):
        self.obal -= amount
        return self.obal

    def get_balance(self):
        return self.obal

    def __str__(self):
        return 'Account [' + str(self.accno) + '] - ' + self.accname + ', ' + self.acctype + " = " + str(self.obal)

acc1 = Account('123', 'John', 10.05, 'current')
acc2 = Account('345', 'John', 23.55, 'savings')
acc3 = Account('567', 'Phoebe', 12.45, 'investment')
print(acc1)
print(acc2)
print(acc3)
acc1.deposit(23.45)
acc1.withdraw(12.33)
print('balance:', acc1.get_balance())