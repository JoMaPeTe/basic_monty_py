#No pueden ser instanciadas directamente
#Sirven como base para otras clases. Es un mapa para decirle a las clases hijas que deben implementar ciertos métodos.
#importar ABC(Abstract Base Class) y abstractmethod decorator 
from abc import ABC, abstractmethod   

class Animal(ABC):  # Clase abstracta porque hereda de ABC
    def __init__(self, name):   
        self.name = name
    @abstractmethod #se declara pero no se implementa en la clase base, sino en las subclases
    def sound(self):  # Método abstracto
        pass
    
    def info(self): #puede tener métodos concretos, no abstractos
        print(f"Soy {self.name}")

animal = Animal("Animal")  # Can't instantiate abstract class Animal without an implementation for abstract method 'sound'