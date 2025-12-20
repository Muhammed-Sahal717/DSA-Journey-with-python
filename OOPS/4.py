"""🧩 Task 4 — Counter
Create a Counter class that:

starts from 0
has increment() method
prints current value"""


class Counter:
    def __init__(self):
        self.count = 0  # we can also put a value here. no only the value pass variable.

    def increment(self):
        self.count += 1
        print(self.count)


c1 = Counter()
c1.increment()
c1.increment()
c1.increment()
c1.increment()
c1.increment()
