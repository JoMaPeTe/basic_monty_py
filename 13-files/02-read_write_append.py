# with abre el archivo y lo cierra,
# el manejo del archivo debe ir dentro del bloque with,
# al salir del bloque el archivo se cierra 
with open('example.txt') as my_file: #mode r by default
    print(my_file.readlines())

with open('example.txt', mode='r') as my_file:
    print(my_file.readlines())
# if it doesnt exist it creates the file
# if it exists it erases all in your file, and substitutes  it by your new content
with open('example.txt', mode='w') as my_file:
    print(my_file.write(':)'))
 #mode r+ allows to read and write   
with open('example.txt', mode='r+') as my_file:
    print(my_file.readlines())
    print(my_file.write(':>)'))
    text =(my_file.write('Greetings earthlings'))

with open('example.txt', mode='a') as my_file:
   
    text =(my_file.write('asdasd'))
    
    print(text)
    