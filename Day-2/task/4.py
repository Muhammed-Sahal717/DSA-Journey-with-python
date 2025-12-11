cap = {
    "India": "New delhi",
    "England": "london",
    "China": "Beijing"
}

user = input("Enter a country: ")

if user == "India" or "india":
    print(cap["India"])
elif user == "England" or "england":
    print(cap["England"])
elif user == "China" or "china":
    print(cap["China"])
else:
    print("Invalid!")