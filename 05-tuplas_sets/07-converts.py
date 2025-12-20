list1 = [1, 2, 2, 3, 4, 4, 5,1,2,6,4,9,10]
tuple1 = tuple(list1)

print("Lista original: ", list1)
print("Tupla: ", tuple1)

set1 = set(list1)
print("Set resultante: ", set1)
set2 = set(tuple1)
print("Set a partir de la tupla: ", set2)

# Crear un tipo de dato a diccionario a partir de una lista de tuplas
list_of_tuples = [("a", 1), ("b", 2), ("c", 3), ("a", 4)]
dict_from_tuples = dict(list_of_tuples)
print("Lista de tuplas:", list_of_tuples)
print("Diccionario a partir de lista de tuplas:", dict_from_tuples)
