name='Juanito'  # Solicita el nombre del usuario
print(f"Hola, {name[2]}!")  # Saluda al usuario por su nombre

print(name[-1])  # Imprime la última letra del nombre
print(name[0:2])  # Imprime las dos primeras letras del nombre

# start, stop, step
print(name[0:5:2])  # Imprime desde el índice 0 hasta el 4, saltando de 2 en 2
print(name[:3])  # Imprime desde el inicio hasta el índice 2
print(name[2:])  # Imprime desde el índice 2 hasta el final
print(name[::-1])  # Imprime el nombre al revés
print(name[-3:-1])  # Imprime los dos caracteres antes del último
print(name[-1:-4:-1])  # Imprime los últimos tres caracteres en orden inverso
print(name[::2])  # Imprime todos los caracteres, saltando de 2 en 2
print(name[1::2])  # Imprime desde el índice 1 hasta el final, saltando de 2 en 2
print(name[-1:-5:-1])  # Imprime el nombre al revés usando índices negativos
print(name[-5::1])  # Imprime el nombre completo usando índices negativos