class Person:
    species = "Human"  # class variable atributo de clase publico
    def __init__(self, name, age): #constructor method imaginary method
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.name = name  # public instance variable atribute de instancia
        self.age = age    # instance variable
    @classmethod # class method recibe cls como primer parametro, se puede llamar desde dentro de la propia clase, desde la clase o desde una instancia
    def changes_species_info(cls, species):
        cls.species = species

    @staticmethod # static method  no recibe ni self ni cls, se puede llamar desde dentro de la propia clase, desde la clase o desde una instancia
    def is_older(age):
        return age >= 18
    
    
print (Person.is_older(20))  # True  Static Method call from the class without creating an instance

person1= Person("Alice", 30)
print(person1.is_older(person1.age))  # True Static Method call from an instance