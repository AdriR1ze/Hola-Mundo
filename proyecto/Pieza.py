from typing import TypeVar, List
from enum import Enum



class TipoPieza(Enum):
    ALFIL = 1
    TORRE = 2
    CABALLO = 3
    PEON = 4
    REY = 5
    REINA = 6


class TipoBando(Enum):
    BLANCO = 1
    NEGRO = 2


class Pieza:

    def __init__(self, tipo: TipoPieza, vivo: bool, posicion: tuple[int, int], bando: TipoBando):
        self.movio=False
        self.tipo = tipo
        self.posicion = posicion
        self.bando = bando

   # def __str__(self):
   #     return self.bando +" "+ self.tipo +" "+self.posicion



