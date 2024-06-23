# Count vowels and consonants in a String

a = input("Enter string to get Vowels & Consonants -> ")
a = a.lower()
vowel_count = 0
consonant_count = 0
a_length = len(a)

for i in range(a_length):
    if a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u':
        vowel_count = vowel_count + 1
    else:
        consonant_count = consonant_count + 1

print("Vowel count in ", a, "=", vowel_count)
print("Consonant count in ", a, "=", consonant_count)
