# 4️⃣ Convert to Uppercase
# Convert all characters in a string to uppercase without using .upper().

"""ASCII facts:

'a' → 97

'z' → 122

'A' → 65

'Z' → 90

👉 Difference between lowercase & uppercase letters is 32"""

# uppercase = lowercase - 32

""" 'a' (97) → 'A' (65)
97 - 32 = 65 """

# Python Tools We Use

# ord(char) → character ➜ ASCII number
# chr(num) → ASCII number ➜ character


text = "aa1na"
result = ""

for ch in text:
    if "a" <= ch <= "z":  # 97 <= ord(ch) <= 122
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)
