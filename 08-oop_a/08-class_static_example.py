class BankAccount:
    interest_rate = 0.02
    def __init__(self, holder, balance=0): 
        self.holder = holder
        self.balance = balance
    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"Interest rate changed to {cls.interest_rate}")
    
    @staticmethod
    def validate_amount(amount):
        return amount > 0
    
    def withdraw(self, amount):
        if self.validate_amount(amount):
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount. Amount must be positive.")

account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)
print(f"Initial interest rate: {BankAccount.interest_rate}")
BankAccount.change_interest_rate(0.03)
print(f"Account1 Interest Rate: {account1.interest_rate}")
account1.withdraw(200) #Withdrew 200. New balance is 800.
account2.withdraw(-50)  # Invalid amount
account2.withdraw(600)  # Insufficient funds
print (BankAccount.validate_amount(150))  # True