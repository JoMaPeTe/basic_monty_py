'''
Un class static method sirve para definir un método que pertenece a la clase en sí misma y no a una instancia específica de la clase.
Podemos acceder a un metodo de clase para modificar atributos de clase en lugar de atributos de instancia o realizar operaciones que no dependen de los atributos de instancia.
'''

class Person:
    species = "Human"  # class variable atributo de clase publico
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def change_a_person_specy(self, new_species):
       # Esto crea una variable de instancia que "tapa" a la de clase (the object variable species is shadowing the class attribute with the same name)
        self.species = new_species
    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species
        
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.species)  # Output: Human
person1.change_a_person_specy("Alien")
print(person1.species)  # Output: Alien
print(person2.species)  # Output: Human
Person.change_species("Martian")
print(person1.species)  # Output: Martian , NO!! ERRROR, it prints Ali/en because the instance variable shadows the class variable
print(person2.species)  # Output: Martian, we print the class variable

print("Variables dentro de person1:", person1.__dict__)
print("Variables dentro de person2:", person2.__dict__)
print('---  --- --- ---')   
print("Variables dentro de la clase Person:", Person.__dict__)
person1.change_species("Reptilian") #person1 is Alice, but we are changing the class variable species, Alice keeps as Alien, but Bob will return Reptilian
print(person1.species)  # Output: Martian , NO!! ERRROR, it prints Ali/en because the instance variable shadows the class variable
print(person2.species)  # Output: Martian, we print the class variable

print("Variables dentro de person1:", person1.__dict__)
print("Variables dentro de person2:", person2.__dict__)
print('---  --- --- ---')   
print("Variables dentro de la clase Person:", Person.__dict__)