run = True

while run:
    print("\n=== MENU ===")
    print("1. Pirnt multiplication table")
    print("2. Pirnt numbers from 1 to n")
    print("3. Count how many even numbers from 1 to n")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # OPTION 1: MULTIPLICATION TABLE
    if choice == 1:
        num = int(input("Enter a number: "))
        print("Table of", num)
        for i in range(1, 11):
            print(num, "x", i, "=", num * i)

    # OPTION 2: PRINT 1 TO n
    elif choice == 2:
        n = int(input("Enter n: "))
        print("Numbers from 1 to", n)
        for i in range(1, n + 1):
            print(i)

    # OPTION 3: COUNT EVEN NUMBERS
    elif choice == 3:
        n = int(input("Enter limit: "))
        count = 0
        for i in range(1, n + 1):
            if i % 2 == 0:
                count = count + 1
        print("Total even numbers =", count)

    # EXIT OPTION
    elif choice == 4:
        run = False 

    else:
        print("Invalid choice, try again!")