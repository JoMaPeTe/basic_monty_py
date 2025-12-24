#print(True == 1)
#print('' == 1)
#print([] == 1)
#print (10 == 10.0)


# Is compara en memoria 0x1234ab
new_list = []
other_list = []
print(new_list is other_list)  # Resultado: Fals  porque ambas listas están en diferentes ubicaciones de memoria
print(new_list == other_list)  # Resultado: True porque ambas listas están vacías y tienen el mismo contenido