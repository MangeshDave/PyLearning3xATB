# Walk in Directory

import os

for root, dir, files in os.walk("C:/Users/ADMIN$/PycharmProjects/PyLearning3xATB/July24"):
    print(f"Current Dir {root}")
    print(f"Sub Dir Dir {dir}")
    print(f"Files Dir Dir {files}")
    print(len(files))
