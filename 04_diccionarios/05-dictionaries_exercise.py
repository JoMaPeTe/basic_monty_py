students= {
    "Ana": [8,7,9],
    "Luis": [6,5,7],
    "Marta": [9,9,10]
}

# Agregar un nuevo estudiante con sus notas
students["Carlos"] = [7,8,9]
print("Diccionario después de agregar a Carlos:", students)
students.update({"Lucia": [10,10,9], "Jorge": [5,6,7]})
print("Diccionario después de agregar a Lucia y Jorge:", students)
# Sacar el promedio de las notas de un estudiante

def calcular_promedio(notas):
    return sum(notas) / len(notas)  
def promedio_estudiante(nombre):
    if nombre in students:
        notas = students[nombre]
        promedio = calcular_promedio(notas)
        return promedio
    else:
        return None
    
def mensaje_promedio(nombre):
    promedio = promedio_estudiante(nombre)
    if promedio is not None:
        return f"El promedio de {nombre} es {promedio:.2f}"
    else:
        return f"El estudiante {nombre} no está en el diccionario."

alumno = input("Ingrese el nombre del estudiante: ")
print(mensaje_promedio(alumno))