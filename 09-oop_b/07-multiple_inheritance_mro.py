class Flyer:
    def fly(self):
        print("Flying")
    def do_something(self):
        print("Doing something in Flyer")
class Swimmer:
    def swim(self):
        print("Swimming")
class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")
  #  def do_something(self):  #First to be looked for in MRO
   #     print("Doing something in Duck")
    def cursing(self):
        super().do_something()  # Llama al método do_something de la clase padre más cercana en MRO
        print("Duck you mother ducker!")
donald = Duck()
donald.fly()    # Output: Flying
donald.swim()   # Output: Swimming
donald.quack()  # Output: Quack!
donald.do_something()  # Output: Doing something in Flyer (the first parent class in MRO)
#Method Resolution Order
print(Duck.mro())# [<class '__main__.Duck'>, <class '__main__.Flyer'>, <class '__main__.Swimmer'>, <class 'object'>]
print(Duck.__mro__)# (<class '__main__.Duck'>, <class '__main__.Flyer'>, <class '__main__.Swimmer'>, <class 'object'>)