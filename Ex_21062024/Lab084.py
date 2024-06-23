# Order of dictionary is generally unordered

my_dict = dict()
my_dict["b"] = 5
my_dict["d"] = 4
my_dict["c"] = 6
my_dict["a"] = 2

for i, j in my_dict.items():
    print(i, j)

from collections import OrderedDict
od = OrderedDict()
od["b"] = 50
od["a"] = 75
od["d"] = 40
print(od)
