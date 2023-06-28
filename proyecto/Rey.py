import Posicion
class Rey:
    def __init__(self, vivo: int, posicion, color):
        self.vivo = vivo
        self.posicion = posicion
        self.color = color
Rey1=Rey(1,Posicion.Casilla("E1"),"blanco")
ReyNegro=Rey(1,Posicion.Casilla("E8"),"negro")