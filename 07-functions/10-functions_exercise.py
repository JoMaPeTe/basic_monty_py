import string
import random
#letras "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# números "0123456789
# símbolos "!@#$%^&*()-_=+[{]}\|;:',<.>/?~"
# caracteres = letras + números + símbolos
# Formula simple: item * 7 +3)% len(caracteres)
#Entrada 8
#Salida: &D^#/23SN

def generate_password(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    characters = letters + numbers + symbols
    password = ""
    for i in range(length):
        index = (i * 7 + 3) % len(characters)
        password += characters[index]
    return password
# Ejemplo de uso    
length = int(input("Enter the length of the password: "))
print(generate_password(length))  # Salida: dkryFMT0


def generate_password2(length_2):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = []
    for i in range(length_2):
        random_char = random.choice(characters)
        password.append(random_char)
    return ''.join(password)
# Ejemplo de uso
length2 = int(input("Enter the length of the password: "))
print(generate_password2(length2))  # Salida: