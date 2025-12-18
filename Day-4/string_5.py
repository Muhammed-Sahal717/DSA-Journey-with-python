# 5️⃣ Count Vowels
# Count how many vowels (a e i o u) are present in a string.


def vowels_string(s):
    vowels = "aeiou"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    print(count)


vowels_string("sahal")
