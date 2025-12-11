nums = [1, 5, 8, 10, 13]

# Keep only even numbers
evens = filter(lambda x: x % 2 == 0, nums)

print(list(evens))

words = ['hi', 'hello', 'yo', 'python']

limit = filter(lambda word: len(word) > 3 , words)

print(list(limit))