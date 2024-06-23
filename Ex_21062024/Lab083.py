# Dictionary to List

my_dict = dict(name="Dave", age=50, address="Pune")
my_list_keys = list(my_dict.keys())
print(my_list_keys)
my_list_values = list(my_dict.values())
print(my_list_values)

for i in my_dict.keys():
    print(i)

for i in my_dict.values():
    print(i)

for i,j in my_dict.items():
    print(i, j, sep=":")
