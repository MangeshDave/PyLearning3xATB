# One liner if else

def even_odd(num):
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")


result = even_odd(5)
print(result)

check_even_odd = lambda num: "Number is Even" if num % 2 == 0 else "Number is Odd"
print(check_even_odd(11))
