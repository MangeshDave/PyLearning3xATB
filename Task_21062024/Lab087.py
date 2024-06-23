# String Reverse

# 3-4 ways to do this in Python

a = input("Enter string to be reversed -> ")
j = 1
a_length = len(a)

for i in range(a_length):
    print(a[-j], end="")
    j = j + 1
