#jecuta un bloque de codigo mientras una condición es verdadera, y no sabemos exactamente cuantas iteraciones necesita
counter=1
#my_boolean = counter<=5 
while counter<=5:#my_boolean : 
    print(f'Number:{counter}')
    counter+=1
 #   my_boolean = counter<=5 # si no pongo esto tengo un buclee 
else:
    print('Ya está!')

response = ''

while response.lower() != 'python':
    response = input('Escribe python para salir: ')
print('Se fini!')