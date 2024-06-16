# Match case -> Like switch case

numbers = int(input("Enter a number: "))

match numbers:
    case 1:
        print("You are in case ", numbers)
    case 2:
        print("You are in case ", numbers)
    case 3:
        print("You are in case ", numbers)
    case 4:
        print("You are in case ", numbers)
    case _:
        print("No idea")

day = input("Enter a month to print its days, e.g. 1 = Jan, 2 = Feb, ... = ")
day.lower()
match day:
    case "jan":
        print("January has 31 days")
    case "feb":
        print("February has 28/29 days")
    case "mar":
        print("March has 31 days")
    case "apr":
        print("April has 30 days")
    case "may":
        print("May has 31 days")
    case "jun":
        print("June has 30 days")
    case "jul":
        print("July has 31 days")
    case "aug":
        print("August has 31 days")
    case "sep":
        print("September has 30 days")
    case "oct":
        print("October has 31 days")
    case "nov":
        print("November has 30 days")
    case "dec":
        print("December has 31 days")
    case _:
        print("Please enter valid month")
