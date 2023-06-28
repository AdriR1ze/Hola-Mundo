import Posicion
class Torre:
    def __init__(self, vivo: int, posicion, color):
        self.vivo = vivo
        self.posicion = posicion
        self.color = color
Torre1=Torre(1,Posicion.Casilla("A1"),"blanco")
Torre2=Torre(1,Posicion.Casilla("H1"),"blanco")
TorreNegra=Torre(1,Posicion.Casilla("A8"),"negro")
TorreNegra2=Torre(1,Posicion.Casilla("H8"),"negro")