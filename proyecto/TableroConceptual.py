from Pieza import Pieza, TipoPieza,TipoBando
from typing import List
import inspect

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
    def remover_pieza(self,pieza):
        self.piezas.remove(pieza)


    def puedo_comer(self,pieza, pos):
        return self.encontrar_pieza(pos)!=None and self.encontrar_pieza(pos).bando!=pieza.bando

    def encontrar_rey(self, color: TipoBando):
        for b in self.piezas:
            if b.tipo==TipoPieza.REY and b.bando==color:
                return b

    def encontrar_pieza(self, posicion: tuple[int,int]):
        for b in self.piezas:
            if b.posicion==posicion:
                return b
    def posibles_movimientos_bien_torre(self,pieza: Pieza):
        lista_por_ahora=self.posibles_movimientos_de_torre(pieza)

        for a in self.piezas:
                if a.posicion in lista_por_ahora and a.bando==pieza.bando:
                #aca esta el error de comer de la torre

                    self.remove(lista_por_ahora, a.posicion)
        return lista_por_ahora

    def posibles_movimientos_bien(self, pieza: Pieza, turno):
        lista_de_movimientos=self.posibles_movimientos(pieza, turno)
        print("+posibles_movimientos_bien ", lista_de_movimientos)
        posicion_momentanea=pieza.posicion
        rs=[]
        for a in lista_de_movimientos:
            la_que_hace = self.encontrar_pieza(a)
            if la_que_hace != None:
                self.remover_pieza(la_que_hace)
                pieza.posicion = a
                if self.tiene_jaque(turno) == False:
                    rs.append(a)
                self.piezas.append(la_que_hace)
                pieza.posicion=posicion_momentanea
            else:
                pieza.posicion = a
                if self.tiene_jaque(turno) == False:
                    rs.append(a)
                pieza.posicion=posicion_momentanea

        print("-posibles_movimientos_bien ", rs)
        return rs

    def posibles_movimientos(self,pieza: Pieza, turno: TipoBando, sin_rey = False,evitar_jaque=False):
        lista_de_movimientos=[]
        if TipoPieza.ALFIL == pieza.tipo:
            lista_de_movimientos=self.posibles_movimientos_bien_alfil(pieza)
        if TipoPieza.CABALLO == pieza.tipo:
            lista_de_movimientos=self.posibles_movimientos_de_caballo(pieza)
        if sin_rey == False and TipoPieza.TORRE == pieza.tipo:
            lista_de_movimientos=self.posibles_movimientos_bien_torre(pieza)
        if TipoPieza.PEON == pieza.tipo:
            lista_de_movimientos=self.posibles_movimientos_bien_peon(pieza,turno,evitar_jaque)
        if TipoPieza.REINA==pieza.tipo:
            lista_de_movimientos=self.posibles_movimientos_de_reina(pieza)
        if sin_rey == False and TipoPieza.REY==pieza.tipo:
            lista_de_movimientos=self.posibles_movimientos_rey_bien(pieza,turno)

        return lista_de_movimientos
    def posibles_movimientos_bien_alfil(self,pieza):
        lista_por_ahora=self.posibles_movimientos_de_alfil(pieza)
        for a in self.piezas:
                if a.posicion in lista_por_ahora and a.bando==pieza.bando:
                        #aca esta el error de comer de la torre
                    self.remove(lista_por_ahora,a.posicion)
        return lista_por_ahora

    def movimiento_diagonal(self,pieza,diagonal,tipo):
        lista_de_movimientos = []
        try:
            primera_vez1 = False
            hay_pieza_delante1 = False
            for a in range(7):
                if tipo == 1:
                    diagonal = (diagonal[0] - 1, diagonal[1] + 1)
                if tipo == 2:
                    diagonal = (diagonal[0] - 1, diagonal[1] - 1)

                if tipo == 3:
                    diagonal = (diagonal[0] + 1, diagonal[1] + 1)
                if tipo==4:
                    diagonal = (diagonal[0] + 1, diagonal[1] - 1)
                if diagonal[0] >= 1 and diagonal[1] < 9 and diagonal[0] <9 and diagonal[1] >=1:
                    if self.encontrar_pieza(diagonal) == None:
                        if hay_pieza_delante1 == False:
                            lista_de_movimientos.append(diagonal)
                    else:
                        hay_pieza_delante1 = True
                        if self.encontrar_pieza(diagonal).bando != pieza.bando and primera_vez1 == False:
                            lista_de_movimientos.append(diagonal)
                            primera_vez1 = True
                        if self.encontrar_pieza(diagonal).bando==pieza.bando:
                            primera_vez1=True
        except:
            print("Error en diagnoal")

        return lista_de_movimientos

    def posibles_movimientos_de_alfil(self,pieza) -> List[tuple[int, int]]:

        diagonal1=(pieza.posicion[0],pieza.posicion[1])
        diagonal2=(pieza.posicion[0],pieza.posicion[1])
        diagonal3=(pieza.posicion[0],pieza.posicion[1])
        diagonal4=(pieza.posicion[0],pieza.posicion[1])
        lista_de_movimientos = []


        lista_de_movimientos.extend(self.movimiento_diagonal(pieza,diagonal1,1))
        lista_de_movimientos.extend(self.movimiento_diagonal(pieza, diagonal2,2))
        lista_de_movimientos.extend(self.movimiento_diagonal(pieza, diagonal3,3))
        lista_de_movimientos.extend(self.movimiento_diagonal(pieza, diagonal4,4))


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
        primera_vez1=0
        primera_vez2 = 0
        primera_vez3 = 0
        primera_vez4 = 0

        for a in range(15):
            columnas_para_adelante = columnas_para_adelante + 1
            columnas_para_atras = columnas_para_atras - 1
            filas_para_arriba = filas_para_arriba + 1
            filas_para_abajo = filas_para_abajo - 1
            if self.encontrar_pieza((columnas_para_adelante,pieza.posicion[1]))==None:
                if columnas_para_adelante < 9 and hay_pieza_delante1==False:
                    lista_de_movimientos.append((columnas_para_adelante, pieza.posicion[1]))

            else:
                if primera_vez1==0:
                    lista_de_movimientos.append((columnas_para_adelante, pieza.posicion[1]))
                    primera_vez1 =1
                hay_pieza_delante1 = True
            if self.encontrar_pieza((columnas_para_atras, pieza.posicion[1])) == None:
                if columnas_para_atras > 0 and hay_pieza_delante2==False:
                    lista_de_movimientos.append((columnas_para_atras, pieza.posicion[1]))

            else:
                if primera_vez2 ==0:
                    lista_de_movimientos.append((columnas_para_atras, pieza.posicion[1]))
                    primera_vez2 =1
                hay_pieza_delante2 = True

            if self.encontrar_pieza((pieza.posicion[0],filas_para_abajo)) == None:
                if filas_para_abajo > 0 and hay_pieza_delante3==False:
                    lista_de_movimientos.append((pieza.posicion[0], filas_para_abajo))
            else:
                if primera_vez3==0:

                    lista_de_movimientos.append((pieza.posicion[0], filas_para_abajo))
                    primera_vez3=1

                hay_pieza_delante3 = True
            if self.encontrar_pieza((pieza.posicion[0],filas_para_arriba)) == None:
                if filas_para_arriba < 9 and hay_pieza_delante4==False:
                    lista_de_movimientos.append((pieza.posicion[0], filas_para_arriba))

            else:
                if primera_vez4==0:
                    lista_de_movimientos.append((pieza.posicion[0], filas_para_arriba))
                    primera_vez4=1
                hay_pieza_delante4 = True
        return lista_de_movimientos
    def posibles_movimientos_de_caballo(self,pieza) -> List[tuple[int, int]]:
        lista_de_movimientos = []
        if self.encontrar_pieza(((pieza.posicion[0] - 2, pieza.posicion[1] - 1)))==None:
            lista_de_movimientos.append((pieza.posicion[0] - 2, pieza.posicion[1] - 1))
        elif self.encontrar_pieza(((pieza.posicion[0] - 2, pieza.posicion[1] - 1))).bando!=pieza.bando:
            lista_de_movimientos.append((pieza.posicion[0] - 2, pieza.posicion[1] - 1))
        if self.encontrar_pieza(((pieza.posicion[0] - 2, pieza.posicion[1] + 1))) == None:
            lista_de_movimientos.append((pieza.posicion[0] - 2, pieza.posicion[1] + 1))
        elif self.encontrar_pieza(((pieza.posicion[0] - 2, pieza.posicion[1] + 1))).bando!=pieza.bando:
            lista_de_movimientos.append((pieza.posicion[0] - 2, pieza.posicion[1] + 1))
        if self.encontrar_pieza(((pieza.posicion[0] + 2), (pieza.posicion[1] - 1))) == None:
            lista_de_movimientos.append(((pieza.posicion[0] + 2), (pieza.posicion[1] - 1)))
        elif self.encontrar_pieza(((pieza.posicion[0] + 2), (pieza.posicion[1] - 1))).bando!=pieza.bando:
            lista_de_movimientos.append(((pieza.posicion[0] + 2), (pieza.posicion[1] - 1)))
        if self.encontrar_pieza(((pieza.posicion[0] + 2), (pieza.posicion[1] + 1))) == None:
            lista_de_movimientos.append(((pieza.posicion[0] + 2), (pieza.posicion[1] + 1)))
        elif self.encontrar_pieza(((pieza.posicion[0] + 2), (pieza.posicion[1] + 1))).bando!=pieza.bando:
            lista_de_movimientos.append(((pieza.posicion[0] + 2), (pieza.posicion[1] + 1)))
        if self.encontrar_pieza(((pieza.posicion[0] + 1), (pieza.posicion[1] + 2))) == None:
            lista_de_movimientos.append(((pieza.posicion[0] + 1), (pieza.posicion[1] + 2)))
        elif self.encontrar_pieza(((pieza.posicion[0] + 1), (pieza.posicion[1] + 2))).bando!=pieza.bando:
            lista_de_movimientos.append(((pieza.posicion[0] + 1), (pieza.posicion[1] + 2)))
        if self.encontrar_pieza(((pieza.posicion[0] - 1), (pieza.posicion[1] + 2))) == None:
            lista_de_movimientos.append(((pieza.posicion[0] - 1), (pieza.posicion[1] + 2)))
        elif self.encontrar_pieza(((pieza.posicion[0] - 1), (pieza.posicion[1] + 2))).bando != pieza.bando:
            lista_de_movimientos.append(((pieza.posicion[0] - 1), (pieza.posicion[1] + 2)))
        if self.encontrar_pieza(((pieza.posicion[0] + 1), (pieza.posicion[1] - 2))) == None:
            lista_de_movimientos.append(((pieza.posicion[0] + 1), (pieza.posicion[1] - 2)))
        elif self.encontrar_pieza(((pieza.posicion[0] + 1), (pieza.posicion[1] - 2))).bando!=pieza.bando:
            lista_de_movimientos.append(((pieza.posicion[0] + 1), (pieza.posicion[1] - 2)))
        if self.encontrar_pieza(((pieza.posicion[0] - 1), (pieza.posicion[1] - 2))) == None:
            lista_de_movimientos.append(((pieza.posicion[0] - 1), (pieza.posicion[1] - 2)))
        elif self.encontrar_pieza(((pieza.posicion[0] - 1), (pieza.posicion[1] - 2))).bando != pieza.bando:
            lista_de_movimientos.append(((pieza.posicion[0] - 1), (pieza.posicion[1] - 2)))
        lista_de_movimientos = list(
            filter(lambda a: a[0] > 0 and a[1] > 0 and a[0] <= 8 and a[1] <= 8, lista_de_movimientos))
        return lista_de_movimientos



    def posibles_movimientos_de_peon(self, pieza):
        turno = pieza.bando
        #si queremos rotar el tablero hay que poner un parametro booleano de si el blanco empieza abajo o arriba el blanco
        lista_de_movimientos = []
        if turno==TipoBando.BLANCO:
            lista_de_movimientos.append((pieza.posicion[0], pieza.posicion[1] + 1))
        if turno==TipoBando.NEGRO:
            lista_de_movimientos.append((pieza.posicion[0], pieza.posicion[1] - 1))
        if pieza.bando == TipoBando.BLANCO and pieza.posicion[1] == 2:
            lista_de_movimientos.append((pieza.posicion[0], pieza.posicion[1] + 2))
        if pieza.bando == TipoBando.NEGRO and pieza.posicion[1] == 7:
            lista_de_movimientos.append((pieza.posicion[0], pieza.posicion[1] - 2))


        return lista_de_movimientos

    def posibles_movimientos_bien_peon(self, pieza,turno,evitar_jaque):

        if evitar_jaque == False:
            lista_por_ahora = self.posibles_movimientos_de_peon(pieza)
            for a in self.piezas:
                if a.posicion in lista_por_ahora:
                    if pieza.bando==TipoBando.BLANCO:
                        if a.posicion==(pieza.posicion[0],pieza.posicion[1]+1):
                            self.remove(lista_por_ahora,a.posicion)
                            if pieza.posicion[1]==2:
                                self.remove(lista_por_ahora,(a.posicion[0],a.posicion[1]+2))
                        elif a.posicion==(pieza.posicion[0],pieza.posicion[1]+2):
                            self.remove(lista_por_ahora,a.posicion)
                    else:
                        if a.posicion==(pieza.posicion[0],pieza.posicion[1]-1):
                            self.remove(lista_por_ahora,a.posicion)
                            if pieza.posicion[1]==7:
                                self.remove(lista_por_ahora,(a.posicion[0], a.posicion[1] - 2))
                        elif a.posicion==(pieza.posicion[0],pieza.posicion[1]-2):
                            self.remove(lista_por_ahora,a.posicion)

                else:
                    pass

                if TipoBando.BLANCO==turno:
                    if a.posicion==(pieza.posicion[0]-1,pieza.posicion[1]+1) and a.bando!=pieza.bando :
                        lista_por_ahora.append((pieza.posicion[0]-1,pieza.posicion[1]+1))
                    if a.posicion==(pieza.posicion[0]+1,pieza.posicion[1]+1) and a.bando!=pieza.bando:
                        lista_por_ahora.append((pieza.posicion[0]+1,pieza.posicion[1]+1))
                else:
                    if a.posicion == (pieza.posicion[0] - 1, pieza.posicion[1] - 1) and a.bando != pieza.bando:
                        lista_por_ahora.append((pieza.posicion[0] - 1, pieza.posicion[1] - 1))
                    if a.posicion == (pieza.posicion[0] + 1, pieza.posicion[1] - 1) and a.bando != pieza.bando:
                        lista_por_ahora.append((pieza.posicion[0] + 1, pieza.posicion[1] - 1))
        else:
            lista_por_ahora=[]
            if TipoBando.BLANCO==turno:
                if pieza.posicion[0] == 1:
                    lista_por_ahora.append((pieza.posicion[0]+1,pieza.posicion[1]+1))
                elif pieza.posicion[0] == 8:
                    lista_por_ahora.append((pieza.posicion[0]-1,pieza.posicion[1]+1))
                else:
                    lista_por_ahora.append((pieza.posicion[0]-1,pieza.posicion[1]+1))
                    lista_por_ahora.append((pieza.posicion[0]+1,pieza.posicion[1]+1))
            else:
                if pieza.posicion[0] == 1:
                    lista_por_ahora.append((pieza.posicion[0] + 1, pieza.posicion[1] - 1))
                elif pieza.posicion[0] == 8:
                    lista_por_ahora.append((pieza.posicion[0] - 1, pieza.posicion[1] - 1))
                else:
                    lista_por_ahora.append((pieza.posicion[0] - 1, pieza.posicion[1] - 1))
                    lista_por_ahora.append((pieza.posicion[0] + 1, pieza.posicion[1] - 1))
        return lista_por_ahora
    def coronacion(self,pieza,pieza_elegida):
        print(pieza_elegida)
        if pieza_elegida==TipoPieza.REINA:
            self.piezas.append(Pieza(TipoPieza.REINA,True,pieza.posicion,pieza.bando))
            self.remove(self.piezas,pieza)
        elif pieza_elegida==TipoPieza.TORRE:
            self.piezas.append(Pieza(TipoPieza.TORRE,True,pieza.posicion,pieza.bando))
            self.remove(self.piezas,pieza)
        elif pieza_elegida==TipoPieza.ALFIL:
            self.piezas.append(Pieza(TipoPieza.ALFIL,True,pieza.posicion,pieza.bando))
            self.remove(self.piezas,pieza)
        elif pieza_elegida==TipoPieza.CABALLO:
            self.piezas.append(Pieza(TipoPieza.CABALLO,True,pieza.posicion,pieza.bando))
            self.remove(self.piezas,pieza)


    def enpasseau(self,pieza):
       pass
    def posibles_movimientos_de_reina(self,pieza):
        lista_de_movimientos = []
        lista_de_movimientos.extend(self.posibles_movimientos_bien_torre(pieza))

        lista_de_movimientos.extend(self.posibles_movimientos_de_alfil(pieza))
        return lista_de_movimientos

    def remove(self, lista,posicion):
        if posicion in lista:
            lista.remove(posicion)

    def posibles_movimientos_de_rey(self,pieza):
        lista_de_movimientos = []
        if self.encontrar_pieza(((pieza.posicion[0]+1,pieza.posicion[1]))) == None:
            lista_de_movimientos.append((pieza.posicion[0]+1,pieza.posicion[1]))
        elif self.encontrar_pieza(((pieza.posicion[0]+1,pieza.posicion[1]))).bando != pieza.bando:
            lista_de_movimientos.append((pieza.posicion[0]+1,pieza.posicion[1]))
        if self.encontrar_pieza(((pieza.posicion[0]+1, pieza.posicion[1]+1))) == None:
            lista_de_movimientos.append((pieza.posicion[0]+1, pieza.posicion[1]+1))
        elif self.encontrar_pieza(((pieza.posicion[0]+1, pieza.posicion[1]+1))).bando != pieza.bando:
            lista_de_movimientos.append((pieza.posicion[0]+1, pieza.posicion[1]+1))
        if self.encontrar_pieza(((pieza.posicion[0]+1, pieza.posicion[1]-1))) == None:
            lista_de_movimientos.append((pieza.posicion[0]+1, pieza.posicion[1]-1))
        elif self.encontrar_pieza(((pieza.posicion[0]+1, pieza.posicion[1]-1))).bando != pieza.bando:
            lista_de_movimientos.append((pieza.posicion[0]+1, pieza.posicion[1]-1))
        if self.encontrar_pieza(((pieza.posicion[0]-1, pieza.posicion[1]))) == None:
            lista_de_movimientos.append((pieza.posicion[0]-1, pieza.posicion[1]))
        elif self.encontrar_pieza(((pieza.posicion[0]-1, pieza.posicion[1]))).bando != pieza.bando:
            lista_de_movimientos.append((pieza.posicion[0]-1, pieza.posicion[1]))
        if self.encontrar_pieza((pieza.posicion[0]-1, pieza.posicion[1]+1)) == None:
            lista_de_movimientos.append((pieza.posicion[0]-1, pieza.posicion[1]+1))
        elif self.encontrar_pieza(((pieza.posicion[0]-1, pieza.posicion[1]+1))).bando != pieza.bando:
            lista_de_movimientos.append((pieza.posicion[0]-1, pieza.posicion[1]+1))
        if self.encontrar_pieza(((pieza.posicion[0]-1, pieza.posicion[1]-1))) == None:
            lista_de_movimientos.append((pieza.posicion[0]-1, pieza.posicion[1]-1))
        elif self.encontrar_pieza(((pieza.posicion[0]-1, pieza.posicion[1]-1))).bando != pieza.bando:
            lista_de_movimientos.append((pieza.posicion[0]-1, pieza.posicion[1]-1))
        if self.encontrar_pieza(((pieza.posicion[0], pieza.posicion[1]+1))) == None:
            lista_de_movimientos.append((pieza.posicion[0], pieza.posicion[1]+1))
        elif self.encontrar_pieza(((pieza.posicion[0], pieza.posicion[1]+1))).bando != pieza.bando:
            lista_de_movimientos.append((pieza.posicion[0], pieza.posicion[1]+1))
        if self.encontrar_pieza(((pieza.posicion[0], pieza.posicion[1]-1))) == None:
            lista_de_movimientos.append((pieza.posicion[0], pieza.posicion[1]-1))
        elif self.encontrar_pieza(((pieza.posicion[0], pieza.posicion[1]-1))).bando != pieza.bando:
            lista_de_movimientos.append((pieza.posicion[0], pieza.posicion[1]-1))
        lista_de_movimientos = list(
            filter(lambda a: a[0] > 0 and a[1] > 0 and a[0] <= 8 and a[1] <= 8, lista_de_movimientos))
        return lista_de_movimientos

#Turno: busco si hay lista de jaque de ese rey
    def lista_de_jaque(self,turno, sin_rey): #todas las piezas que pueden comer al rey
        lista_de_piezas = []
        rey_blanco = self.encontrar_rey(TipoBando.BLANCO)
        rey_negro = self.encontrar_rey(TipoBando.NEGRO)
        rey = rey_negro
        if turno == TipoBando.BLANCO:
            rey = rey_blanco
        for a in self.piezas:
            if a.bando != turno:
                for b in self.posibles_movimientos(a, a.bando, sin_rey):
                    if rey.posicion == b:
                        lista_de_piezas.append(a.posicion)

        print("Tiene jaque:", lista_de_piezas)
        return lista_de_piezas

    def tiene_jaque(self,turno, sin_rey=False):
        if len(self.lista_de_jaque(turno, sin_rey))>0:
            return True
        else:
            return False

    def anti_turno(self,turno):
        if turno==TipoBando.BLANCO:
            return TipoBando.NEGRO
        else:
            return TipoBando.BLANCO
    def posibles_movimientos_enroque(self,pieza,lista_de_movimiento,turno):
        if pieza.movio == False:
            # lo hacemos para la fila 1 y 8
            for fila in [1, 8]:
                # Agrega los movimientos de enroque
                posReyColDerecha = pieza.posicion[0] + 2
                if self.encontrar_pieza((posReyColDerecha, fila)) == None:
                    lista_de_movimiento.append((posReyColDerecha, fila))
                posReyColIzquierda = pieza.posicion[0] - 2
                if self.encontrar_pieza((posReyColIzquierda, fila)) == None:
                    lista_de_movimiento.append((posReyColIzquierda, fila))

                # elimina los movimientos de enroque si hay un jaque posible
                for cualquiera in self.piezas:
                    if cualquiera.bando != pieza.bando:
                        lista_de_movimientos_totales = self.posibles_movimientos(cualquiera, self.anti_turno(turno),
                                                                                 True)
                        if lista_de_movimientos_totales != None:
                            for d in lista_de_movimientos_totales:
                                for e in lista_de_movimiento:
                                    posReyColizq1 = pieza.posicion[0] - 1
                                    posReyColDer1 = pieza.posicion[0] + 1
                                    if (d[0] == posReyColizq1 and d[1] == fila):
                                        self.remove(lista_de_movimiento, (d[0] - 2, d[1]))
                                        self.remove(lista_de_movimiento, (d[0] - 1, d[1]))
                                    elif (d[0] == posReyColDer1 and d[1] == fila):
                                        self.remove(lista_de_movimiento, (d[0] + 2, d[1]))
                                        self.remove(lista_de_movimiento, (d[0] + 1, d[1]))
                                    elif d == e:
                                        lista_de_movimiento.remove(d)


            #  Elima el enroque si hay una pieza en la trayectoria
            if (pieza.posicion[0] - 2, pieza.posicion[1]) in lista_de_movimiento:
                if pieza.bando == TipoBando.BLANCO and (self.encontrar_pieza((1, 1) != None
                                                                             or self.encontrar_pieza(
                    (1, 1)).movio == True or self.encontrar_pieza((1, 1)).tipo != TipoPieza.TORRE) \
                                                        or self.encontrar_pieza((2, 1)) != None or self.encontrar_pieza(
                            (3, 1)) != None or self.encontrar_pieza((4, 1)) != None):
                    self.remove(lista_de_movimiento, (pieza.posicion[0] - 2, pieza.posicion[1]))
                if pieza.bando == TipoBando.NEGRO and (self.encontrar_pieza((1, 8) != None
                                                                            or self.encontrar_pieza(
                    (1, 8)).movio == True or self.encontrar_pieza((1, 8)).tipo != TipoPieza.TORRE) \
                                                       or self.encontrar_pieza((2, 8)) != None or self.encontrar_pieza(
                            (3, 8)) != None or self.encontrar_pieza((4, 8)) != None):
                    self.remove(lista_de_movimiento, (pieza.posicion[0] - 2, pieza.posicion[1]))
            if (pieza.posicion[0] + 2, pieza.posicion[1]) in lista_de_movimiento:
                if pieza.bando == TipoBando.BLANCO and (
                        self.encontrar_pieza((8, 1) != None or self.encontrar_pieza((8, 1)).movio == True
                                             or self.encontrar_pieza(
                            (8, 1)).tipo != TipoPieza.TORRE) or self.encontrar_pieza(
                    (7, 1)) != None or self.encontrar_pieza((6, 1)) != None):
                    self.remove(lista_de_movimiento, (pieza.posicion[0] + 2, pieza.posicion[1]))
                if pieza.bando == TipoBando.NEGRO and (
                        self.encontrar_pieza((8, 8) != None or self.encontrar_pieza((8, 8)).movio == True
                                             or self.encontrar_pieza(
                            (8, 8)).tipo != TipoPieza.TORRE) or self.encontrar_pieza(
                    (7, 8)) != None or self.encontrar_pieza((6, 8)) != None):
                    self.remove(lista_de_movimiento, (pieza.posicion[0] + 2, pieza.posicion[1]))

    def posibles_movimientos_rey_bien(self,pieza,turno):
        lista_de_movimiento=self.posibles_movimientos_de_rey(pieza)
        print("pos del rey", pieza.posicion, pieza.bando, " ", lista_de_movimiento,  inspect.stack()[3][3])
        posicion_moment=pieza.posicion
        #Eliminamos los movimiento que hacen jaque
        for b in lista_de_movimiento.copy():
            #hay que remover y luego agregar a la lista al alfil si el rey puede comer
            la_que_hace = self.encontrar_pieza(b)
            if la_que_hace != None:
                self.remover_pieza(la_que_hace)
                pieza.posicion = b
                if self.tiene_jaque(turno,True) == True:
                    print("remmove1 by", b)
                    self.remove(lista_de_movimiento, b)
                self.piezas.append(la_que_hace)
                pieza.posicion=posicion_moment

        # ENROQUE
        if pieza.movio == False:
            self.posibles_movimientos_enroque(pieza,lista_de_movimiento,turno)

        #eliminar los casos donde el peon hace jaque al movimiento del rey
        for peon in self.piezas:
            if peon.tipo==TipoPieza.PEON and peon.bando!=pieza.bando:
                peon_puede_comer=self.posibles_movimientos_bien_peon(peon,peon.bando,True)
                for movimientos in peon_puede_comer:
                    if movimientos in lista_de_movimiento:
                        print("remove por por diagonal peon", movimientos, " ", peon.posicion)
                        self.remove(lista_de_movimiento,movimientos)

        print("LISTA COMPLETA", pieza.bando, " ",  lista_de_movimiento)
        return lista_de_movimiento
    def evitar_jaque(self,pieza,turno):
        #ver si hay posibles movimientos del rey si hay jaque
        posicion_momentanea = pieza.posicion
        lista_de_movimientos=[]
        if self.tiene_jaque(turno)==True:
            for a in self.posibles_movimientos(pieza,turno):
                la_que_hace = self.encontrar_pieza(a)
                if la_que_hace!=None:
                    self.remover_pieza(la_que_hace)
                pieza.posicion=a
                if self.tiene_jaque(turno)==False:
                    lista_de_movimientos.append(a)
                if la_que_hace!=None:
                    self.piezas.append(la_que_hace)
        pieza.posicion=posicion_momentanea
        return lista_de_movimientos
    def piezas_a_letras(self,pieza):
        if TipoBando.BLANCO==pieza.bando:
            if pieza.tipo==TipoPieza.TORRE:
                return "R"
            if pieza.tipo ==TipoPieza.ALFIL:
                return "B"
            if pieza.tipo ==TipoPieza.REY:
                return "K"
            if pieza.tipo ==TipoPieza.REINA:
                return "Q"
            if pieza.tipo==TipoPieza.PEON:
                return "P"
            if pieza.tipo==TipoPieza.CABALLO:
                return "N"
        else:
            if pieza.tipo==TipoPieza.TORRE:
                return "r"
            if pieza.tipo ==TipoPieza.ALFIL:
                return "b"
            if pieza.tipo ==TipoPieza.REY:
                return "k"
            if pieza.tipo ==TipoPieza.REINA:
                return "q"
            if pieza.tipo==TipoPieza.PEON:
                return "p"
            if pieza.tipo==TipoPieza.CABALLO:
                return "n"
    def notacion_fen(self,turno):
        lista_strins_inicial=""
        pieza_anterior=None
        esp = "%20"
        encontro_una=None
        for f in range(8):
            contador = 0


            encontro_una = False


            f=8-f

            for c in range(8):
                c=c+1
                hay_pieza=self.encontrar_pieza((c,f))
                if hay_pieza==None:
                    contador=contador+1
                else:
                    if contador!=0:
                        lista_strins_inicial+=f"{contador}{self.piezas_a_letras(hay_pieza)}"
                    elif contador==0:
                        lista_strins_inicial+=f"{self.piezas_a_letras(hay_pieza)}"
                    contador = 0
                    encontro_una=True
                if hay_pieza!=None:
                    pieza_anterior = hay_pieza

            if contador > 0:
                lista_strins_inicial+=str(contador)
            if f!=1:
                lista_strins_inicial += "/"


        if turno==TipoBando.BLANCO:
            lista_strins_inicial+= esp + "w"
        else:
            lista_strins_inicial+= esp + "b"
        lista_strins_inicial+= esp + "-"
        lista_strins_inicial+= esp + "-"
        lista_strins_inicial+= esp + "0" + esp + "1"
        return lista_strins_inicial

    def game_over(self,turno):
        if self.tiene_jaque(turno) == False:
            return False
        listilla = []
        for a in self.piezas:
            if turno==a.bando:
                for b in self.evitar_jaque(a,turno):
                    listilla.append(b)
        if len(listilla) > 0:
            return False

        return True
    def tablas(self,turno):
        for a in self.piezas:
            if a.bando == turno:
                if len(self.posibles_movimientos(a,turno)) > 0:
                    return False

        return True

