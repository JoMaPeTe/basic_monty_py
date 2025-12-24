inventory = {
    'chocolate': 10,
    'buñuelos':7,
    'rosco':4,
    'chicles':1,
    'pestiño':2,
    'torrija':3
}
cart =[]
print('Bienvenido a pasteles Dev')
print('Inventario: ')
for product, price in inventory.items():
    print(f'{product.capitalize()}: ${price}')
    
option = ' '
while True:
    print('*************')
    option=input("Que dulce desea comprar?(escribir 'salir' para terminar): ").lower()
    if option== ('salir'):
        break
    elif option in inventory:
        cart.append(option)
        print(f'{option.capitalize()} agregado al carrito.')
    else:
        print('Producto no disponible.')
print('*************')
total = 0
print('Productos en el carrito:')
for item in cart:
    print(f'- {item.capitalize()}: ${inventory[item]}')
    total += inventory[item]

print(f'Total a pagar: ${total}')