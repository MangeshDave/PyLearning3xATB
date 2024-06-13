# Task -> Write a program to classify a trianle based on its side lengths
# Equilateral -> All 3 sides are equal
# Isosceles -> Exactly 2 sides are equal
# Scalene -> All 3 sides are different

side1 = int(input("Enter 1st side of triangle = "))
side2 = int(input("Enter 2nd side of triangle = "))
side3 = int(input("Enter 3rd side of triangle = "))

if side1 == side2 and side1 == side3:
    print("Triangle is Equilateral")
elif ((side1 == side2 and side1 != side3) or (side2 == side3 and side2 != side1) or (side1 == side3 and side1 != side2)):
    print("Triangle is Isosceles")
elif ((side1 != side2) and (side1 != side3) and (side2 != side3)):
    print("Triangle is Scalene")
else:
    print(None)