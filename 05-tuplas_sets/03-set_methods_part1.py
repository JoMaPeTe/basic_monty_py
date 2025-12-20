#conjuntos ver diagramas de Ben

#.add
my_set = {1, 2, 3}
print("Conjunto original:", my_set)
my_set.add(3)
my_set.add(4)
print("Conjunto después de agregar 4:", my_set)

#.remove
my_set.remove(2)

# my_set.remove(7)  # Esto generará un error porque el elemento 7 no está en el conjunto
print("Conjunto después de eliminar 2:", my_set)
#.discard igual que remove pero no genera error si el elemento no existe
my_set.discard(5)  # No genera error aunque el 5 no esté en el conjunto
print("Conjunto después de descartar 5 (sin error):", my_set)

#.pop() elimina y devuelve un elemento aleatorio del conjunto
removed_element = my_set.pop()  
print("Elemento eliminado con pop():", removed_element)
print("Conjunto después de pop():", my_set) 