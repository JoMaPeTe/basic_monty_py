nombre = input("¿Cómo te llamas? ")
#skill= input("¿Sabes python? (si/no) ")
skills= input("Ingrese sus habilidades separadas por comas (por ejemplo: python,java,c++) ")
años_experiencia = input("¿Cuántos años de experiencia tienes en programación? ")
años_experiencia = int(años_experiencia)

skill_list = skills.lower().split(',')
evaluated_skills = 'python' in skill_list or 'django' in skill_list
""" if evaluated_skills and años_experiencia >= 3:
        print(f"Felicidades {nombre}, cumples con los requisitos para el puesto.OPTIMO")
    elif evaluated_skills and 1 < años_experiencia < 3:
        print(f"Felicidades {nombre}, cumples con los requisitos para el puesto.BUENO")
    elif evaluated_skills and años_experiencia <= 1:
        print(f"Felicidades {nombre}, cumples con los requisitos para el puesto.REGULAR")
    else:
        print(f"Lo sien to {nombre}, no cumples con los requisitos para el puesto.")"""
result =''
if evaluated_skills:
   if años_experiencia >= 3:
        result = ' OPTIMO'
   elif 1 < años_experiencia < 3:
        result = ' BUENO'
   else:  
        result = ' REGULAR'
else:
    result = ' Lo siento, no cumples con los requisitos de habilidades.'    

print (f"Felicidades {nombre}, cumples con los requisitos para el puesto, es {result}")