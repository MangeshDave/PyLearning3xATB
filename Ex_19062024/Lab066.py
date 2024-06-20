# Double value with function

my_list = [1, 2, 3, 4, 5]
temp_list = []


def double(num):
    return num * 2


for i in range(5):
    temp_list.append(double(my_list[i]))

print(temp_list)
