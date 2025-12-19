"""🧩 Task 2 — Bank Account
Create a BankAccount class with:

account_holder
balance
methods: deposit(), withdraw()"""


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        amount = int(input("Enter your deposit amount: "))
        self.balance = self.balance + amount


b1 = BankAccount("sahal", 20000)

b1.deposit()
