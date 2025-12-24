class Person:
    species = "Human"  # class variable atributo de clase publico
    def __init__(self, name, age): #constructor method imaginary method
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.name = name  # public instance variable atribute de instancia
        self.age = age    # instance variable
    def work(self):
        return (f"{self.name} is working.")
    def eat(self, food):
        if food.lower() == 'migas':
            return (f"{self.name} gets superpowers from {food}!")
        else:
            return (f"{self.name} is getting energy from {food}.")
person1 = Person("Alice", 30)
print(person1.name)  # Accessing public instance variable
print(person1.age)   # Accessing public instance variable   
print(Person.species)  # Accessing public class variable
print(person1.work())  # Calling public method
print(person1.eat('pasta'))  # Calling public method
print(person1.eat('Migas'))  # Calling public method with special food