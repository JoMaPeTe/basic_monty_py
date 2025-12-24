# inheritance = "is a type of" strong acomplishment
# composition = "has a posibility of" weaker acomplishment
class Flyer:
    def fly(self):
        print("Flying")
    def do_something(self):
        print("Doing something in Flyer")
class Swimmer:
    def swim(self):
        print("Swimming")
class Duck():  # Usando composición en lugar de herencia múltiple
    def __init__(self):
        self.flyer = Flyer()  # Composición: Duck tiene un objeto instancia de Flyer
        self.swimmer = Swimmer()  # Composición: Duck tiene un Swimmer
    def start_fly(self):
        self.flyer.fly()
    def start_swim(self):
        self.swimmer.swim()
    def quack(self):
        print("Quack!")
  #  def do_something(self):
   #     print("Doing something in Duck")
    def cursing(self):
       # super().do_something()  # ERROR ! AttributeError: 'super' object has no attribute 'do_something'
        self.flyer.do_something()  # Llama al método do_something de la clase Flyer
        print("Duck you mother ducker!")
donald = Duck()
donald.start_fly()    # Output: Flying
donald.start_swim()   # Output: Swimming
donald.quack()  # Output: Quack!
#donald.do_something()  # Output: ERROR: 'Duck' object has no attribute 'do_something'
donald.cursing()
#Method Resolution Order: ahora python ejecuta el do_something de flyer. Lo mismo super():no significa "la clase padre", sino "la siguiente clase en la lista MRO".
print(Duck.mro())# [<class '__main__.Duck'>, <class 'object'>]
print(Duck.__mro__)# (<class '__main__.Duck'>, <class 'object'>)