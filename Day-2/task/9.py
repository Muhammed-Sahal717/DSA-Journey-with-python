# Map Strings: Given ['apple', 'banana'], use map to create a list of the lengths of these words [5, 6].

words = ["apple", "banana"]

length = map(len, words)

print(list(length))