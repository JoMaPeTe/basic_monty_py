class Animal:
    def make_sound(self):
        print("Some generic animal sound")  
class Dog(Animal):
    def make_sound(self):
        print("Woof!")
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

def make_noise(animal):
    if isinstance(animal, Animal):
        animal.make_sound()
    else:
        print("This is not an animal!")

firulais = Dog()
michi = Cat()
wombat = Animal()
make_noise(firulais)  # Output: Woof!
make_noise(michi)      # Output: Meow!
make_noise("Berenjena")  # Output: This is not an animal!
make_noise(wombat)    # Output: Some generic animal sound