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

    def verificar_movimiento(self, movimiento):
        if self.tiene_jaque()==True:
             contador=0
             #if self.posibles_movimientos(self.lista_de_jaque()[contador]) == b:
                 #lista_de_piezas.append(b)

    def posibles_movimientos_bien_torre(self,pieza: Pieza):
        lista_por_ahora=self.posibles_movimientos_de_torre(pieza)

        for a in self.piezas:
                if a.posicion in lista_por_ahora and a.bando==pieza.bando:
                #aca esta el error de comer de la torre

                    lista_por_ahora.remove(a.posicion)
        return lista_por_ahora

    def posibles_movimientos_bien(self, pieza: Pieza, sin_rey=False):
        lista_de_movimientos=self.posibles_movimientos(pieza, sin_rey)
        posicion_momentanea=pieza.posicion
        rs=[]
        for a in lista_de_movimientos:
            pieza.posicion=a

            if self.tiene_jaque()==False:
                rs.append(a)
            pieza.posicion=posicion_momentanea
        return rs

    def posibles_movimientos(self,pieza: Pieza, sin_rey = False):
        lista_de_movimientos=[]
        if TipoPieza.ALFIL == pieza.tipo:
            lista_de_movimientos=self.posibles_movimientos_bien_alfil(pieza)
        if TipoPieza.CABALLO == pieza.tipo:
            lista_de_movimientos=self.posibles_movimientos_de_caballo(pieza)
        if sin_rey == False and TipoPieza.TORRE == pieza.tipo:
            lista_de_movimientos=self.posibles_movimientos_bien_torre(pieza)
        if TipoPieza.PEON == pieza.tipo:
            lista_de_movimientos=self.posibles_movimientos_bien_peon(pieza)
        if TipoPieza.REINA==pieza.tipo:
            lista_de_movimientos=self.posibles_movimientos_de_reina(pieza)
        if sin_rey == False and TipoPieza.REY==pieza.tipo:
            lista_de_movimientos=self.posibles_movimientos_rey_bien(pieza)

        return lista_de_movimientos
    def posibles_movimientos_bien_alfil(self,pieza):
        lista_por_ahora=self.posibles_movimientos_de_alfil(pieza)
        for a in self.piezas:
                if a.posicion in lista_por_ahora and a.bando==pieza.bando:
                        #aca esta el error de comer de la torre
                    lista_por_ahora.remove(a.posicion)
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

    def posibles_movimientos_bien_peon(self, pieza):
        lista_por_ahora = self.posibles_movimientos_de_peon(pieza)
        for a in self.piezas:
            if a.posicion in lista_por_ahora:
                if pieza.bando==TipoBando.BLANCO:
                    if a.posicion==(pieza.posicion[0],pieza.posicion[1]+1):
                        lista_por_ahora.remove(a.posicion)
                        if pieza.posicion[1]==2:
                            lista_por_ahora.remove((a.posicion[0],a.posicion[1]+1))
                    elif a.posicion==(pieza.posicion[0],pieza.posicion[1]+2):
                        lista_por_ahora.remove(a.posicion)
                else:
                    if a.posicion==(pieza.posicion[0],pieza.posicion[1]-1):
                        lista_por_ahora.remove(a.posicion)
                        if pieza.posicion[1]==7:
                            lista_por_ahora.remove((a.posicion[0], a.posicion[1] - 1))
                    elif a.posicion==(pieza.posicion[0],pieza.posicion[1]-2):
                        lista_por_ahora.remove(a.posicion)

            else:
                pass
            if a.posicion==(pieza.posicion[0]-1,pieza.posicion[1]+1) and a.bando!=pieza.bando:
                lista_por_ahora.append((pieza.posicion[0]-1,pieza.posicion[1]+1))
            if a.posicion==(pieza.posicion[0]+1,pieza.posicion[1]+1) and a.bando!=pieza.bando:
                lista_por_ahora.append((pieza.posicion[0]+1,pieza.posicion[1]+1))
        return lista_por_ahora
    def enpasseau(self,pieza):
       pass
    def posibles_movimientos_de_reina(self,pieza):
        lista_de_movimientos = []
        lista_de_movimientos.extend(self.posibles_movimientos_bien_torre(pieza))

        lista_de_movimientos.extend(self.posibles_movimientos_de_alfil(pieza))
        return lista_de_movimientos

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

    def lista_de_jaque(self): #todas las piezas que pueden comer al rey
        lista_de_piezas = []
        rey_blanco = self.encontrar_rey(TipoBando.BLANCO)
        rey_negro = self.encontrar_rey(TipoBando.NEGRO)
        for a in self.piezas:
            if a.tipo!=TipoPieza.REY:
                for b in self.posibles_movimientos(a):
                    if rey_blanco.posicion == b:
                        lista_de_piezas.append(a)
                    if rey_negro.posicion == b:
                        lista_de_piezas.append(a)
        return lista_de_piezas

    def tiene_jaque(self):
        if len(self.lista_de_jaque())>0:
            return True
        else:
            return False

    def posibles_movimientos_rey_bien(self,pieza):
        lista_de_movimiento=self.posibles_movimientos_de_rey(pieza)
        posicion_moment=pieza.posicion
        for b in self.posibles_movimientos_de_rey(pieza):
            #hay que remover y luego agregar a la lista al alfil si el rey puede comer
            pieza.posicion=b
            if self.tiene_jaque()==True:
                lista_de_movimiento.remove(b)
        pieza.posicion=posicion_moment

        # ENROQUE, TODO falta para hacer negras
        if pieza.movio==False:
            g=pieza.posicion[0]+2
            if self.encontrar_pieza((g,1))==None:
                lista_de_movimiento.append((g,1))
            a=pieza.posicion[0]-2
            if self.encontrar_pieza((a,1))==None:
                lista_de_movimiento.append((a,1))
            a = pieza.posicion[0] - 1
            g = pieza.posicion[0] + 1
            for cualquiera in self.piezas:
                if cualquiera.bando!=pieza.bando:
                    lista_de_movimientos_totales=self.posibles_movimientos(cualquiera, True)
                    if lista_de_movimientos_totales!=None:
                        for d in lista_de_movimientos_totales:
                            for e in lista_de_movimiento:
                                if (d[0] == a and d[1]==1):
                                    lista_de_movimiento.remove((d[0] - 2, d[1]))
                                elif (d[0] == g and d[1]==1):
                                    lista_de_movimiento.remove((d[0] + 2, d[1]))
                                elif d==e:
                                    lista_de_movimiento.remove(d)
            if (pieza.posicion[0] - 2, pieza.posicion[1]) in lista_de_movimiento:
                if pieza.bando==TipoBando.BLANCO and (self.encontrar_pieza((1, 1)) == None or self.encontrar_pieza((1, 1)).movio == True and self.encontrar_pieza((1, 1)).tipo==TipoPieza.TORRE):
                    lista_de_movimiento.remove((pieza.posicion[0] - 2, pieza.posicion[1]))
                if pieza.bando==TipoBando.NEGRO and (self.encontrar_pieza((1, 8)) == None or self.encontrar_pieza((1, 8)).movio == True and self.encontrar_pieza((1, 8)).tipo==TipoPieza.TORRE):
                    lista_de_movimiento.remove((pieza.posicion[0] - 2, pieza.posicion[1]))
            if (pieza.posicion[0] + 2, pieza.posicion[1]) in lista_de_movimiento:
                if pieza.bando==TipoBando.BLANCO and (self.encontrar_pieza((8, 1)) == None or self.encontrar_pieza((8, 1)).movio == True and self.encontrar_pieza((8, 1)).tipo==TipoPieza.TORRE):
                    lista_de_movimiento.remove((pieza.posicion[0] + 2, pieza.posicion[1]))
                if pieza.bando==TipoBando.NEGRO and (self.encontrar_pieza((8, 8)) == None or self.encontrar_pieza((8, 8)).movio == True and self.encontrar_pieza((8, 8)).tipo==TipoPieza.TORRE):
                    lista_de_movimiento.remove((pieza.posicion[0] + 2, pieza.posicion[1]))




        return lista_de_movimiento
    def evitar_jaque(self,pieza):
        #ver si hay posibles movimientos del rey si hay jaque
        posicion_momentanea = pieza.posicion
        lista_de_movimientos=[]
        if self.tiene_jaque()==True:
            for a in self.posibles_movimientos(pieza):
                la_que_hace = self.encontrar_pieza(a)
                if la_que_hace!=None:
                    self.remover_pieza(la_que_hace)
                pieza.posicion=a
                if self.tiene_jaque()==False:
                    lista_de_movimientos.append(a)
                if la_que_hace!=None:
                    self.piezas.append(la_que_hace)
        pieza.posicion=posicion_momentanea
        if pieza.tipo==TipoPieza.REY:
            lista_de_movimientos.extend(self.posibles_movimientos(self.encontrar_rey(pieza.bando)))
        return lista_de_movimientos

    def notacion_fen(self):
        columna1=[]
        columna2=[]
        columna3=[]
        columna4=[]
        columna5=[]
        columna6=[]
        columna7=[]
        columna8=[]
        lista_strins_inicial=[]
        longitud=-1
        contador=0
        una_vez=0
        lista_strins_final=[]
        self.piezas.sort(key=lambda x: (x.posicion[0]+(x.posicion[1]-1)*8))
        for a in self.piezas:


            longitud_a_colocar = a.posicion[0]-1

            lista_strins_inicial.append((longitud_a_colocar,a))
        for b in lista_strins_inicial:
            contador=contador+b





