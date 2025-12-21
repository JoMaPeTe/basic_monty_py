#ayuda a acceder a un indes de string o list
# for index, char in enumerate('CualquierCosa'):
#     print(index,char)

# for index, char in enumerate([1,2,3,4,5]):
#     print(index,char)

for index, char in enumerate((range(100))):
    print(index,char)
    if index == 30:
        print('Yoja! Dejate iiiii')
          
# for index, char in enumerate(list(range(100))):
#     print(index,char)