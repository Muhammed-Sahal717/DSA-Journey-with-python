# 7️⃣ First Non-Repeating Character
# Find the first character that does not repeat.
# Input: "aabbccd" Output: d


def repeat_char(s):
    output = ""
    for ch in s:
        if output != ch:
            output += ch
    return output


print(repeat_char("aabbccd"))
