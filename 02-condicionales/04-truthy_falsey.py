#Truthy
print(bool(True))          # Verdadero
print(bool(1))             # Entero distinto de cero
print(bool(-1))            # Entero distinto de cero
print(bool(0.5))           # Flotante distinto de cero
print(bool(-0.5))          # Flotante distinto de cero  
print(bool(1j))            # Número complejo distinto de cero
print(bool("Hola"))        # Cadena no vacía
print(bool([1, 2, 3]))     # Lista no vacía
print(bool((1, 2, 3)))     # Tupla no vacía
print(bool({1, 2, 3}))     # Conjunto no vacío
#Falsey
print(bool(False))         # Falso 
print(bool(0))             # Entero cero
print(bool(0.0))           # Flotante cero
print(bool(0j))            # Número complejo cero
print(bool(""))            # Cadena vacía
print(bool([]))            # Lista vacía
print(bool(None))          # Valor None
