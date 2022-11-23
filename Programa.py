from Punto import Punto

class Programa:

    def __init__(self):
        pass

messi=Punto()
elBicho=Punto()
iniesta=Punto()

messi.x=8
messi.y=2
elBicho.x=9
elBicho.y=9
iniesta.x=15
iniesta.y=30

a=messi.calcular_distancia(elBicho,iniesta)
print(a)