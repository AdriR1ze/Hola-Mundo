import pygame
from pygame import MOUSEBUTTONDOWN

from TableroConceptual import Tablero
from Pieza import TipoPieza,TipoBando,Pieza
from proyecto.Pieza import Pieza

NEGRO = (0, 0, 0)
tablero_primario=Tablero()
pygame.init()
pantalla = pygame.display.set_mode((1050, 802))
reloj = pygame.time.Clock()
Terminar=False


def posicion_relativa(posicion: tuple[int, int]):
    x = posicion[0] * 100 + 2 - 99
    y = (9 - posicion[1]) * 100 + 2 - 99
    return (x, y)

def posicion_relativa_centrada(posicion: tuple[int, int]):
    x = posicion[0] * 100 + 2 - 99+50
    y = (9 - posicion[1]) * 100 + 2 - 99+50
    return (x, y)


def numero_relativo(posicion: tuple[int, int]):
    x = int((posicion[0] - 97) / 100 + 2)
    y = 9 - int(posicion[1] / 100 + 0.02 + 0.99)
    return (x, y)

def dibujar_tablero():

    imagen = "Imagenes\\Tablero.jpg"
    imp = pygame.image.load(imagen).convert()
    imp = pygame.transform.scale(imp, (802, 802))
    pantalla.blit(imp,(0,0))

def dibujar_posibles(posicion):
    a: Pieza=tablero_primario.encontrar_pieza(posicion)
    if a!=None:
        #print("tipo de pieza", a.tipo)
        la_posicion = tablero_primario.posibles_movimientos(a)
        if len(la_posicion) > 0:
            #print("comprobante",la_posicion)
            for b in la_posicion:
                posicion_a_dibujar = posicion_relativa_centrada(b)
                #print(posicion_a_dibujar)
                pygame.draw.circle(pantalla, (40,40,40), (posicion_a_dibujar), 8, 0)
                #print("posicion a posibles", b)



def dibujar_piezas():
    for a in tablero_primario.piezas:
        print(a.bando)
        if a.bando==TipoBando.BLANCO:
            print("comprobante")
            if a.tipo == TipoPieza.CABALLO:
                imagen = "Imagenes\\CaballoBlanco.png"
                print("otroooo")
            if a.tipo == TipoPieza.ALFIL:
                imagen = "Imagenes\\AlfilBlanco.png"
            if a.tipo == TipoPieza.REY:
                imagen = "Imagenes\\ReyBlanco.png"
            if a.tipo == TipoPieza.REINA:
                imagen = "Imagenes\\ReinaBlanca.png"
            if a.tipo == TipoPieza.TORRE:
                imagen = "Imagenes\\TorreBlanca.png"
            if a.tipo == TipoPieza.PEON:
                imagen = "Imagenes\\PeonBlanco.png"
        else:
           if a.tipo == TipoPieza.CABALLO:
               imagen = "Imagenes\\CaballoNegro.png"
           if a.tipo == TipoPieza.ALFIL:
               imagen = "Imagenes\\AlfilNegro.png"
           if a.tipo == TipoPieza.REY:
               imagen = "Imagenes\\ReyNegro.png"
           if a.tipo == TipoPieza.REINA:
               imagen = "Imagenes\\ReinaNegra.png"
           if a.tipo == TipoPieza.TORRE:
               imagen = "Imagenes\\TorreNegra.png"
           if a.tipo == TipoPieza.PEON:
               imagen = "Imagenes\\PeonNegro.png"

        imp = pygame.image.load(imagen).convert_alpha()
        imp = pygame.transform.scale(imp, (96, 96))
        p = posicion_relativa(a.posicion)
        pantalla.blit(imp, p)
pos=None
dibujar=True
#print(tablero_primario)
while not Terminar:

    for Evento in pygame.event.get():
        if Evento.type == pygame.QUIT:
            Terminar = True
        if Evento.type == MOUSEBUTTONDOWN:
            pos=numero_relativo(Evento.pos)
            dibujar=True

    if dibujar:
        dibujar=False
        dibujar_tablero()
        dibujar_piezas()
        if pos!=None:
            dibujar_posibles(pos)

    # ---Manejo de eventos

    #print(Evento.pos, " " ,pos)






    # --Todos los dibujos van después de esta línea




        # ---Código de dibujo----



    # --Todos los dibujos van antes de esta línea
    pygame.display.update()
    pygame.display.flip()
    reloj.tick(20)  # Limitamos a 20 fotogramas por segundo
pygame.quit()