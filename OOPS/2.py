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
        self.balance += amount
        print("Deposit successful. Balance:", self.balance)

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful. Balance:", self.balance)
            else:
                print("Insufficient balance!")
        else:
            print("invalid deposit amount!")


b1 = BankAccount("Sahal", 20000)

b1.deposit(5000)
b1.withdraw(3000)
b1.withdraw(30000)
