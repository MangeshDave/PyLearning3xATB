# OS Module

import os

# Get file modification time

mtime = os.path.getmtime("Lab144.py")
print(mtime)

import time

print(time.gmtime(mtime))
print(time.localtime())
