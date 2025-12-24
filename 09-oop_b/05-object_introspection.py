#Capacidad de examinar los atributos y métodos de un objeto en tiempo de ejecución
x=[1, 2, 3]
print(type(x))  # Devuelve <class 'list'>
print(dir(x))  # Lista de atributos y métodos del objeto x
#['__add__', '__class__', '__class_getitem__', '__contains__',
# '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__',
# '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__init_subclass__', '__iter__', '__le__',
# '__len__', '__lt__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
# '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
# '__str__', '__subclasshook__', 'append', 'clear', 'copy',
# 'count', 'extend', 'index', 'insert', 'pop', 'remove',
# 'reverse', 'sort']
print(hasattr(x, 'append'))  # Devuelve True
print(getattr(x, 'append'))  # Devuelve el método append
print(callable(x.append))  # Devuelve True
append_method = getattr(x, 'append')
append_method(4)
print(x)  # Output: [1, 2, 3, 4]
print(id(x))  # Devuelve el identificador único del objeto x