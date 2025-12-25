# icacls sinpermisos.txt /deny "$($env:USERNAME):(R)"
# icacls sinpermisos.txt /reset
try:
    with open("sinpermisos.txt", "r") as file:
        content= file.read()
        print(content)
except PermissionError as err:
    print("No tiene permisos sobre el archivo")
except FileNotFoundError as err:
    print("El archivo no existe")
except Exception as err:
    print(f"Ocurrió un error:{type(err).__name__}")