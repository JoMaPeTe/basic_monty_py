option = ""
shopping_cart = []

while option != '7':
    print('*************')
    print("Carrito de compras")
    print('Opciones:')
    print('1- Agregar un producto')
    print('2- Eliminar un producto')
    print('3- Mostrar productos ordenados')
    print('4- Buscar un producto')
    print('5- Contar productos del carrito')
    print ('6- Vaciar carrito ')
    print ('7-Salir')
    print('*************')

 
    if option == '1':
        product = input("Ingrese el nombre del producto a agregar: ")
        if product not in shopping_cart:
            shopping_cart.append(product)
            print(f"Producto '{product}' agregado al carrito.")
        else:
            print(f"Producto '{product}' ya existe en el carrito.")
    elif option == '2':
        product = input("Ingrese el nombre del producto a eliminar: ")
        if product in shopping_cart:
            shopping_cart.remove(product)
            print(f"Producto '{product}' eliminado del carrito.")
        else:
            print(f"Producto '{product}' no encontrado en el carrito.")
    elif option == '3':
        if len(shopping_cart) == 0:
            print("El carrito está vacío.")
        else:
            shopping_cart.sort()
            print("Productos en el carrito ordenados alfabéticamente:")
            for item in shopping_cart:
                print(f"- {item}")
    elif option == '4':
        product = input("Ingrese el nombre del producto a buscar: ")
        if product in shopping_cart:
            print(f"Producto '{product}' encontrado en el carrito.")
        else:
            print(f"Producto '{product}' no encontrado en el carrito.") 
    elif option == '5':
        count = len(shopping_cart)
        print("El total de productos en el carrito es:", count)
    elif option == '6':
        shopping_cart.clear()
        print("El carrito ha sido vaciado.")
    elif option == '':
        pass
    else:
        print("Opción no válida. Por favor seleccione una opción del 1 al 7.")  
        
    print("Contenido actual del carrito de compras:", shopping_cart)  
    option = input("Seleccione una opción (1-7): ")
print("Contenido final del carrito de compras:", shopping_cart) 