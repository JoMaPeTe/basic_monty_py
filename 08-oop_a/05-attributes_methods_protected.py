class Person:
  # class variable atributo de clase publico
    def __init__(self, name): #constructor method imaginary method
        self.name = name  
        self._energy = 100  # protected instance variable atributo de instancia protegido (convencion)  
    def _waste_energy(self, amount):  # protected method metodo protegido (convencion)
        self._energy -= amount
        self._energy = max(self._energy, 0)
        return self._energy
person1 = Person("Alice")
print(person1.name)  # Accessing public instance variable
# Accessing protected instance variable (not recommended, but possible)
print(person1._energy)
# Calling protected method (not recommended, but possible)
print(person1._waste_energy(30))
