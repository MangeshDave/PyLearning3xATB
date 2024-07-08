# File IO
try:
    with open('Dummy.txt', 'r') as file:
        print(file.read())
        file.close()
except FileNotFoundError as fnfe:
    print("This file is not found")
    print(fnfe)
