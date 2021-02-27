class Calculadora():
    def __init__(self):
        self.__valor1__ = 0
        self.__valor2__ = 0
        self.__resultado__ = 0

    def set_valor1(self, val):
        self.__valor1__ = val

    def set_valor2(self, val):
        self.__valor2__ = val
    
    def get_resultado(self):
        return self.__resultado__

    def sumar(self):
        self.__resultado__ = self.__valor1__ + self.__valor2__

c = Calculadora()
c.set_valor1(5)
c.set_valor2(3)
c.sumar()
print(c.get_resultado())
