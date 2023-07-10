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
        if self.jaque()==True:
             contador=0
             #if self.posibles_movimientos(self.lista_de_jaque()[contador]) == b:
                 #lista_de_piezas.append(b)

    def posibles_movimientos_bien_torre(self,pieza: Pieza):
        lista_por_ahora=self.posibles_movimientos_de_torre(pieza)

        for a in self.piezas:
                if a.posicion in lista_por_ahora and a.bando==pieza.bando:
                #aca esta el error de comer de la torre

                    lista_por_ahora.remove(a.posicion)
        print(lista_por_ahora)
        return lista_por_ahora

    def posibles_movimientos(self,pieza: Pieza):
        if TipoPieza.ALFIL == pieza.tipo:
            return self.posibles_movimientos_bien_alfil(pieza)
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

    def posibles_movimientos_bien_alfil(self,pieza):
        lista_por_ahora=self.posibles_movimientos_de_alfil(pieza)


        for a in self.piezas:
                if a.posicion in lista_por_ahora and a.bando==pieza.bando:
                        #aca esta el error de comer de la torre

                    lista_por_ahora.remove(a.posicion)



        return lista_por_ahora

    def movimiento_diagonal(self,pieza,diagonal,tipo):
        lista_de_movimientos=[]
        primera_vez1 = 0
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
            if diagonal[0] >= 1 and diagonal[1] < 9:
                if self.encontrar_pieza(diagonal) == None:
                    if hay_pieza_delante1 == False:
                        lista_de_movimientos.append(diagonal)
                else:
                    if self.encontrar_pieza(diagonal).bando != pieza.bando and primera_vez1 == 0:
                        lista_de_movimientos.append(diagonal)
                        primera_vez1 = 1
                    hay_pieza_delante1 = True
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
            if self.jaque()==False:
                if self.encontrar_pieza((columnas_para_adelante,pieza.posicion[1]))==None:
                    if columnas_para_adelante < 9 and hay_pieza_delante1==False:
                        lista_de_movimientos.append((columnas_para_adelante, pieza.posicion[1]))

                else:
                    if self.encontrar_pieza((columnas_para_adelante, pieza.posicion[1])).bando != pieza.bando and primera_vez1==0:
                        lista_de_movimientos.append((columnas_para_adelante, pieza.posicion[1]))
                        primera_vez1 =1
                    hay_pieza_delante1 = True
                if self.encontrar_pieza((columnas_para_atras, pieza.posicion[1])) == None:
                    if columnas_para_atras > 0 and hay_pieza_delante2==False:
                        lista_de_movimientos.append((columnas_para_atras, pieza.posicion[1]))

                else:
                    if self.encontrar_pieza((columnas_para_atras, pieza.posicion[1])).bando != pieza.bando and primera_vez2 ==0:
                        lista_de_movimientos.append((columnas_para_atras, pieza.posicion[1]))
                        primera_vez2 =1
                    hay_pieza_delante2 = True

                if self.encontrar_pieza((pieza.posicion[0],filas_para_abajo)) == None:
                    if filas_para_abajo > 0 and hay_pieza_delante3==False:
                        lista_de_movimientos.append((pieza.posicion[0], filas_para_abajo))
                else:
                    if self.encontrar_pieza((pieza.posicion[0], filas_para_abajo)).bando != pieza.bando and primera_vez3==0:
                        #print("La coordenada es:", (pieza.posicion[0],filas_para_abajo))
                        lista_de_movimientos.append((pieza.posicion[0], filas_para_abajo))
                        primera_vez3=1

                    hay_pieza_delante3 = True
                if self.encontrar_pieza((pieza.posicion[0],filas_para_arriba)) == None:
                    if filas_para_arriba < 9 and hay_pieza_delante4==False:
                        lista_de_movimientos.append((pieza.posicion[0], filas_para_arriba))

                else:
                    if self.encontrar_pieza((pieza.posicion[0],filas_para_arriba)).bando != pieza.bando and primera_vez4==0:
                        lista_de_movimientos.append((pieza.posicion[0], filas_para_arriba))
                        primera_vez4=1
                    hay_pieza_delante4 = True
            else:
                lista_de_movimientos.append(self.encontrar_piezas_pueden_llegar(pieza))
        #print(lista_de_movimientos)
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
        lista_de_movimientos.extend(self.posibles_movimientos_bien_torre(pieza))

        lista_de_movimientos.extend(self.posibles_movimientos_de_alfil(pieza))
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

    def lista_de_jaque(self): #todas las piezas que pueden comer al rey
        lista_de_piezas = []
        rey_blanco = self.encontrar_rey(TipoBando.BLANCO)
        rey_negro = self.encontrar_rey(TipoBando.NEGRO)
        for a in self.piezas:
            for b in self.posibles_movimientos(a):
                if rey_blanco.posicion == b:
                    lista_de_piezas.append(a)
                if rey_negro.posicion == b:
                    lista_de_piezas.append(a)
        return lista_de_piezas
    def jaque(self):
        if self.lista_de_jaque>0:
            return True
        else:
            return False
    def movimiento_rey_en_jaque(self):
        pass
    def evitar_jaque(self):
        #ver si hay posibles movimientos del rey si hay jaque
        for a in self.piezas:
            
