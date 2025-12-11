# List Sum: Write a function sum_list(numbers) that takes a list of numbers and returns the total sum.

def sum_list(numbers):
    total = 0

    for num in numbers:
        total += num
    return total

print(sum_list([12, 34, 45,55]))