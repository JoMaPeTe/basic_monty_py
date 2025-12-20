name = input("¿Cuál es tu nombre? ")  # Solicita el nombre del usuario  

year_of_birth = int(input("¿Cuál es tu año de nacimiento?"))
email = input('¿Cuál es tu correo?')# Solicita la edad
password = input('¿Cuál es tu contraseña?')# Solicita la contraseña     

print(f'''Resumen de la información proporcionada:
      Nombre: {name}
      Año de nacimiento: {year_of_birth}
      Tendras { 2050 - year_of_birth } años en 2050
      Correo: {email}
      Contraseña: {'*' * len(password)}''')
