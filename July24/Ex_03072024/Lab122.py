# Try Except
try:
    a = int(input("Enter the num1 "))
    b = int(input("Enter the num2 "))
    c = a / b
    print("Result = ", c)
except Exception as e:
    print(e)
