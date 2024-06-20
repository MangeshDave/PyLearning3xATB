# Lambda & Map
my_list = [1, 2, 3, 4, 5]
double_item = lambda num: num * 3

double_list = list(map(double_item, my_list))
print(double_list)

double_list = list(map(lambda num: num * 2, my_list))
print(double_list)

print(list(map(lambda num: num * 4, my_list)))
