# Factorial

year = 200

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(year, "is leap lear")
else:
    print(year, "is not leap year")
