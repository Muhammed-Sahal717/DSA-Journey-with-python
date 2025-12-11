color = input("Enter your favorite color:")

print(color)

# Type casting

n1 = input("Enter a number")
n2 = input("Enter a number")

# input() function always return string(including numbers), 
# so we convert string_number into a number using type casting.
n1_number = int(n1)
n2_number = int(n2)

res = n1_number + n2_number
print(res)