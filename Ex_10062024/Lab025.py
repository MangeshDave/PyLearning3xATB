# Task 2

# write a program to calculate square & cube of a given number
# Write a program to take two numbers from user & show them if both are equal, first is less than or greater than second number

import math

Num = float(input("Enter a number"))
Num_Square = pow(Num, 2)
Num_Cube = Num**3
print("Square of ", Num, "=", Num_Square)
print("Cube of ", Num, "=", Num_Cube)

Num1 = input("Enter first number for comparison")
Num2 = input("Enter second number for comparison")
Comparison_Equal = (Num1 == Num2)
Comparison_Greater = (Num1 > Num2)
Comparison_Smaller = (Num1 < Num2)
if(Comparison_Smaller):
    print("First number is smaller than second number")
elif(Comparison_Greater):
    print("First number is greater than second number")
else:print("Both numbers are equal")