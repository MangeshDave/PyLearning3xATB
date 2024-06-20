# Functions -> 4 types

# 1. without arguments without return
print("1. without arguments without return")


def greet():
    print("Hello")


greet()

# 2. with arguments without return
print("2. with arguments without return")


def greet(name):
    print("Hello", name)


greet("Mangesh")

# 3. without arguments with return
print("3. without arguments with return")


def greet():
    return "Mangesh"


name = greet()
print(name)

# 4. with arguments with return
print("4. with arguments with return")


def greet(name1):
    print(name1)
    return "Dave"


result = greet("Pramod")
print(result)
