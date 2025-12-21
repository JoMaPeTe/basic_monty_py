numbers=[1,2,3,4,5]

#Itereables: iterables, listas,diccionarios, set, tuplas.
# for number in numbers:
#     print(number)
    
#Iterador: objeto que recuerda su posicion
iterator = iter(numbers)
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))

#Dict
user = {
    'name':'Ryland Grace',
    'age':45,
    'can_go_on_space_walk':True,
    'perform_extra_vehicular_activities':True,
    'breed_alien_Taumebas':True,
    'grow_Astrofagos':False
}
#keys
for item in user:
    print(item)
#keys
for item in user.keys():
    print(item)
#values
for item in user.values():
    print(item)
#Tuples
for item in user.items():
    print(item)
#Destructure
for item in user.items():
    key, value= item
    print(key,value)
    
#Desectructura2
for key,value in user.items():
    print(key,value)