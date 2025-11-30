"""
    Se define la clase matrizMNA:
        - lista de nodos, donde tierra es el ultimo nodo
        - listas de componentes por tipo
"""

import componentes as c

class matrizMNA:

    def __init__(self, componentes:list):

    # Obtener lista de nodos
        
        self.nodos=set() #conjunto -> lista (ordeada o no) de nodos
        for componente in componentes:
            self.nodos.add(componente.nodo1)
            self.nodos.add(componente.nodo2)

            # De paso obtener listas de componentes por tipo
            if componente is c.ftVoltaje:
                self.voltajes.append(componente)
            if componente is c.ftCorriente:
                self.corrientes.append(componente)
            if componente is c.Resistencia:
                self.resistencias.append(componente)

        try:
            self.nodos=sorted(list(self.nodos))
        except Exception:
            self.nodos=list(self.nodos)

        for nodo in self.nodos: #crear matriz
            pass