"""🧩 Task 5 — Real-Life Object
Pick any real-world object (Phone, Laptop, Fan):

Define at least 3 attributes
Define at least 2 methods"""


class Phone:
    def __init__(self, model, is_on, battery):
        self.model = model
        self.is_on = is_on
        self.battery = battery

    def gaming(self):
        if self.is_on == "on":
            if self.battery >= 40:
                print("start gaming!")
            else:
                print("You don't have enough charge!")
        else:
            print("Sorry!")

    def typing(self):
        if self.is_on == True:
            if self.battery >= 12:
                print("Start typing!")
            else:
                print("You don't have enough charge!")
        else:
            print("Sorry!")


p1 = Phone("samsung", True, 70)
p2 = Phone("iQOO", False, 100)


p1.typing()

p2.gaming()
