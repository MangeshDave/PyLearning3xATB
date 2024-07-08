# File Handling

file = open("Dummy_File.txt", "r")
content = file.readline()
content2 = file.readlines()
print(content)
print(content2)
file.close()
