class Animal:
    def __init__(self, name,age=0):
        self.name = name
        self.age = age
    def info(self):
        print(f"Soy {self.name}, tengo {self.age} años")
    def sound(self):
        print(f"{self.name} hace un sonido.")  
    
class Dog(Animal):
    def __init__(self, name, age=0,breed="Unknown"):
        super().__init__(name, age)  # Llama al constructor de la clase padre
        self.breed = breed
    def sound(self):
        super().sound()  # Llama al método sound de la clase padre
        print(f"{self.name} says Woof!")
    def info(self): #overriding
        super().info()  # Llama al método info de la clase padre
        print(f"Soy de raza {self.breed}")
class Cat(Animal):
    def sound(self):
        super().sound()  # Llama al método sound de la clase padre  
        print(f"{self.name} says Meow!")

firulais=Dog("Firulais")
firulais.sound()
firulais.info()
rocky = Dog("Rocky",3,"Bulldog")
rocky.sound()
rocky.info()