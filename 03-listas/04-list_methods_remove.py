numbers_list = [1,2,3,4,5]

#pop
removed_element = numbers_list.pop()
print(removed_element)  # 5
print(numbers_list)  # [1, 2, 3, 4]

removed_element = numbers_list.pop(1)
print(removed_element)  # 2
print(numbers_list)  # [1, 3, 4]


#remove
numbers_list.remove(3)
print(numbers_list)  # [1, 4]
#numbers_list.remove(10)  # ValueError: list.remove(x): x not in list
numbers_list.insert(0,4)
numbers_list.insert(6,4) #insert at the end
print(numbers_list)  # [1, 4, 4, 4]
numbers_list.remove(4)  # removes the first occurrence of 4
print(numbers_list)  # [1, 4, 4]
numbers_list.clear()
print(numbers_list)  # []