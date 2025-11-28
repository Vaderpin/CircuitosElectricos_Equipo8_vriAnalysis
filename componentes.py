class Resistencia:

    def __init__(self, nombre:str, nodo1:int, nodo2:int, valor:float):
        self.nombre = nombre
        self.nodo1  = nodo1
        self.nodo2  = nodo2
        self.valor  = valor 

    def myPrint(self):
        print("Resistencia ", self.nombre, ": (", self.nodo1, " - ", self.valor, " ohmios - ", self.nodo2, ")")

class ftVoltaje:
    
    def __init__(self, nombre:str, nodo1:int, nodo2:int, valor:float):
        self.nombre = nombre
        self.nodo1  = nodo1
        self.nodo2  = nodo2
        self.valor  = valor
    
    def myPrint(self):
        print("Voltaje     ", self.nombre, ": (", self.nodo1, " - ", self.valor, " voltios - ", self.nodo2, ")")

class ftCorriente:
    
    def __init__(self, nombre:str, nodo1:int, nodo2:int, valor:float):
        self.nombre = nombre
        self.nodo1  = nodo1
        self.nodo2  = nodo2
        self.valor  = valor

    def myPrint(self):
        print("Corriente   ", self.nombre, ": (", self.nodo1, " - ", self.valor, " amperios - ", self.nodo2, ")")