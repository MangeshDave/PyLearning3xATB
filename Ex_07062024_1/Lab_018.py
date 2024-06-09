#Use of List functions count, reverse, sort

shopping_list = ['milk', 'Poha', 'bread', 'butter']
print(shopping_list)
#count -> counts occurences of an element in list
count1 = shopping_list.count("sugar")
print(count1)
count1 = shopping_list.count("milk")
print(count1)
#reverse -> reverses the list
shopping_list.reverse()
print(shopping_list)
#sort -> sorts the list ascending
shopping_list.sort()
print(shopping_list)
abc = [1, 3, 5, 2, 8, 4]
abc.sort()
print(abc)
#sort -> sorts in descending if reverse=True given
abc.sort(reverse=True)
print(abc)