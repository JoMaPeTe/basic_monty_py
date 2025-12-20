# in
# not in
# Sirven para comprobar si un elemento está o no en una secuencia (lista, tupla, cadena, etc.)
print(9 in range(1, 10))  # Resultado: True    
print('a' in 'manzana')  # Resultado: True
print(5 in [1, 2, 3, 4, 5])  # Resultado: True
print('x' not in 'manzana')  # Resultado: True
fruits = ['manzana', 'banana', 'cereza']
if 'banana' in fruits:
    print("La banana está en la lista de frutas")  # Se imprime porque 'banana' está en la lista
    
word = "python"
if 'y' not in word:
    print("La letra 'y' no está en la palabra")  # No se imprime porque 'y' está en la palabra
numbers = [10, 20, 30, 40, 50]
if 25 not in numbers:
    print("El número 25 no está en la lista de números")  # Se imprime porque 25 no está en la lista    
# Combinación con operadores lógicos
colors = ['rojo', 'verde', 'azul']
if 'rojo' in colors and 'amarillo' not in colors:
    print("El color rojo está en la lista y el amarillo no")  # Se imprime porque ambas condiciones son verdaderas  
if 'a' in word or 'z' in word:
    print("La letra 'a' o la letra 'z' está en la palabra")  # Se imprime porque 'a' está en la palabra 
if not ('x' in word):
    print("La letra 'x' no está en la palabra")  # Se imprime porque 'x' no está en la palabra

