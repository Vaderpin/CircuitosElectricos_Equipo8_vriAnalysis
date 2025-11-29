class Resistencia:

    def __init__(self, nombre:str, nodo1:int, nodo2:int, valor:float):

        if not (
                isinstance(nombre, str) and 
                isinstance(nodo1, int) and 
                isinstance(nodo2, int) and 
                isinstance(valor, (int, float))
            ):
            raise TypeError("Serie inválida para Resistencia ", nombre, ": (", nodo1, " - ", valor, " ohmios - ", nodo2, ")")

        self.nombre = nombre
        self.nodo1  = nodo1
        self.nodo2  = nodo2
        self.valor  = float(valor)

    def myPrint(self):
        print("Resistencia ", self.nombre, ": (", self.nodo1, " - ", self.valor, " ohmios - ", self.nodo2, ")")

class ftVoltaje:
    
    def __init__(self, nombre:str, nodo1:int, nodo2:int, valor:float):

        if not (
                isinstance(nombre, str) and 
                isinstance(nodo1, int) and 
                isinstance(nodo2, int) and 
                isinstance(valor, (int, float))
            ):
            raise TypeError("Serie inválida para Voltaje ", nombre, ": (", nodo1, " - ", valor, " voltios - ", nodo2, ")")

        self.nombre = nombre
        self.nodo1  = nodo1
        self.nodo2  = nodo2
        self.valor  = float(valor)
    
    def myPrint(self):
        print("Voltaje     ", self.nombre, ": (", self.nodo1, " - ", self.valor, " voltios - ", self.nodo2, ")")

class ftCorriente:
    
    def __init__(self, nombre:str, nodo1:int, nodo2:int, valor:float):
        
        if not (
                isinstance(nombre, str) and 
                isinstance(nodo1, int) and 
                isinstance(nodo2, int) and 
                isinstance(valor, (int, float))
            ):
            raise TypeError("Serie inválida para Corriente ", nombre, ": (", nodo1, " - ", valor, " amperios - ", nodo2, ")")

        self.nombre = nombre
        self.nodo1  = nodo1
        self.nodo2  = nodo2
        self.valor  = float(valor)

    def myPrint(self):
        print("Corriente   ", self.nombre, ": (", self.nodo1, " - ", self.valor, " amperios - ", self.nodo2, ")")