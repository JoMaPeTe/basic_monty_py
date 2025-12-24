#dunder stands for "double underscore" (doble guion bajo) and refers to special methods in Python that have names surrounded by double underscores, like __init__, __str__, __add__, etc. These methods allow you to define how objects of your class behave with built-in operations and functions.
#These methods are also known as "magic methods" or "special methods".

from operator import add


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello I'm {self.name}, I'm {self.age}"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

    def __add__(self, other):
        if isinstance(other, Person):
            return Person(f"{self.name} & {other.name}", self.age + other.age)
        return NotImplemented

    """    def __len__(self):
        return len(self.name) """
persona1 = Person("Alice", 30) 
print (persona1) # sin __str__ : <__main__.Person object at 0x0000016F65FD86E0>
#print (len(persona1)) # Output: 5 (length of the name "Alice"). Si no está definido TypeError: object of type 'Person' has no len()
print (repr(persona1)) # Output: Person('Alice', 30)
print(add(persona1 , persona1)) # Output: Person('Alice & Alice', 60)

# Usamos comprensión de listas para filtrar solo los dunder
dunder_methods = [method for method in dir(persona1) if method.startswith('__') and method.endswith('__')]

print(f"Dunder methods encontrados: {len(dunder_methods)}")
# Usamos pprint (pretty print) para que se vea ordenado en columnas
import pprint
pprint.pprint(dunder_methods)