# Palidrome of String

# i/p = naman , nitin, level

# o/p = true

# i/p = pramod

# o/p = false

flag = 0
a = input("Enter string check for Palindrome - ")
a = a.lower()
print(a)
j = 1
a_length = int(len(a)/2)
for i in range(a_length):
    if a[i] == a[-j]:
        j = j+1
        flag = 1
    else:
        flag = 0

if flag == 1:
    print("String is Palindrome")
else:
    print("String is non-Palindrome")
