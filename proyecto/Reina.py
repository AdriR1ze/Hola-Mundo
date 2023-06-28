import Posicion
class Reina:
    def __init__(self, vivo: int, posicion, color):
        self.vivo = vivo
        self.posicion = posicion
        self.color = color
Reina1 = Reina(1, Posicion.Casilla("D1"), "blanco")
ReinaNegra = Reina(1, Posicion.Casilla("D8"), "negro")