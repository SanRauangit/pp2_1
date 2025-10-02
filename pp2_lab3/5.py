class Account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,cash):
        if cash>0:
            self.balance += cash
            print(f"Deposited: {cash:.2f}$. \n New balance: {self.balance:.2f}$ \n ")
        else:
            print("Deposit must be positive")
        return self.balance
    def withdraw(self,amount):
        if amount<=0:
            print("Withdraw must be positive!")
            return self.balance
        if amount>self.balance:
            print(f"Withdrawal denied! Insufficient funds. \n Available: {self.balance:.2f}$ \n")
            return self.balance
        else:
            self.balance -= amount
            print(f"Witdrew: {amount:.2f}$ \n Available: {self.balance:.2f}$ \n")
            return self.balance
        
account=Account("Steve Nash" , 100)
account.deposit(200)
account.withdraw(150)

account2=Account("Anthony Edwards",20)
account2.deposit(50)
account2.withdraw(80)