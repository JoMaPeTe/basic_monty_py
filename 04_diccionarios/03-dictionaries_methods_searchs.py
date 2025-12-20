user= {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
    (1,2,3):"valor tupla"
}

# .get()
print(user.get("name"))  # Imprime: Alice
# in
print("Alice" in user)  # Imprime: False porque "Alice" es un valor, no una clave
print("name" in user)  # Imprime: True
print("address" in user)  # Imprime: False  
# not in
print("address" not in user)  # Imprime: True
print("email" not in user)  # Imprime: False
# .keys()
print(user.keys())  # Imprime: dict_keys(['name', 'age', 'email', (1, 2, 3)])
print("Alice" in user.keys())  # Imprime: False es como el in user por default
# .values()
print(user.values())  # Imprime: dict_values(['Alice', 30, 'alice@example.com', 'valor tupla'])
print("Alice" in user.values())  # Imprime: True
print(user.items())  # Imprime: dict_items([('name', 'Alice'), ('age', 30), ('email', '