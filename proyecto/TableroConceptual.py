from Pieza import Pieza, TipoPieza,TipoBando
from typing import List
class Tablero():
    def __init__(self):

        self.piezas = []
        Alfil = Pieza(TipoPieza.ALFIL, True, (2, 3), TipoBando.BLANCO)
        Torre = Pieza(TipoPieza.TORRE, True, (4, 5), TipoBando.BLANCO)
        Caballo = Pieza(TipoPieza.CABALLO, True, (8, 8), TipoBando.BLANCO)
        Peon = Pieza(TipoPieza.PEON, True, (1, 1), TipoBando.BLANCO)
        self.piezas.append(Alfil)
        self.piezas.append(Torre)
        self.piezas.append(Caballo)
        self.piezas.append(Peon)

    def casillas_totales(self):
        lista_de_casillas = []
        for a in range(8):
            a = a + 1
            for b in range(8):
                b = b + 1
                lista_de_casillas.append((a, b))

        return lista_de_casillas
    def casillas_ocupadas(self):
        pass

    def casillas_restantes(self):
        pass
tablero=Tablero()
print(tablero.casillas_restantes())
#for a in Pieza.conjunto_piezas:

#print(Tablero.casillas_totales())