# Tuple -> Same as list, but immutable (Its values cannot be changed by accessing individual elements)

my_tuple = (1, 2, 3, 4, 5)
# my_tuple(0) = 60              # Not possible -> Immutable
print(my_tuple)

my_list = [1, 2, 3, 4, 5]
my_list[0] = 10                    # Possible -> Mutable
print(my_list)
