class Person:
    def __init__(self, name, age): #constructor method imaginary method
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.name = name  # instance variable
        self.age = age    # instance variable

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1)
print(f"Person 1: Name = {person1.name}, Age = {person1.age}")
print(f"Person 2: Name = {person2.name}, Age = {person2.age}")