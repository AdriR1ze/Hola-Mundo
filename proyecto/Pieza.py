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
        self.tipo = tipo
        self.vivo = vivo
        self.posicion = posicion
        self.bando = bando

    def posibles_movimientos_de_alfil(self) -> List[tuple[int, int]]:
        lista_de_movimientos = []
        for columna in range(8):
            columna = columna + 1
            for fila in range(8):
                fila = fila + 1
                if abs((columna - self.posicion[0])) == abs((fila - self.posicion[1])) and (
                        columna, fila) != self.posicion:
                    lista_de_movimientos.append((columna, fila))
        return lista_de_movimientos

    def posibles_movimientos_de_caballo(self) -> List[tuple[int, int]]:
        lista_de_movimientos = []
        lista_de_movimientos.append((self.posicion[0] - 2, self.posicion[1] - 1))
        lista_de_movimientos.append((self.posicion[0] - 2, self.posicion[1] + 1))
        lista_de_movimientos.append(((self.posicion[0] + 2), (self.posicion[1] - 1)))
        lista_de_movimientos.append(((self.posicion[0] + 2), (self.posicion[1] + 1)))
        lista_de_movimientos.append(((self.posicion[0] + 1), (self.posicion[1] + 2)))
        lista_de_movimientos.append(((self.posicion[0] - 1), (self.posicion[1] + 2)))
        lista_de_movimientos.append(((self.posicion[0] + 1), (self.posicion[1] - 2)))
        lista_de_movimientos.append(((self.posicion[0] - 1), (self.posicion[1] - 2)))
        lista_de_movimientos = list(
            filter(lambda a: a[0] > 0 and a[1] > 0 and a[0] <= 8 and a[1] <= 8, lista_de_movimientos))
        return lista_de_movimientos

    def posibles_movimientos_de_torre(self):
        lista_de_movimientos = []
        filas_para_arriba = self.posicion[1]
        filas_para_abajo = self.posicion[1]
        columnas_para_adelante = self.posicion[0]
        columnas_para_atras = self.posicion[0]
        for a in range(15):
            columnas_para_adelante = columnas_para_adelante + 1
            columnas_para_atras = columnas_para_atras - 1
            filas_para_arriba = filas_para_arriba + 1
            filas_para_abajo = filas_para_abajo - 1
            if columnas_para_adelante < 9:
                lista_de_movimientos.append((columnas_para_adelante, self.posicion[1]))
            if columnas_para_atras > 0:
                lista_de_movimientos.append((columnas_para_atras, self.posicion[1]))
            if filas_para_abajo > 0:
                lista_de_movimientos.append((self.posicion[0], filas_para_abajo))
            if filas_para_arriba < 9:
                lista_de_movimientos.append((self.posicion[0], filas_para_arriba))
        return lista_de_movimientos

    def posibles_movimientos_de_peon(self):
        lista_de_movimientos = []
        lista_de_movimientos.append((self.posicion[1] + 1, self.posicion[0]))
        return lista_de_movimientos

    def posibles_movimientos(self):
        if TipoPieza.ALFIL == self.tipo:
            return self.posibles_movimientos_de_alfil()
        if TipoPieza.CABALLO == self.tipo:
            return self.posibles_movimientos_de_caballo()
        if TipoPieza.TORRE == self.tipo:
            return self.posibles_movimientos_de_torre()
        if TipoPieza.PEON == self.tipo:
            return self.posibles_movimientos_de_peon()





