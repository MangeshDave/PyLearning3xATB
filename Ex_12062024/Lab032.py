# Conditions -> Multiple conditions

# Take 3 nos from user & show him which no is greater

Num1 = int(input("Enter 1st number = "))
Num2 = int(input("Enter 2nd number = "))
Num3 = int(input("Enter 3rd number = "))

if Num1 > Num2 and Num1 > Num3:
    print(Num1)
elif Num2 > Num1 and Num2 > Num3:
    print(Num2)
else:
    print(Num3)
