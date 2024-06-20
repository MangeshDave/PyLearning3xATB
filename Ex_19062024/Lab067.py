# Map
# 1. Takes each item from the list
# 2. Execute the function on it
# 3. Return the same number of elements (list)

my_list = [1, 2, 3, 4, 17]
temp_list = []
for i in my_list:
    temp_list.append(i*2)

print(temp_list)

def double_item(num):
    return num * 3



double_list = list(map(double_item, my_list))
print(double_list)
