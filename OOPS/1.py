"""🧩 Task 1 — Student Class
Create a Student class with:

name
roll_number
a method display() that prints details"""


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("The student name is", self.name, ", roll number is", self.roll)


s1 = Student("Sahal", 20)
s2 = Student("Alex", 21)

s1.display()
s2.display()
