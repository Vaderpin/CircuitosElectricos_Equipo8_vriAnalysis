"""
    En este código se tratará la entrada de datos desde el archivo,
    así como el "main" del programa
"""

import os
import componentes as c

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Diccionario de prefijos: tabla hash
PREFIJOS = {
    'M': 1000000,   
    'k': 1000,      
    'm': 1/1000,    
    'u': 1/1000000,
    'μ': 1/1000000
}

#para convertir mili/kilo/... ohms/voltios/amperes a ohms/voltios/amperes
def convertirUnidades (num:str):
    prefijo=num[len(num)-1]
    if prefijo in PREFIJOS:
        numero=float(num[0:len(num) - 1])
        return numero*PREFIJOS[prefijo]
    else:
        numero=float(num)
        return numero

#convierte el archivo a un arreglo polimórfico manejable por python
def cargarArchivo(archivo):
    componentes=[]
    with open(archivo, "r") as circuito:
        for line in circuito:
            line = line.strip() #elimina \n, \t y espacios al principio y al final
            if not line or line.startswith(("#","/","\\")): #ignora comentarios y saltos en blanco
                continue
            info=line.split() #especificar en el argumento si se usara un separador diferente
            info[2]=int(info[2])
            info[3]=int(info[3])
            info[4]=convertirUnidades(info[4])
            match info[0]:
                case "V": elemento=c.ftVoltaje(*info[1:5])
                case "R": elemento=c.Resistencia(*info[1:5])
                case "I": elemento=c.ftCorriente(*info[1:5])
                case _: raise TypeError("tipo inválido ", info[0], ", existentes: V, R, I")
            componentes.append(elemento)
    return componentes

def imprimirComponentes(componentes):
    for componente in componentes:
        componente.myPrint()

if __name__ == "__main__" :
    while (True):
        clear() # Mostrar: inicio
        print("")
        print("██  ██  █████▄   ████")
        print("██▄▄██  ██▄▄██▄   ██ ")             
        print(" ▀██▀   ██   ██  ████")
        print("┏━┓┏┓╻┏━┓╻  ╻ ╻┏━┓╻┏━┓")
        print("┣━┫┃┗┫┣━┫┃  ┗┳┛┗━┓┃┗━┓")
        print("╹ ╹╹ ╹╹ ╹┗━╸ ╹ ┗━┛╹┗━┛")
        print("")
        archivo=input(">   Nombre del archivo (escriba \"salir\" para cerrar el programa): ")
        if (archivo=="salir"): break

        try:
            circuito=cargarArchivo(archivo)
            banner=1
        except Exception as e:
            clear() # Mostrar: error
            print("Ocurrió un error, revise el archivo, introduzca enter para continuar o ! si requiere ver más info")
            opc=input()
            if (opc=='!'): 
                print(e)
                ok=input()
            continue

        clear() # Mostrar: circuito
        imprimirComponentes(circuito)
        
        ok=input()
        
    clear() # Mostrar: despedida
    print("Gracias por usar el programa\n")