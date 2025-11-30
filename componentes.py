class Componente:
    TIPO = "???"
    UNIDAD = "unidades"

    def __init__(self, nombre, nodo1, nodo2, valor: float):
        if not isinstance(valor, (int, float)):
            raise TypeError(
                f"Magnitud inválida para {self.TIPO} {nombre}: "
                f"({nodo1} - {valor} {self.UNIDAD} - {nodo2})"
            )

        self.nombre = nombre
        self.nodo1 = nodo1
        self.nodo2 = nodo2
        self.valor = float(valor)

        try:
            self.nodo1=float(self.nodo1)
            self.nodo2=float(self.nodo2)
        except Exception:
            pass

    def myPrint(self):
        print(
            f"{self.TIPO:<12} {self.nombre}: "
            f"({self.nodo1} - {self.valor} {self.UNIDAD} - {self.nodo2})"
        )


class Resistencia(Componente):
    TIPO = "Resistencia"
    UNIDAD = "ohmios"

    def __init__(self, *args):
        super().__init__(*args)
        self.r=self.valor
        self.i=0
        self.v=0

class ftVoltaje(Componente):
    TIPO = "Voltaje"
    UNIDAD = "voltios"

    def __init__(self, *args):
        super().__init__(*args)
        self.i=0
        self.v=self.valor


class ftCorriente(Componente):
    TIPO = "Corriente"
    UNIDAD = "amperios"

    def __init__(self, *args):
        self.i=0
