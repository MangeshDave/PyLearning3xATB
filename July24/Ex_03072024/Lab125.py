try:
    num1 = int(input("Enter num1 "))
    num2 = int(input("Enter num2 "))
    result = num1 / num2
except ValueError as ve:
    print("You entered other than integer")
    print(ve)
except ZeroDivisionError as zde:
    print("You divided by 0 ")
    print(zde)
else:
    print("You entered correct data")
    print(result)
finally:
    print("I will be always executed")
    print("End of program")
