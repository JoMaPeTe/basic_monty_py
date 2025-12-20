user= {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
    
}
#.copy()
user_copy = user.copy()  # Crear una copia del diccionario user
print("Copia del diccionario user:", user_copy)
user_copy['age'] = 31  # Modificar la copia
# print("Diccionario original user después de modificar la copia:", user)  # El diccionario original no se ve afectado
# print("Copia modificada:", user_copy)

# .pop() en listas no hacia falta, pero en  diccionarios hay que poner la key
removed_value = user.pop("email")  # Eliminar la clave "email" y obtener su valor   
print(user)  # Imprime el diccionario sin la clave "email"
print("Valor eliminado:", removed_value)  # Imprime el valor asociado a la clave "email"
# .popitem(), elimina el último par clave-valor agregado. Hay que tener en cuenta que los diccionarios son estructuras desordenadas en versiones anteriores a Python 3.7.
last_item = user.popitem()  # Eliminar el último par clave-valor agregado
print("Último par clave-valor eliminado:", last_item) #('age', 30)
print("Diccionario después de popitem():", user)  # Imprime {'name': 'Alice'}
#.update() cambia el valor de una key existente o agrega un nuevo par clave-valor si la clave no existe
user.update({"name": "Bob", "city": "KungDum"})  # Actualizar el nombre y agregar la ciudad
print("Diccionario después de update():", user)  # Imprime {'name': 'Bob', 'city': 'New York'}

#.append() no existe en diccionarios sino en listas
user["country"] = user.get("country", []) #si no existe country, lo crea con una lista vacía
user["country"].append("Narnia")
user["country"].append("Wakanda")
print("Diccionario después de agregar países:", user)
# Agregar un nuevo par clave-valor