class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []

    def __init__(self, user, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.rate = int_rate
        self.balance = balance
        self.user = user
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self
            

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(self.balance)
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            print(self.balance)
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
        

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.rate
        else:
            print("Insufficient funds")
        return self

    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            print(f"{account.user} ${account.balance} and the interest rate is {account.rate}")


account1 = BankAccount("Nima's Account has: ", 0.1, 2000)
account1.deposit(500).withdraw(3000).yield_interest().display_account_info()

account2 = BankAccount("Yooo's Account has: ", 10, 2000)
account2.deposit(8000).withdraw(5000).yield_interest().display_account_info()

BankAccount.all_balances()

