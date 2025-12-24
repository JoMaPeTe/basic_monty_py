#print("Hello, World!" SyntaxError: '(' was never closed
#print(x)  # NameError: name 'x' is not defined

x="5"
y= 7
#print(x + y)  # TypeError: can only concatenate str (not "int") to str
#int("Hola") # ValueError: invalid literal for int() with base 10: 'Hola'
list=[1, 2, 3]
#print(list[5])  # IndexError: list index out of range
my_dict={"a":1, "b":2}
#print(my_dict["c"])  # KeyError: 'c'
x=10
#x.append(5)  # AttributeError: 'int' object has no attribute 'append'
x= 10 / 0 # ZeroDivisionError: division by zero