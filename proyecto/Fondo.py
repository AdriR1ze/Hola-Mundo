import pygame
from pygame import MOUSEBUTTONDOWN

from TableroConceptual import Tablero
from Pieza import TipoPieza,TipoBando,Pieza
from proyecto.Pieza import Pieza

NEGRO = (0, 0, 0)
tablero_primario=Tablero()
pygame.init()
pantalla = pygame.display.set_mode((802, 802))
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
    largo = 0
    altura = 0

    pantalla.fill((255, 255, 255))

    for a in range(8):
        largo = largo + 100
        pygame.draw.line(pantalla, (0, 0, 0), [largo, 0], [largo, 800], 2)

    for a in range(8):
        altura = altura + 100
        pygame.draw.line(pantalla, (0, 0, 0), [0, altura], [800, altura], 2)

    pygame.draw.line(pantalla, (0, 0, 0), [0, 0], [0, 800], 2)
    pygame.draw.line(pantalla, (0, 0, 0), [0, 800], [0, 800], 2)
    pygame.draw.line(pantalla, (0, 0, 0), [800, 0], [0, 0], 2)
    pygame.draw.line(pantalla, (0, 0, 0), [0, 800], [800, 800], 2)

def dibujar_posibles(posicion):
    a: Pieza=tablero_primario.encontrar_pieza(posicion)
    if a!=None:
        print("tipo de pieza", a.tipo)
        la_posicion = a.posibles_movimientos()
        if len(la_posicion) > 0:
            #print("comprobante",la_posicion)
            for b in la_posicion:
                posicion_a_dibujar = posicion_relativa_centrada(b)
                #print(posicion_a_dibujar)
                pygame.draw.circle(pantalla, NEGRO, (posicion_a_dibujar), 9, 8)
                #print("posicion a posibles", b)



def dibujar_piezas():
    for a in tablero_primario.piezas:
        if a.tipo == TipoPieza.CABALLO:
            imagen = "Imagenes\\CaballoNegro.png"
        if a.tipo == TipoPieza.ALFIL:
            imagen = "Imagenes\\CaballoNegro.png"
        if a.tipo == TipoPieza.REY:
            imagen = "Imagenes\\CaballoNegro.png"
        if a.tipo == TipoPieza.REINA:
            imagen = "Imagenes\\CaballoNegro.png"
        if a.tipo == TipoPieza.TORRE:
            imagen = "Imagenes\\CaballoNegro.png"
        if a.tipo == TipoPieza.PEON:
            imagen = "Imagenes\\PeonNegro.jpg"
        imp = pygame.image.load(imagen).convert()
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