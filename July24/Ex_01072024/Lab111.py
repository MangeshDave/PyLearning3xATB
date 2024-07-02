# Inheritance OOPs
# 1. Single Inheritance -> Father & Son

class Father:
    gold = "2Kg-Gold"

    def father_method(self):
        print("This is father method")


class Son(Father):                  # Usage
    silver = "1Kg-Silver"

    def son_method(self):
        print("This is son method")


pramod = Son()
print(pramod.gold)
print(pramod.silver)
pramod.father_method()
pramod.son_method()
father1 = Father()
# father1.son_method()      Not allowed
# print(father1.siver)      Not allowed
