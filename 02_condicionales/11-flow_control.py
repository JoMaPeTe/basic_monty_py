edad = input("Ingresa tu edad: ")
edad = int(edad)
if edad < 0:
    print("La edad no puede ser negativa.")
elif edad <= 12:
    print("Eres un niño.")
elif edad <= 17:
    print("Eres menor de edad.")
elif edad <= 64:
    print("Eres adulto.")
else:
    print("Eres adulto mayor.")