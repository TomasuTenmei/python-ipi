class BankAccount:
    
    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self, amount):
        
        self.balance += amount

    def withdraw(self, amount):
        
        if amount <= self.balance:
            
            self.balance -= amount
            
        else:
            
            print("Fonds insuffisants")

    def get_balance(self):
        
        return round(self.balance, 2)

class SavingsAccount(BankAccount):
    
    def __init__(self, balance = 0, interest_rate = 0.003):
        
        super().__init__(balance)
        self.interest_rate = interest_rate

    def set_rate(self, value):
        
        self.interest_rate = value

    def capitalization(self, month_count):
        
        for month in range(month_count):
            
            interest = self.balance * self.interest_rate
            self.balance += interest


account1 = SavingsAccount(1000)
account2 = SavingsAccount(500)
account3 = SavingsAccount(10000)

account1.set_rate(0.004)
account1.capitalization(12)
print("Solde de account1 après 12 mois :", account1.get_balance())

account2.capitalization(12 * 1)
print("Solde de account2 après 12 mois :", account2.get_balance())
account2.capitalization(12 * 2)
print("Solde de account2 après 24 mois :", account2.get_balance())
account2.capitalization(12 * 3)
print("Solde de account2 après 36 mois :", account2.get_balance())
account2.capitalization(12 * 4)
print("Solde de account2 après 48 mois :", account2.get_balance())

account3.set_rate(0.005)
account3.capitalization(12 * 1)
print("Solde de account1 après 1 an :", account3.get_balance())
account3.capitalization(12 * 2)
print("Solde de account1 après 2 ans :", account3.get_balance())
account3.capitalization(12 * 3)
print("Solde de account1 après 3 ans :", account3.get_balance())
account3.capitalization(12 * 4)
print("Solde de account1 après 4 ans :", account3.get_balance())