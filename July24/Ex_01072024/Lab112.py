# Inheritance OOPs
# 2. Hierarchical Inheritance -> Father & son1, son2, son3....

class Father:
    father_house = "4BHK"

    def father_method(self):
        print("This is father method")


class Pramod(Father):  # Usage
    pramod_house = "1BHK"

    def pramod_method(self):
        print("This is pramod method")


class Mangesh(Father):  # Usage
    mangesh_house = "2BHK"

    def mangesh_method(self):
        print("This is mangesh method")


class Deepak(Father):  # Usage
    deepak_house = "3BHK"

    def deepak_method(self):
        print("This is deepak method")


pramod = Pramod()
mangesh = Mangesh()
deepak = Deepak()
print(pramod.father_house)
print(pramod.pramod_house)
print(mangesh.father_house)
print(mangesh.mangesh_house)
print(deepak.father_house)
print(deepak.deepak_house)
pramod.father_method()
pramod.pramod_method()
father1 = Father()
pramod.father_method()
mangesh.father_method()
deepak.father_method()
# father1.pramod_house()      Not allowed
# father1.deepak_method()      Not allowed
# mangesh.pramod_method()       Not allowed
# print(pramod.deepak_house)       Not allowed
