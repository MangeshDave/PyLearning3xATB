#Use of List functions index, clear, print list elements, copy

shopping_list = ['milk', 'Poha', 'bread', 'butter']
print(shopping_list)
#index -> finds index of an element
index1 = shopping_list.index("butter")
print(index1)
print(shopping_list[-1])
print(shopping_list[1])
#copy -> copies a list in a variable
shopping_list1 = shopping_list.copy()
print(shopping_list1)
#clear -> deletes all elements of list
shopping_list.clear()
print(shopping_list)