class Animal:
    def __init__(self, name):
        self.name = name
    def sleep(self):
        print(f"{self.name} is sleeping.")  
    
class Dog(Animal):
    def sound(self):
        print(f"{self.name} says Woof!")
class Cat(Animal):
    def sound(self):
        print(f"{self.name} says Meow!")

firulais=Dog("Firulais")
michi=Cat("Michi")
firulais.sleep()
firulais.sound()

michi.sleep()
michi.sound()