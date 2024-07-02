# Method Overriding - Same name in the parent and
# child always override the parent functions
# super means call my parent function

class Father:
    def home(self):
        print("1BHK")

    def gold(self):
        print("1Kg")


class Son(Father):
    def home(self):
        super().home()      # Here parent function is called
        print("No House")

    def gold(self):         # Here child function overrides parent function
        print("5Kg")


pramod = Son()
pramod.home()
pramod.gold()
