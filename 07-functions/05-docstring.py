def hello(greet="Hola",name="Pepe"):
    """
        Prints a customized greeting message.
    """
    print(f"{greet}, {name}!")

hello(name="Marie",greet="Bonjour")

def multiply(a:float, b:float) -> float:
    """
        Multiplies two numbers and returns the result.
    """
    return a * b

print(multiply(4, 5))  # This will print 20