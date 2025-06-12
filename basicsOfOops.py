


class BankAccount:
    def __init__(self,account_number,holder_name,balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self,amount):
        if amount>0:
            self.balance = self.balance+amount
        else:
            print("the entered amount is not valid")

    def withdraw(self,amount):
        if amount<self.balance:
            self.balance = self.balance-amount
        else:
            print("insufficient balance")

    def display(self):
        print("The account holder name is ", self.holder_name)
        print("The account number is ", self.account_number)
        print("The balance in account is ",self.balance)

BankAccount1 = BankAccount("060310110002538","sunita Veer",5000000)
BankAccount1.deposit(100000)
BankAccount1.withdraw(10000)
BankAccount1.display()