name = "sahal"

for letter in name:
    # Do something with letter
    print(letter)



for num in range(10, 21, 2):
    print(num)

# Print numbers from 1 to 20
for i in range(1, 21):
    print(i)

# Print numbers from 20 to 1
for i in range(20, 0, -1):
    print(i)

# Print all even numbers btw 1 to 50
for i in range(0, 50, 2):
    print(i)

#print the table of seven
for i in range(1, 11, 1):
    result = 7 * i

    print(f"7 * {i} = {result}")

# Print my name 10 times using a loop
for i in range(10):
    print("sahal")


nums = [10, 12, 2, 16, 30, 4, 8, 7, 22, 55, 19]

for num in nums:
    if num > 10:
        print(num)

nums = [10, 21, 16, 19, 7, 32]
count = 0
for num in nums:
    if num%2==0:
        count = count + 1
print(count)

nums = [45, 89, 100, 396, 34, 18, 76]

largest = nums[0]
for num in nums:
    if num > largest:
        largest = num
print(largest)

# vowels
name = "python"

count = 0

for ch in name:
    if ch in "aeiou":
        count = count + 1
print(count)