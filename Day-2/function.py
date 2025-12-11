def add_nums(a, b):
    return a + b

print(add_nums(10, 20))


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))

def nums(n):
    if n < 1:
        return
    print(n)
    nums(n-1)
nums(10)