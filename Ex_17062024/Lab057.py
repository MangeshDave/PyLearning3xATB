# Fibonacci

n = 6

fibo = [0, 1]

i = 2
while i < 7:
    n = (i-2) + (i-1)
    fibo.append(n)
    i = i + 1

print(fibo)
