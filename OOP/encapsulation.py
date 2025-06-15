"""
hiding internal details
and one more thing is not allowing to direct access

"""
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance # it has been converted public to private

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}, New balance {self.__balance}")

    def get_balance(self):
        return self.__balance #controlled acces
    

account = BankAccount('1234', 5000)
account.deposit(2000)
print(account.get_balance())

# print(account.__balance) you cannot access like this because you have made this private