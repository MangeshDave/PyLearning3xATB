# Inheritance OOPs
# 4. Multiple Inheritance -> Father, Mother -> Son

class Father:
    f_house = "2BHK"


class Mother:
    m_house = "3BHK"


class Son(Father, Mother):
    s_house = "1BHK"


son = Son()
father = Father()
mother = Mother()
print("Son has access to ")
print(son.f_house)
print(son.m_house)
print(son.s_house)
print("Father has access to ")
print(father.f_house)
print("Mother has access to ")
print(mother.m_house)
