# Filter Negative: Given [-5, 10, -2, 20, 0], use filter to create a list of only positive numbers.

numbers = [-5, 10, -2, 20, 0]

positive = filter(lambda num:  num > 0, numbers)

print(list(positive))