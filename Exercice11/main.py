class BankAccount:

    def __init__(self, account_holer: str, balance: float):
        self.account_holer = account_holer
        self.balance = balance

    def deposit(self, amount: float):
        new_balance = self.balance + amount
        if new_balance >= 0:
            self.balance = new_balance
            self.display_balance()
        else:
            print(
                f"Vous ne pouvez pas déposer la somme de {amount}€"
                " au risque de passer dans le rouge"
            )
            self.display_balance()

    def withdraw(self, amount: float):
        new_balance = self.balance - amount
        if new_balance >= 0:
            self.balance = new_balance
            self.display_balance()
        else:
            print(
                f"Vous ne pouvez pas retirer la somme de {amount}€"
                " au risque de passer dans le rouge"
            )
            self.display_balance()

    def display_balance(self):
        print(
            f"Bonjour {self.account_holer}, "
            f"vous avez actuellement {self.balance}€ sur votre compte."
        )


compte = BankAccount("Thibault", 3526.25)
compte.deposit(2163)
compte.withdraw(8000)
compte.withdraw(2641.56)
compte.display_balance()
