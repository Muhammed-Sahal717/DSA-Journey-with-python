fruits=["banana", "apple", "cherry"]

for fruit in fruits:    # the fruit is a temporary variable of fruits.
    print(f"I like {fruit}")    # the f is f_string, for tell the string contain a variable.


prices = [10.99, 27.75, 5.25]
total_cost = 0

for price in prices:
    total_cost += price

    print(f"The total cost is: ${total_cost}")