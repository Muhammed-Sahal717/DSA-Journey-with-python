"""🧩 Task 3 — Rectangle
Create a Rectangle class with:

length
width
method to calculate area"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(area)


a1 = Rectangle(8, 2)
a1.area()
