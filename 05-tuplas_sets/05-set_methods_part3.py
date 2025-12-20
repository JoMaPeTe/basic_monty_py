set1 ={1,2,3,4,5}
set2 ={4,5,6,7,8}
# .symmetric_difference() crea un nuevo set que contiene los elementos que están en uno de
# los sets pero no en ambos.  Lo contrario de la intersección.
set_symmetric_difference = set1.symmetric_difference(set2)
print("Diferencia simétrica entre set1 y set2:", set_symmetric_difference) #Diferencia simétrica entre set1 y set2: {1, 2, 3, 6, 7, 8}
# .issubset() verifica si todos los elementos    del primer set están en el segundo set
set1={1,2,3}
set2={1,2,3,4,5}

is_subset = set1.issubset(set2)
print("¿set1 es un subconjunto de set2?", is_subset) #¿set1 es un subconjunto de set2? False
# .issuperset() verifica si el primer set contiene todos los elementos del segundo set
is_superset = set2.issuperset(set1)
print("¿set2 es un superconjunto de set1?", is_superset) #¿set2 es un superconjunto de set1? False
# .clear() elimina todos los elementos del set
set1.clear()
print("set1 después de clear():", set1) #set1 después de clear(): set()
