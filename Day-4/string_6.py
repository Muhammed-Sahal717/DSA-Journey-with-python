# 6️⃣ Remove Spaces
# Remove all spaces from a string.
# Input: "hello world python" Output: "helloworldpython"


def rem_space(s):
    s = s.replace(" ", "")
    print(s)


rem_space("hello world python")


def rem_space1(ch):
    result = ""
    for c in ch:
        if c != " ":
            result += c
    return result


print(rem_space1("hello world python"))
