from abc import ABC, abstractmethod
from random import randint

class Instrumento(ABC):

    @abstractmethod
    def afinar(self):
        pass
    
    @abstractmethod
    def tocar(self, nota=None):
        pass

class Guitarra(Instrumento):
    
    def afinar(self):
        a = Afinador()
        a.generar_tono()
        print("afinando guitarra")      

    def tocar(self, nota=None):
        if nota == None:
            print("tocando guitarra")
        else:
            print("tocando guitarra en " + nota)

class Viola(Instrumento):
    
    def afinar(self):
        print("afinando viola")

    def tocar(self, nota=None):
        if nota == None:
            print("tocando viola")
        else:
            print("tocando viola en " + nota)

class Afinador():
    def generar_tono(self):
        print("generando tono para afinar")


class Banda():
    def __init__(self):
        self.instrumentos = []
        for i in range(3):
            self.instrumentos.append(self.generar_instrumento())

    def generar_instrumento(self):
        if randint(0, 10) % 2 == 0:
            i = Guitarra()
        else:
            i = Viola()
        return i

    def presentar(self):
        for i in self.instrumentos:
            i.afinar()
            i.tocar()

b = Banda()
b.presentar()
