# range(1, 10)
print(range(1,10))
# Sabemos que es iterable porque iter devuelve iterator
# <range_iterator object at 0x0000024BF8F68350>
print(iter(range(1,10)))
#step
for number in range(0,10,2):
    print(number)
for _ in range(0,10,2):
    print('Enviar notificacion')

