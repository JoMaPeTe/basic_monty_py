
def hello(greet="Hola",name="Pepe"):
    print(f"{greet}, {name}!")

hello()
hello("Hello")
hello(name="Alice")

#keyword arguments
hello("Paco","Buenos días")
hello(name="Marie",greet="Bonjour")
