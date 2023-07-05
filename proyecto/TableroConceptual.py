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

        self.piezas.append(Pieza(TipoPieza.ALFIL, True, (6, 5), TipoBando.NEGRO))
        self.piezas.append( Pieza(TipoPieza.ALFIL, True, (6, 8), TipoBando.NEGRO))
        self.piezas.append(Pieza(TipoPieza.TORRE, True, (3, 5), TipoBando.NEGRO))
        self.piezas.append(Pieza(TipoPieza.TORRE, True, (5, 5), TipoBando.NEGRO))
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

    def encontrar_pieza(self, posicion: tuple[int,int]):
        for b in self.piezas:
            if b.posicion==posicion:
                return b

    def posibles_movimientos_bien_torre(self,pieza: Pieza):
        lista_por_ahora=self.posibles_movimientos_de_torre(pieza)

        for a in self.piezas:
                if a.posicion in lista_por_ahora:


                    lista_por_ahora.remove(a.posicion)
        return lista_por_ahora

    def posibles_movimientos(self,pieza: Pieza):
        if TipoPieza.ALFIL == pieza.tipo:
            return self.posibles_movimientos_de_alfil(pieza)
        if TipoPieza.CABALLO == pieza.tipo:
            return self.posibles_movimientos_de_caballo(pieza)
        if TipoPieza.TORRE == pieza.tipo:
            return self.posibles_movimientos_bien_torre(pieza)
        if TipoPieza.PEON == pieza.tipo:
            return self.posibles_movimientos_bien_peon(pieza)
        if TipoPieza.REINA==pieza.tipo:
            return self.posibles_movimientos_de_reina(pieza)
        if TipoPieza.REY==pieza.tipo:
            return self.posibles_movimientos_de_rey(pieza)

    def posibles_movimientos_de_alfil(self,pieza) -> List[tuple[int, int]]:
        lista_de_movimientos = []
        for columna in range(8):
            columna = columna + 1
            for fila in range(8):
                fila = fila + 1
                if abs((columna - pieza.posicion[0])) == abs((fila - pieza.posicion[1])) and (
                        columna, fila) != pieza.posicion and self.encontrar_pieza((columna,fila))==None:
                    lista_de_movimientos.append((columna, fila))
        return lista_de_movimientos

    def posibles_movimientos_de_caballo(self,pieza) -> List[tuple[int, int]]:
        lista_de_movimientos = []
        if self.encontrar_pieza(((pieza.posicion[0] - 2, pieza.posicion[1] - 1)))==None:
            lista_de_movimientos.append((pieza.posicion[0] - 2, pieza.posicion[1] - 1))
        if self.encontrar_pieza(((pieza.posicion[0] - 2, pieza.posicion[1] + 1))) == None:
            lista_de_movimientos.append((pieza.posicion[0] - 2, pieza.posicion[1] + 1))
        if self.encontrar_pieza(((pieza.posicion[0] + 2), (pieza.posicion[1] - 1))) == None:
            lista_de_movimientos.append(((pieza.posicion[0] + 2), (pieza.posicion[1] - 1)))
        if self.encontrar_pieza(((pieza.posicion[0] + 2), (pieza.posicion[1] + 1))) == None:
            lista_de_movimientos.append(((pieza.posicion[0] + 2), (pieza.posicion[1] + 1)))
        if self.encontrar_pieza(((pieza.posicion[0] + 1), (pieza.posicion[1] + 2))) == None:
            lista_de_movimientos.append(((pieza.posicion[0] + 1), (pieza.posicion[1] + 2)))
        if self.encontrar_pieza(((pieza.posicion[0] - 1), (pieza.posicion[1] + 2))) == None:
            lista_de_movimientos.append(((pieza.posicion[0] - 1), (pieza.posicion[1] + 2)))
        if self.encontrar_pieza(((pieza.posicion[0] + 1), (pieza.posicion[1] - 2))) == None:
            lista_de_movimientos.append(((pieza.posicion[0] + 1), (pieza.posicion[1] - 2)))
        if self.encontrar_pieza(((pieza.posicion[0] - 1), (pieza.posicion[1] - 2))) == None:
            lista_de_movimientos.append(((pieza.posicion[0] - 1), (pieza.posicion[1] - 2)))
            lista_de_movimientos = list(
                filter(lambda a: a[0] > 0 and a[1] > 0 and a[0] <= 8 and a[1] <= 8, lista_de_movimientos))
        return lista_de_movimientos

    def posibles_movimientos_de_torre(self,pieza):
        lista_de_movimientos = []
        filas_para_arriba = pieza.posicion[1]
        filas_para_abajo = pieza.posicion[1]
        columnas_para_adelante = pieza.posicion[0]
        columnas_para_atras = pieza.posicion[0]
        hay_pieza_delante1 = False
        hay_pieza_delante2 = False
        hay_pieza_delante3 = False
        hay_pieza_delante4 = False
        for a in range(15):
            columnas_para_adelante = columnas_para_adelante + 1
            columnas_para_atras = columnas_para_atras - 1
            filas_para_arriba = filas_para_arriba + 1
            filas_para_abajo = filas_para_abajo - 1

            if self.encontrar_pieza((columnas_para_adelante,pieza.posicion[1]))==None:
                if columnas_para_adelante < 9 and hay_pieza_delante1==False:
                    lista_de_movimientos.append((columnas_para_adelante, pieza.posicion[1]))
            else:
                hay_pieza_delante1=True
            if self.encontrar_pieza((columnas_para_atras, pieza.posicion[1])) == None:
                if columnas_para_atras > 0 and hay_pieza_delante2==False:
                    lista_de_movimientos.append((columnas_para_atras, pieza.posicion[1]))
            else:
                hay_pieza_delante2=True
            if self.encontrar_pieza((filas_para_abajo, pieza.posicion[0])) == None:
                if filas_para_abajo > 0 and hay_pieza_delante3==False:
                    lista_de_movimientos.append((pieza.posicion[0], filas_para_abajo))
            else:
                hay_pieza_delante3=True
            if self.encontrar_pieza((filas_para_arriba, pieza.posicion[0])) == None:
                if filas_para_arriba < 9 and hay_pieza_delante4==False:
                    lista_de_movimientos.append((pieza.posicion[0], filas_para_arriba))
            else:
                hay_pieza_delante4=True
        return lista_de_movimientos

    def posibles_movimientos_de_peon(self, pieza):
        lista_de_movimientos = []
        lista_de_movimientos.append((pieza.posicion[0], pieza.posicion[1] + 1))
        if pieza.bando == TipoBando.BLANCO and pieza.posicion[1] == 2:
            lista_de_movimientos.append((pieza.posicion[0], pieza.posicion[1] + 2))
            # print("test")
        return lista_de_movimientos

    def posibles_movimientos_bien_peon(self, pieza):
        lista_por_ahora = self.posibles_movimientos_de_peon(pieza)
        for a in self.piezas:
            if a.posicion in lista_por_ahora:
                lista_por_ahora.remove(a.posicion)
            else:
                pass
        return lista_por_ahora
    def posibles_movimientos_de_reina(self,pieza):
        lista_de_movimientos = []
        filas_para_arriba = pieza.posicion[1]
        filas_para_abajo = pieza.posicion[1]
        columnas_para_adelante = pieza.posicion[0]
        columnas_para_atras = pieza.posicion[0]
        hay_pieza_delante1 = False
        hay_pieza_delante2 = False
        hay_pieza_delante3 = False
        hay_pieza_delante4 = False
        for a in range(15):
            columnas_para_adelante = columnas_para_adelante + 1
            columnas_para_atras = columnas_para_atras - 1
            filas_para_arriba = filas_para_arriba + 1
            filas_para_abajo = filas_para_abajo - 1

            if self.encontrar_pieza((columnas_para_adelante, pieza.posicion[1])) == None:
                if columnas_para_adelante < 9 and hay_pieza_delante1 == False:
                    lista_de_movimientos.append((columnas_para_adelante, pieza.posicion[1]))
            else:
                hay_pieza_delante1 = True
            if self.encontrar_pieza((columnas_para_atras, pieza.posicion[1])) == None:
                if columnas_para_atras > 0 and hay_pieza_delante2 == False:
                    lista_de_movimientos.append((columnas_para_atras, pieza.posicion[1]))
            else:
                hay_pieza_delante2 = True
            if self.encontrar_pieza((filas_para_abajo, pieza.posicion[0])) == None:
                if filas_para_abajo > 0 and hay_pieza_delante3 == False:
                    lista_de_movimientos.append((pieza.posicion[0], filas_para_abajo))
            else:
                hay_pieza_delante3 = True
            if self.encontrar_pieza((filas_para_arriba, pieza.posicion[0])) == None:
                if filas_para_arriba < 9 and hay_pieza_delante4 == False:
                    lista_de_movimientos.append((pieza.posicion[0], filas_para_arriba))
            else:
                hay_pieza_delante4 = True
        for columna in range(8):
            columna = columna + 1
            for fila in range(8):
                fila = fila + 1
                if abs((columna - pieza.posicion[0])) == abs((fila - pieza.posicion[1])) and (
                        columna, fila) != pieza.posicion and self.encontrar_pieza((columna, fila)) == None:
                    lista_de_movimientos.append((columna, fila))
        return lista_de_movimientos
    def posibles_movimientos_de_rey(self,pieza):
        lista_de_movimientos=[]

        lista_de_movimientos.append((pieza.posicion[0]+1,pieza.posicion[1]))
        lista_de_movimientos.append((pieza.posicion[0]+1, pieza.posicion[1]+1))
        lista_de_movimientos.append((pieza.posicion[0]+1, pieza.posicion[1]-1))
        lista_de_movimientos.append((pieza.posicion[0]-1, pieza.posicion[1]))
        lista_de_movimientos.append((pieza.posicion[0]-1, pieza.posicion[1]+1))
        lista_de_movimientos.append((pieza.posicion[0]-1, pieza.posicion[1]-1))
        lista_de_movimientos.append((pieza.posicion[0], pieza.posicion[1]+1))
        lista_de_movimientos.append((pieza.posicion[0], pieza.posicion[1]-1))
        lista_de_movimientos = list(
            filter(lambda a: a[0] > 0 and a[1] > 0 and a[0] <= 8 and a[1] <= 8, lista_de_movimientos))
        return lista_de_movimientos


