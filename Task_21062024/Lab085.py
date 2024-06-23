# Task1 - Right Triangle Star Pattern
# n = 5
# *
# **
# ***
# ****
# *****

n = 5
my_list = []
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print("\n")

