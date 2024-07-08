try:
    with open("Dummy_File.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as fnfe:
    print(fnfe)
finally:
    print("File closing")
    file.close()
