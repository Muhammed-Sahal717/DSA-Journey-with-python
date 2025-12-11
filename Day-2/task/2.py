# Max Value: Find the largest number in the list [10, 50, 2, 90] without using the max() function (use a loop).

numbers = [10, 50, 100, 90]

largest = numbers[0]

for num in numbers:    
    if num > largest:
        largest = num

print(largest)