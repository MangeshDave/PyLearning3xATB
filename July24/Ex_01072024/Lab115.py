# Inheritance OOPs
# 5. Hybrid Inheritance -> Mix of all other

class GrandPa:
    g_house = "4BHK"


class Father(GrandPa):  # Single inheritance
    f_house = "1BHK"


class Mother(GrandPa):  # when this came above became hierarchical inheritance
    m_house = "2BHK"


class Grand_Child(Father, Mother):  # Multilevel + Multiple
    GC_house = "My House 3BHK"


grand_child = Grand_Child()
print(grand_child.g_house)
print(grand_child.f_house)
print(grand_child.m_house)
print(grand_child.GC_house)
