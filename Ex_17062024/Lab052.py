# Functions

def sum_2(a, b):
    print(a + b)


sum_2(3, 4)
sum_2(a=5, b=4)
sum_2(b=10, a=5)


def sum_3(a=1, b=1, c=1):
    return a + b + c


result = sum_3()                # Default values will be used
print(result)
result = sum_3(1, 2, 3) # Default values will be overwritten
print(result)
result = sum_3(a=1, c=2)        # Only  2 values passed
print(result)
