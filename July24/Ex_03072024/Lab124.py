try:
    num1 = int(input("Enter num1 "))
    num2 = int(input("Enter num2 "))
    result = num1 / num2
    print(result)
except ValueError as ve:
    print("You entered other than integer")
    print(ve)
except ZeroDivisionError as zde:
    print("You divided by 0 ")
    print(zde)
finally:
    print("I will be always executed")
