print (True and False)  # Resultado: False
print (True or False)   # Resultado: True   
print (not True)       # Resultado: False

age = 20
license = True
if age >= 18 and license:
    print("Puedes conducir")# Se imprime porque ambas condiciones son verdaderas
    
is_student = False
membership = True
if is_student or membership:
    print("Tienes acceso al descuento") # Se imprime porque una de las condiciones es verdadera 
    
is_raining = False
if not is_raining:
    print("No necesitas un paraguas") # Se imprime porque la condición es falsa y el operador not la invierte
