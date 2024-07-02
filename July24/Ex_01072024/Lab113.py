# Inheritance OOPs
# 3. Multilevel Inheritance -> GrandPa - Father - Son

class Grandpa:
    g_house = "3BHK"


class Father(Grandpa):
    f_house = "2BHK"


class Son(Father):
    s_house = "1BHK"


son = Son()
father = Father()
grandpa = Grandpa()
print("Son has access to")
print(son.s_house)
print(son.f_house)
print(son.g_house)
print("Father has access to")
print(father.f_house)
print(father.g_house)
print("GrandPa has access to")
print(grandpa.g_house)
