"""Write a Python program that:
1 - Stores a list of numbers.
2 - Uses a loop to check each number.
3 - Counts:
 - How many numbers are even
 - How many numbers are odd
 - How many numbers are positive
 - How many numbers are negative
 - How many numbers are zero
4 - Prints all results at the end."""

# Step 1: List of numbers
numbers = [12, -5, 0, 7, -3, 8, 0, 15]

# Step 2: Initialize counters
even_count = 0
odd_count = 0

positive_count = 0
negative_count = 0

zero_count = 0

# Step 3: Loop through the list
for num in numbers:

    # Check positive, negative or zero
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

    # Check even or odd
    if num != 0:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

# Step 4: Display results
print("Numbers:", numbers)
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("zero values:", zero_count)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
