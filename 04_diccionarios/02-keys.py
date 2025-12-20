user={
    "name": "Alice",
    "age": 30,

    "email": "alice@example.com",
    #[1,2,3]:"spodkfpsok", la lista no es un tipo inmutable, por lo que no puede ser clave
    (1,2,3):"valor tupla"  # Las tuplas son tipos inmutables y pueden ser claves
}
user["name"] = "Bob"  # Modificar el valor asociado a la clave "name"
user["age"] = 31   # Modificar el valor asociado a la clave "age"
print(user["name"])  # Imprime: Bob
user["city"] = "Los Angeles"  # Modificar el valor asociado a la clave "city"
print(user)   # Imprime: {'name': 'Bob', 'age': 31, 'email': '
print(user[(1,2,3)])  # Imprime: valor tupla