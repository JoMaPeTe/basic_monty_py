#Una interfaz es una clase abstracta que solo contiene métodos abstractos (sin implementación).
#Define un contrato que las clases que implementan la interfaz deben seguir.
#Asegura que disintas clases tengan los mismos métodos, aunque hagan cosas distintas, permitiendo la interoperabilidad.
#importar ABC(Abstract Base Class) y abstractmethod decorator 
from abc import ABC, abstractmethod   
#Definición de una interfaz pura
class IAnimal(ABC):  # A veces se pone 'I' delante por convención
    
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass
    
#Definicion de una interfaz no pura (clase abstracta con métodos concretos)
class Animal(ABC):  # Clase abstracta porque hereda de ABC
    def __init__(self, name):   
        self.name = name
    @abstractmethod #se declara pero no se implementa en la clase base, sino en las subclases
    def sound(self):  # Método abstracto
        pass
    #Si pongo otro método concreto, no abstracto, está permitido, pero ya no es una interfaz pura.
    def info(self): # puede tener métodos concretos, no abstractos
       print(f"Soy {self.name}")

#animal = Animal("Animal")  # Can't instantiate abstract class Animal without an implementation for abstract method 'sound'
class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Duck(IAnimal):
    def sound(self):
        return "Quack!"
    def move(self):
        return "The duck swims and flies."

taquito=Dog("Taquito")  # Si no tiene sound implementado=> TypeError: Can't instantiate abstract class Dog with abstract method sound
michi=Cat("Michi")      # Si no tiene sound implementado=>TypeError: Can't instantiate abstract class Cat with
taquito.info()  # Output: Soy Taquito
print(taquito.sound())  # Output: Woof! 
michi.info()   # Output: Soy Michi
print(michi.sound())    # Output: Meow!
donald=Duck()
print(donald.sound())  # Output: Quack! 
print(donald.move())   # Output: The duck swims and flies.