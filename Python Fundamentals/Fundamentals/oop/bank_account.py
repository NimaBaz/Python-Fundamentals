class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.rate = int_rate
        self.balance = balance

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
            print(self.balance)
        else:
            print("Insufficient funds")
        return self
        
account1 = BankAccount(0.1, 2000)
account1.deposit(500).withdraw(3000).display_account_info().yield_interest()

account2 = BankAccount(10, 2000)
account2.deposit(8000).withdraw(5000).display_account_info().yield_interest()

