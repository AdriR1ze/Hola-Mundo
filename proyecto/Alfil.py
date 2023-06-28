import Posicion
class Alfil:
    def __init__(self, vivo: int, posicion, color, color_de_suelo):
        self.vivo = vivo
        self.posicion = posicion
        self.color = color
Alfil1=Alfil(1,Posicion.Casilla("C1"),"blanco","NEGRO")
Alfil2=Alfil(1,Posicion.Casilla("F1"),"blanco","BLANCO")
AlfilNegro=Alfil(1,Posicion.Casilla("C8"),"negro","BLANCO")
AlfilNegro1=Alfil(1,Posicion.Casilla("F8"),"negro","NEGRO")