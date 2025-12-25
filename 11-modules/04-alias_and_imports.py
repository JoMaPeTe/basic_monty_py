import math 
print (math.sqrt(16))  # Using the math module

#Importing specific function 
from math import sqrt 
print(sqrt(25))  # Using the imported function

#Importing specific functions with alias
from datetime import datetime as dt
print(dt.now()) #Using datetime alias
# Output: 2025-12-25 08:26:34.462325

#Importing entire module with alias
import statistics as stats
data = [1, 2, 3, 4, 5]
print(stats.mean(data))  # Using the statistics module alias
# Output: 3
import random as rnd
print(rnd.randint(1, 10))  # Using the random module alias
# Output:  a random integer between 1 and 10
from math import sin as seno, cos as coseno, pi,sqrt as square_root
print(seno(pi / 2) + square_root(25))
print(coseno(pi))# Using the aliased sine function

#Not recommended: Importing all functions from a module (conflict name risk)
from math import *
print(sqrt(36))  # Using the imported function without module prefix
#Name espace prefix helps to avoid conflicts
#Name conflicts can occur with this approach
# For example, if another module has a function named sqrt, it will override the math.sqrt function.
# It's better to import only what you need or use module aliases to avoid confusion.
