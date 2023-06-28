import Posicion
class Peon:
    def __init__(self, vivo: int, posicion, color):
        self.vivo = vivo
        self.posicion = posicion
        self.color = color
Peon1=Peon(1,Posicion.Casilla("A2"),"blanco")
Peon2=Peon(1,Posicion.Casilla("B2"),"blanco")
Peon3=Peon(1,Posicion.Casilla("C2"),"blanco")
Peon4=Peon(1,Posicion.Casilla("D2"),"blanco")
Peon5=Peon(1,Posicion.Casilla("E2"),"blanco")
Peon6=Peon(1,Posicion.Casilla("F2"),"blanco")
Peon7=Peon(1,Posicion.Casilla("G2"),"blanco")
Peon8=Peon(1,Posicion.Casilla("H2"),"blanco")
PeonNegro1=Peon(1,Posicion.Casilla("A7"),"negro")
PeonNegro2=Peon(1,Posicion.Casilla("B7"),"negro")
PeonNegro3=Peon(1,Posicion.Casilla("C7"),"negro")
PeonNegro4=Peon(1,Posicion.Casilla("D7"),"negro")
PeonNegro5=Peon(1,Posicion.Casilla("E7"),"negro")
PeonNegro6=Peon(1,Posicion.Casilla("F7"),"negro")
PeonNegro7=Peon(1,Posicion.Casilla("G7"),"negro")
PeonNegro8=Peon(1,Posicion.Casilla("H7"),"negro")
PeonesBlancos=[Peon1,Peon2,Peon3,Peon4,Peon5,Peon6,Peon7,Peon8]
print(Peon1.posicion)