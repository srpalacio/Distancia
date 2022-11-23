import math

class Punto:
    
    def __init__(self):
        self.x=0
        self.y=0

    def calcular_distancia(self,otroPunto,tercerPunto):

        r=math.sqrt(math.pow((self.x-otroPunto.x-tercerPunto.x),2)+math.pow((self.y-otroPunto.y-tercerPunto.y),2))
        return r