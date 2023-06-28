import Posicion
class Caballo:
    def __init__(self, vivo: int, posicion, color):
        self.vivo = vivo
        self.posicion = posicion
        self.color = color
Caballo1=Caballo(1,Posicion.Casilla("B1"),"blanco")
Caballo2=Caballo(1,Posicion.Casilla("G1"),"blanco")
CaballoNegro=Caballo(1,Posicion.Casilla("B8"),"negro")
CaballoNegro2=Caballo(1,Posicion.Casilla("G8"),"negro")