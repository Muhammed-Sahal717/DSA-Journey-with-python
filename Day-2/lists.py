# lists- mutable-[] - slower compare to tuple

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[0])

#slicing
print(numbers[1 : 3]) # From idex 1 upto 3.(but not including index 3)

numbers[0] = 70

# Add a number to the end
numbers.append(80)

print(numbers)

# mini task

friends = ["Basheer", "Faheem", "Shahid"]

friends.append("Sahal")

print(friends[1])

print(friends)