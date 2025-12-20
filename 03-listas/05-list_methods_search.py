numbers_list = [1, 2, 3, 4, 5]
#index
index_of_3 = numbers_list.index(3)
print(index_of_3)  # 2  
#index with start and end
index_of_4 = numbers_list.index(4, 2, 5)
print(index_of_4)  # 3  # starts searching from index 2 to 4
#ValueError: 10 is not in list
#index_of_10 = numbers_list.index(10)
#print(index_of_10) 
#index_of_4 = numbers_list.index(4, 0, 2)
#print(index_of_4)  # ValueError: 4 is not in list between index 0 and 1
#in operator
is_3_in_list = 3 in numbers_list
print(is_3_in_list)  # True
is_10_in_list = 10 in numbers_list
print(is_10_in_list)  # False
#count
print(numbers_list.count(4))  # 1
numbers_list.append(4)  
print(numbers_list)  # [1, 2, 3, 4, 5, 4]
print(numbers_list.count(4))  # 2 el 4 aparece dos veces
print(numbers_list.count(10))  # 0