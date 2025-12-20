for item in 'Python':
    print(item)   
for fruit in ['apple', 'banana', 'cherry']:
    print(fruit)
suma=0
fibonacci=[0]

for number in range(30):
    print(number)
    suma += number
print('Suma bucle', suma)
sum_list = sum(list(range(30)))
print("Sum function:", sum_list)
a=0
b=1
fibonacci=[0,1]

for i in range(2,30):
    fibonacci.append( fibonacci[i-2]+fibonacci[i-1])
print("Current fibonacci's number:", fibonacci)