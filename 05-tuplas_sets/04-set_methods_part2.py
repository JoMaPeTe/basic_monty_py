# .union() crea un nuevo set que es la unión de dos sets, es decir, contiene todos los elementos de ambos sets sin duplicados.
set_a = {1, 2, 3}
set_b = {2, 3, 4, 5}   
set_union = set_a.union(set_b)
print("Unión de set_a y set_b:", set_union) #Unión de set_a y set_b: {1, 2, 3, 4, 5}
# .intersection() crea un nuevo set que es la intersección de dos sets, es decir, contiene solo los elementos que están en ambos sets.
set_intersection = set_a.intersection(set_b)
print("Intersección de set_a y set_b:", set_intersection) #Intersección de set_a y set_b: {2, 3}
# .difference() crea un nuevo set que contiene los elementos que están en el primer set pero no en el segundo.
set_difference = set_a.difference(set_b)    
print("Diferencia de set_a y set_b (elementos en set_a pero no en set_b):", set_difference) #Diferencia de set_a y set_b (elementos en set_a pero no en set_b): {1}


