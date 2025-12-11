# List comprehension - [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5]

# long way- slower
squares = []

for n in numbers:
    squares.append(n**2)
# list comprehension way- faster
squares_comp = [n ** 2 for n in numbers]

print(squares_comp)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_comp = [n for n in nums if n % 2 == 0]

print(even_comp)