#oculta detalles internos de una clase para proteger su estado y comportamiento
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # atributo de instancia privado

    def deposit(self, amount):  # método público
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):  # método público
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds or invalid amount")

    def get_balance(self):  # método público
        return self.__balance
    
account = BankAccount(1000)
account.deposit(500) 
print("Current Balance:", account.get_balance())

#Al usar __balance y obligar a usar los métodos deposit o withdraw, aseguras que nadie pueda cambiar el saldo sin pasar por las reglas (los if) que has programado.
#account.__balance = -1000000 # This is not our object private balance! It's a new public attribute.
#print("Current Balance:", account.__balance)
#print(account.__dict__)
account._BankAccount__balance = -1000000 # We shouldn't do this. Python mangles the name to make it harder to access, but still possible.
print("Current Balance:", account.get_balance())
print(account.__dict__)