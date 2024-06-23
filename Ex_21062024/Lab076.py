# SET operations

set1 = {1, 2, 3, 4}
set2 = {2, 3, 7, 8}
set3 = set1.union(set2)
print(set3)
set4 = set1.difference(set2)
print(set4)
set5 = set2.difference(set1)
print(set5)
set6 = set1.intersection(set2)
print(set6)
set7 = set2.intersection(set1)
print(set7)
