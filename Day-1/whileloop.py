count = 0
while count < 3: 
    print(f"Current count: {count}")
    count += 1 
print("Loop finished.")

count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1

guess = False
while not guess:
    num = int(input("Enter a number: "))
    if num == 7:
        guess = True
        print("You guessed correct!")
    else:
        print("you guessed wrong!")
