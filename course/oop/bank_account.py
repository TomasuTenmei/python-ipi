class BankAccount:
    
    def __init__(self, name = 'John', balance = 1000):
        
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        
        if amount > 0:
            
            self.balance += amount
            print(f'Le dépot de {amount} a était accepté. Nouveau solde : {self.balance}')
            
        else:
            
            print('Montant de dépôt invalide.')

    def withdraw(self, amount):
        
        if amount > 0 and amount <= self.balance:
            
            self.balance -= amount
            print(f'Le retrait de {amount} a était accepté. Nouveau solde : {self.balance}')
            
        else:
            
            print('Montant de retrait invalide ou solde insuffisant.')

    def display(self):
        
        print(f'Account information : {self.name}\nSolde : {self.balance}')


account1 = BankAccount()
account2 = BankAccount('Alice', 2000)


account1.display()
account1.deposit(500)
account1.withdraw(200)
account1.display()

account2.display()
account2.deposit(1000)
account2.withdraw(1500)
account2.display()
