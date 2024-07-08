# File IO
try:
    with open('Dummy_File.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as fnfe:
    print("This file is not found")
    print(fnfe)
finally:
    print("Closing the file")
    file.close()
