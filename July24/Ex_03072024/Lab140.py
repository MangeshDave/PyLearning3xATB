with open("Dummy_File.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line, end="\n")
