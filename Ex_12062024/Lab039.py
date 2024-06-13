# Factorial

# Definition -> 5! = 5*4*3*2*1

num = int(input("Enter a number to find factorial = "))

fact = 1
i = 1

while i <= num:
    fact = fact * i
    i = i + 1

print("Factorial = ", fact)
