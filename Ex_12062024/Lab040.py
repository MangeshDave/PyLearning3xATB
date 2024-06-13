# Fibonacci

# Definition -> series of numbers where current number is addition of previous 2 numbers

fibo = int(input("Enter a number till Fibonacci you want to print = "))

a = [0, 1]
if fibo == 1:
    print(0)
elif fibo == 2:
    print(0, 1)
else:
    print(None)

i = 1
while i <= fibo:
    a[i+2] = a[i] + a[i+1]

print(a)

