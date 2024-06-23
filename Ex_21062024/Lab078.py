# Decorators

def my_decorator(func):
    def wrapper():
        print("Starting........")
        print("******************")
        func()
        print("******************")
        print("Starting........")

    return wrapper()


@my_decorator  # without this decorator won't work
def say_hello():
    print("Hello")
