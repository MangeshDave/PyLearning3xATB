# Anagrams

# String s1 = "silent";
# String s2 = "listen";

# namo - mano - onam

# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase

a = input("Enter a string1 to ckeck if its ANAGRAM or not -> ")
b = input("Enter a string2 to ckeck if its ANAGRAM or not -> ")
a = a.lower()
b = b.lower()
str_len1 = len(a)
str_len2 = len(b)

new_a = list(a)
new_b = list(b)

new_a = new_a.sort()
new_b = new_b.sort()

if str_len1 == str_len2:
    if new_a == new_b:
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")
else:
    print("Strings are not anagrams")

