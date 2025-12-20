# coding: utf-8
'''
Comentario multilinia
'''
saludo = "Hola Mundo"
print(saludo)  # Imprime el saludo en la consola
name = input("¿Cómo te llamas? ")  # Solicita el nombre del usuario
lastname = input("¿Cuál es tu apellido? ")  # Solicita el apellido del usuario
PI = 3.1416  # Definición de la constante PI

_nombre_privado = "Variable privada" # Variable privada por convención PEP8 snake_case

# Variable pública string formating f-string
nombre_completo = f"{name} {lastname}"
nombre_completo1=f'{name} {lastname}'
nombre_completo2 = "{} {}".format(name, lastname)
nombre_completo3 = "%s %s" % (name, lastname)
nombre_completo4 = name + " " + lastname
nombre_completo5 = " ".join([name, lastname])
nombre_completo6 = " ".join((name, lastname))
nombre_completo7 = " ".join({name, lastname})# el orden puede variar en un set
nombre_completo8 = " ".join(name for name in [name, lastname])
nombre_completo9 = " ".join(map(str, [name, lastname]))
nombre_completo10 = " ".join([str(name), str(lastname)])
nombre_completo11 = " ".join([name.capitalize(), lastname.capitalize()])
print(f"Encantado de conocerte, {nombre_completo}!")  # Saluda al
print(f"Encantado de conocerte, {nombre_completo1}!")  # Saluda al
print(f"Encantado de conocerte, {nombre_completo2}!")  # Saluda al
print(f"Encantado de conocerte, {nombre_completo3}!")  # Saluda al
print(f"Encantado de conocerte, {nombre_completo4}!")  # Saluda al
print(f"Encantado de conocerte, {nombre_completo5}!")  # Saluda al
print(f"Encantado de conocerte, {nombre_completo6}!")  # Saluda al
print(f"Encantado de conocerte, {nombre_completo7}!")  # Saluda al
print(f"Encantado de conocerte, {nombre_completo8}!")  # Saluda al
print(f"Encantado de conocerte, {nombre_completo9}!")  # Saluda al
print(f"Encantado de conocerte, {nombre_completo10}!")  # Saluda al
print(f"Encantado de conocerte, {nombre_completo11}!")  # Saluda al

print(f"PI tiene un valor aproximado de {PI}")  # Imprime el valor de PI
# tipos de datos básicos
entero = 42  # Tipo entero  
flotante = 3.14  # Tipo flotante
cadena = "Esto es una cadena"  # Tipo cadena
booleano = True  # Tipo booleano False
lista = [1, 2, 3, 4, 5]  # Tipo lista
tupla = (1, 2, 3)  # Tipo tupla
conjunto = {1, 2, 3}  # Tipo conjunto set
diccionario = {"clave": "valor"}  # Tipo diccionario
diccionario_saludo = {"hola": "hello", "adios": "bye"}
informacion_personal = {
    "nombre": name,
    "apellido": lastname,
    "edad": 30
}
print(f"Tipos de datos: {type(entero)}, {type(flotante)}, {type(cadena)}, {type(booleano)}, {type(lista)}, {type(tupla)}, {type(conjunto)}, {type(diccionario)}")

print(nombre_completo.upper())  # Convierte el nombre completo a mayúsculas 
text1="Hola"
text2='Mundo'
text3 ='''Esto es un texto
multilínea'''
text4 ="""Otro texto
multilínea"""
print(text3)
print(text4)
#string formating
