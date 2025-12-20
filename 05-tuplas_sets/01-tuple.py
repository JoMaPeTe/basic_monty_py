# Listas especiales
# Las tuplas son similares a las listas, pero son inmutables.
# Esto significa que una vez que se crea una tupla, no se puede modificar, agregar o eliminar elementos.
# Se definen utilizando paréntesis () en lugar de corchetes [].
# Crear una tupla
mi_tupla = (1, 2, 3, "cuatro", "cinco",3,2,2)
print("Tupla original:", mi_tupla)

# Ordenado, tiene indices como las listas
# inmutables una vez creadas no se pueden modificar, ni añadir ni eliminar elementos
# Permite duplicados
# Metodos disponibles para las tuplas:
# .count
print("Cantidad de veces que aparece '2' en la tupla:", mi_tupla.count(2))
# .Index
print("Índice del primer valor '3' en la tupla:", mi_tupla.index(3))
# Acceder a elementos de la tupla
print("Elemento en el índice 3:", mi_tupla[3])  

# mi_tupla[3] = "nuevo_valor"  # Esto generará un error porque las tuplas son inmutables
new_tuple = mi_tupla[3]
new_tuple = "nuevo_valor"
print("Intentando modificar la tupla:", new_tuple)
weekday_tuple = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
print("Días de la semana:", weekday_tuple)
