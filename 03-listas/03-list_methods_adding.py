number_list = [1, 2, 3]
print(number_list)  # [1, 2, 3]
number_list.append(4)
print(number_list)  # [1, 2, 3, 4]
number_list.append(5)
print(number_list)  # [1, 2, 3, 4, 5]
print(number_list.append(6))  # None

number_list.insert(0,24)
print(number_list)  # [24, 1, 2, 3, 4, 5, 6]
number_list.insert(3,15)
print(number_list)  # [24, 1, 2, 15, 3, 4, 5, 6]

number_list.extend([7,8,9])
print(number_list)  # [24, 1, 2, 15,