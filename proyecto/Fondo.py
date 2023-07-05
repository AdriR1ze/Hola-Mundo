import pygame
from menu import Menu
from pygame import MOUSEBUTTONDOWN, RESIZABLE, surface

from Pieza import TipoPieza,TipoBando,Pieza
from TableroConceptual import Tablero
from pygame.locals import *
pos_inicial = None
pos_destino = None
mover_pieza = False
tablero_tamano=(802, 802)
NEGRO = (0, 0, 0)
tablero_primario=Tablero()
pygame.init()
pantalla = pygame.display.set_mode(tablero_tamano)
reloj = pygame.time.Clock()
Terminar=False


def posicion_relativa(posicion: tuple[int, int]):
    x = posicion[0] * tablero_tamano[0]/8 + 2 - (tablero_tamano[0]/8)-1
    y = (9 - posicion[1]) * tablero_tamano[0]/8 + 2 - tablero_tamano[0]/8-1
    return (x, y)

def posicion_relativa_centrada(posicion: tuple[int, int]):
    x = posicion[0] * tablero_tamano[0]/8 + 2 - 99+tablero_tamano[0]/16
    y = (9 - posicion[1]) * tablero_tamano[0]/8 + 2 - 99+tablero_tamano[0]/16
    return (x, y)


def numero_relativo(posicion: tuple[int, int]):
    x = int((posicion[0] - 97) / 100 + 2)
    y = 9 - int(posicion[1] / 100 + 0.02 + 0.99)
    return (x, y)
class dibujar:

    def dibujar_tablero(self):

        imagen = "Imagenes\\Tablero.png"
        imp = pygame.image.load(imagen).convert()
        imp = pygame.transform.scale(imp, (tablero_tamano[0],tablero_tamano[1]))
        pantalla.blit(imp,(0,0))

    def dibujar_posibles(self,posicion):
        a: Pieza=tablero_primario.encontrar_pieza(posicion)
        if a!=None:
            #print("tipo de pieza", a.tipo)
            la_posicion = tablero_primario.posibles_movimientos(a)
            if len(la_posicion) > 0:
                #print("comprobante",la_posicion)
                for b in la_posicion:
                    posicion_a_dibujar = posicion_relativa_centrada(b)
                    #print(posicion_a_dibujar)
                    c=pygame.draw.circle(pantalla, (40,40,40), (posicion_a_dibujar), 8, 0)
                    c
                    #print("posicion a posibles", b)

    def mover_pieza(self,posicion):
        turno=objeto_dibujo.cambiar_turno(NEGRO)
        for a in tablero_primario.piezas:
            for b in tablero_primario.posibles_movimientos(a):
                if posicion==b:
                    objeto_dibujo.dibujar_una_pieza(posicion)
        pieza = tablero_primario.encontrar_pieza(posicion)
        if pieza !=None and pieza.bando == turno:
            movimientos = tablero_primario.posibles_movimientos(pieza)
            if len(movimientos) > 0:
                if posicion in movimientos:
                    pieza.posicion = posicion
                    return True
        return False
    def cambiar_turno(self,turno):
        if turno == TipoBando.BLANCO:
            turno = TipoBando.NEGRO
        else:
            turno = TipoBando.BLANCO
        return turno
    def dibujar_piezas(self):
        for a in tablero_primario.piezas:
            #print(a.bando)
            if a.bando==TipoBando.BLANCO:
                #print("comprobante")
                if a.tipo == TipoPieza.CABALLO:
                    imagen = "Imagenes/CaballoBlanco.png"
                    #print("otroooo")
                if a.tipo == TipoPieza.ALFIL:
                    imagen = "Imagenes/AlfilBlanco.png"
                if a.tipo == TipoPieza.REY:
                    imagen = "Imagenes/ReyBlanco.png"
                if a.tipo == TipoPieza.REINA:
                    imagen = "Imagenes/ReinaBlanca.png"
                if a.tipo == TipoPieza.TORRE:
                    imagen = "Imagenes/TorreBlanca.png"
                if a.tipo == TipoPieza.PEON:
                    imagen = "Imagenes/PeonBlanco.png"
            else:
               if a.tipo == TipoPieza.CABALLO:
                   imagen = "Imagenes/CaballoNegro.png"
               if a.tipo == TipoPieza.ALFIL:
                   imagen = "Imagenes/AlfilNegro.png"
               if a.tipo == TipoPieza.REY:
                   imagen = "Imagenes/ReyNegro.png"
               if a.tipo == TipoPieza.REINA:
                   imagen = "Imagenes/ReinaNegra.png"
               if a.tipo == TipoPieza.TORRE:
                   imagen = "Imagenes/TorreNegra.png"
               if a.tipo == TipoPieza.PEON:
                   imagen = "Imagenes/PeonNegro.png"

            imp = pygame.image.load(imagen).convert_alpha()
            imp = pygame.transform.scale(imp, (tablero_tamano[0]/8.35416, tablero_tamano[1]/8.35416))
            p = posicion_relativa(a.posicion)
            pantalla.blit(imp, p)
    def dibujar_una_pieza(posicion):
        for a in tablero_primario.piezas:
            if a.posicion==posicion:
                #print("por fa")
                if a.bando == TipoBando.BLANCO:
                    # print("comprobante")
                    if a.tipo == TipoPieza.CABALLO:
                        imagen = "Imagenes/CaballoBlanco.png"
                        # print("otroooo")
                    if a.tipo == TipoPieza.ALFIL:
                        imagen = "Imagenes/AlfilBlanco.png"
                    if a.tipo == TipoPieza.REY:
                        imagen = "Imagenes/ReyBlanco.png"
                    if a.tipo == TipoPieza.REINA:
                        imagen = "Imagenes/ReinaBlanca.png"
                    if a.tipo == TipoPieza.TORRE:
                        imagen = "Imagenes/TorreBlanca.png"
                    if a.tipo == TipoPieza.PEON:
                        imagen = "Imagenes/PeonBlanco.png"
                else:
                    if a.tipo == TipoPieza.CABALLO:
                        imagen = "Imagenes/CaballoNegro.png"
                    if a.tipo == TipoPieza.ALFIL:
                        imagen = "Imagenes/AlfilNegro.png"
                    if a.tipo == TipoPieza.REY:
                        imagen = "Imagenes/ReyNegro.png"
                    if a.tipo == TipoPieza.REINA:
                        imagen = "Imagenes/ReinaNegra.png"
                    if a.tipo == TipoPieza.TORRE:
                        imagen = "Imagenes/TorreNegra.png"
                    if a.tipo == TipoPieza.PEON:
                        imagen = "Imagenes/PeonNegro.png"

                imp = pygame.image.load(imagen).convert_alpha()
                imp = pygame.transform.scale(imp, (tablero_tamano[0] / 8.35416, tablero_tamano[1] / 8.35416))
                p = posicion_relativa(a.posicion)
                pantalla.blit(imp, p)
#def movimiento_de_pieza():
    #for i in tablero_primario.piezas:
        #i.posicion(tablero_primario.posibles_movimientos(i))
objeto_dibujo=dibujar()
pos=None
dibuja=True
#print(tablero_primario)
mover=0
while not Terminar:

    for Evento in pygame.event.get():
        if Evento.type == pygame.QUIT:
            Terminar = True
        if Evento.type == MOUSEBUTTONDOWN:
            pos = numero_relativo(Evento.pos)
            dibujar = True
            if pos in tablero_primario.piezas:
                mover_pieza(pos)
                objeto_dibujo.cambiar_turno(NEGRO)

    if dibuja:
        dibuja=False
        objeto_dibujo.dibujar_tablero()
        objeto_dibujo.dibujar_piezas()
        if pos!=None:
            objeto_dibujo.dibujar_posibles(pos)
            mover=1







    pygame.display.update()
    pygame.display.flip()
    reloj.tick(20)  # Limitamos a 20 fotogramas por segundo
pygame.quit()