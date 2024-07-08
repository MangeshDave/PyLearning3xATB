# File IO
try:
    with open('Dummy.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as fnfe:
    print("This file is not found")
    print(fnfe)
finally:
    print("Closing the file")
    try:
        file.close()
    except NameError as ne:
        print(ne)
