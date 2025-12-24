#Nos interesa el "qué hace" y no el "cómo lo hace"
class CoffeMaker:
    def __boil_water(self): #método privado
        pass
    def __mix(self): #método privado
        pass
    def make_coffe(self): #método público
        self.__boil_water()
        self.__mix()
        print("Coffe is ready")

coffe_maker = CoffeMaker()
coffe_maker.make_coffe() #Solo nos interesa que prepare el café, no los detalles de cómo lo hace