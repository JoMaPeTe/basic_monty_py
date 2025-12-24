class Person:
  # class variable atributo de clase publico
    def __init__(self, name, age): #constructor method imaginary method
        self.name = name  
        self.age = age
        self.__password = "1234"  # name mangling _NOMBERCLASE__password # private instance variable atributo de instancia privado (convencion)  
            # _Person__password
    def __generate_password(self):  # private method metodo privado (convencion)
        return f"$${self.name}{self.age}"
    
person1 = Person("Alice", 30)
print(person1.name)  # Accessing public instance variable
#print(person1.__password) this will fail
print(person1._Person__password) # Accessing private instance variable using name mangling
print(person1._Person__generate_password()) # Calling private method using name mangling