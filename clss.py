class BankAccount():
    # default method loaded
    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount
        print(self.balance)

    def withdraw(self,amount):
        self.balance -= amount
        print(self.balance)

class MinimumBalance(BankAccount):
    def __init__(self,minBal):
        BankAccount.__init__(self)
        self.minBal = minBal

    def withdraw(self,amount):
        if self.balance - amount < self.minBal:
            print("Insufficient balance")
        else:
            BankAccount.withdraw(self,amount)

a = BankAccount()
b = BankAccount()

a.deposit(500)
b.deposit(700)
b.withdraw(800)
