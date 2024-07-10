# OS Module

import os

# os.mkdir("Mangesh")

size = os.path.getsize("Lab143.py")
print(size)

if size != 0:
    print("File exist & has some contents")
else:
    print("File doesn't exists, No contents")
