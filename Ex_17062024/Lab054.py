# *args

def toppings(*args):
    for i in args:
        print(i, end="    ")


toppings("Tomato", "Cheese")
