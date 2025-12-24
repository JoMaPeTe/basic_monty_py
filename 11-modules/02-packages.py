#from abc import ABC, abstractmethod   
""" from my_package import messages, math_utils
print(math_utils.addition(10, 15))
greeting = messages.greet("Alice")
farewell = messages.bye("Alice")
print(greeting)
print(farewell) """
from my_package import addition, greet, bye
print(addition(10, 15))
greeting = greet("Alice")
farewell = bye("Alice")
print(greeting)
print(farewell)