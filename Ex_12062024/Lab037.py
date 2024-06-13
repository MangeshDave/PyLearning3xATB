# Task2: Leap year checking
# Leap year is divisible by 4, not divisible by 100, but also divisible by 400

Year = int(input("Enter a year for leap year checking = "))

if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("Year is a leap")
        else:
            print("Year is not leap")
    elif Year % 4 == 0:
        print("Year is leap")
    else:
        print("Year is not leap")
else:
    print("Year is not leap")
