from Pieza import Pieza, TipoPieza,TipoBando
from typing import List
class Tablero():
    def __init__(self):
        self.piezas = []
        self.piezas.append(Pieza(TipoPieza.ALFIL, True, (3, 1), TipoBando.BLANCO))
        self.piezas.append(Pieza(TipoPieza.ALFIL, True, (6, 1), TipoBando.BLANCO))
        self.piezas.append(Pieza(TipoPieza.TORRE, True, (1, 1), TipoBando.BLANCO))
        self.piezas.append(Pieza(TipoPieza.TORRE, True, (8, 1), TipoBando.BLANCO))
        self.piezas.append(Pieza(TipoPieza.CABALLO, True, (2, 1), TipoBando.BLANCO))
        self.piezas.append(Pieza(TipoPieza.CABALLO, True, (7, 1), TipoBando.BLANCO))
        self.piezas.append(Pieza(TipoPieza.PEON, True, (1, 2), TipoBando.BLANCO))
        self.piezas.append(Pieza(TipoPieza.PEON, True, (2, 2), TipoBando.BLANCO))
        self.piezas.append(Pieza(TipoPieza.PEON, True, (3, 2), TipoBando.BLANCO))
        self.piezas.append(Pieza(TipoPieza.PEON, True, (4, 2), TipoBando.BLANCO))
        self.piezas.append(Pieza(TipoPieza.PEON, True, (5, 2), TipoBando.BLANCO))
        self.piezas.append(Pieza(TipoPieza.PEON, True, (6, 2), TipoBando.BLANCO))
        self.piezas.append(Pieza(TipoPieza.PEON, True, (7, 2), TipoBando.BLANCO))
        self.piezas.append(Pieza(TipoPieza.PEON, True, (8, 2), TipoBando.BLANCO))
        self.piezas.append(Pieza(TipoPieza.REINA,True,(4,1),TipoBando.BLANCO))
        self.piezas.append(Pieza(TipoPieza.REY, True, (5, 1), TipoBando.BLANCO))

        self.piezas.append(Pieza(TipoPieza.ALFIL, True, (3, 8), TipoBando.NEGRO))
        self.piezas.append( Pieza(TipoPieza.ALFIL, True, (6, 8), TipoBando.NEGRO))
        self.piezas.append(Pieza(TipoPieza.TORRE, True, (1, 8), TipoBando.NEGRO))
        self.piezas.append(Pieza(TipoPieza.TORRE, True, (8, 8), TipoBando.NEGRO))
        self.piezas.append(Pieza(TipoPieza.CABALLO, True, (2, 8), TipoBando.NEGRO))
        self.piezas.append(Pieza(TipoPieza.CABALLO, True, (7, 8), TipoBando.NEGRO))
        self.piezas.append(Pieza(TipoPieza.PEON, True, (1, 7), TipoBando.NEGRO))
        self.piezas.append(Pieza(TipoPieza.PEON, True, (2, 7), TipoBando.NEGRO))
        self.piezas.append(Pieza(TipoPieza.PEON, True, (3, 7), TipoBando.NEGRO))
        self.piezas.append(Pieza(TipoPieza.PEON, True, (4, 7), TipoBando.NEGRO))
        self.piezas.append(Pieza(TipoPieza.PEON, True, (5, 7), TipoBando.NEGRO))
        self.piezas.append( Pieza(TipoPieza.PEON, True, (6, 7), TipoBando.NEGRO))
        self.piezas.append( Pieza(TipoPieza.PEON, True, (7, 7), TipoBando.NEGRO))
        self.piezas.append( Pieza(TipoPieza.PEON, True, (8, 7), TipoBando.NEGRO))
        self.piezas.append(Pieza(TipoPieza.REINA,True,(4,8),TipoBando.NEGRO))
        self.piezas.append(Pieza(TipoPieza.REY, True, (5, 8), TipoBando.NEGRO))

    def encontrar_pieza(self, posicion):
        for b in self.piezas:
            if b.posicion==posicion:
                return b



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

#for a in Pieza.conjunto_piezas:

#print(Tablero.casillas_totales())