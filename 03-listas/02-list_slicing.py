shopping_card = [ 'camisas', 'pantalones', 'zapatos', 'calcetines', 'chaqueta', 'bufanda' ]

print(shopping_card[0])  # ['zapatos', 'calcetines', 'chaqueta']
print(shopping_card[1:4])  # ['pantalones', 'zapatos', 'calcetines']
print(shopping_card[:3])    # ['camisas', 'pantalones', '
#print(shopping_card[9])    
new_list = shopping_card[2:5]
print(new_list)  # ['zapatos', 'calcetines', 'chaqueta']
print(shopping_card)    # ['camisas', 'pantalones', 'zapatos', 'calcetines', 'chaqueta', 'bufanda']

new_list[0] = 'sandalias'
print(new_list)  # ['sandalias', 'calcetines', 'chaqueta']
print(shopping_card)    # ['camisas', 'pantalones', 'zapatos', 'calcetines', 'chaqueta', 'bufanda']\
shopping_card[2:5] = ['botas', 'guantes', 'gorra']
print(new_list)  # ['sandalias', 'calcetines', 'chaqueta']
print(shopping_card)   # ['camisas', 'pantalones', 'botas', 'guantes', 'gorra', 'bufanda']

new_list2_= shopping_card[:] # list slicing de toda la lista
print(new_list2_)  # ['camisas', 'pantalones', 'botas
new_list2_[0] = 'remera'
print(new_list2_)  # ['remera', 'pantalones', 'botas
print(shopping_card)   # ['camisas', 'pantalones', 'botas', 'guantes', 'gorra', 'bufanda']