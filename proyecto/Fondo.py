import pygame
from pygame import MOUSEBUTTONDOWN

from TableroConceptual import Tablero
from Pieza import TipoPieza,TipoBando,Pieza
tablero_primario=Tablero()
pygame.init()
Pantalla = pygame.display.set_mode((802,802))
reloj = pygame.time.Clock()
Terminar=False


def posicion_relativa(posicion: tuple[int, int]):
    x = posicion[0] * 100 + 2 - 99
    y = (9 - posicion[1]) * 100 + 2 - 99
    return (x, y)


def numero_relativo(posicion: tuple[int, int]):
    x = int((posicion[0] - 97) / 100 + 2)
    y = int(posicion[1] / 100 - 0.9 + 0.02 + 0.99 + 1)
    return (x, y)


#print(tablero_primario)
while not Terminar:
    # ---Manejo de eventos
    for Evento in pygame.event.get():
        if Evento.type == pygame.QUIT:
            Terminar = True
        if Evento.type == MOUSEBUTTONDOWN:
            pos=numero_relativo(Evento.pos)
            print(Evento.pos, " " ,pos)

    # ---La lógica del juego

    ListaDeColumnas = [1, 2, 3, 4, 5, 6, 7, 8]
    ListaDeFilas = [1, 2, 3, 4, 5, 6, 7, 8]
    largo=0
    altura=0
    NEGRO=(0,0,0)



    # ---Código de dibujo----
    Pantalla.fill((255,255,255))


    # --Todos los dibujos van después de esta línea

    for a in tablero_primario.piezas:
        if a.tipo == TipoPieza.CABALLO:
            imagen="Imagenes\\CaballoNegro.png"
        if a.tipo==TipoPieza.ALFIL:
            imagen="Imagenes\\CaballoNegro.png"
        if a.tipo==TipoPieza.REY:
            imagen="Imagenes\\CaballoNegro.png"
        if a.tipo==TipoPieza.REINA:
            imagen="Imagenes\\CaballoNegro.png"
        if a.tipo==TipoPieza.TORRE:
            imagen="Imagenes\\CaballoNegro.png"
        if a.tipo==TipoPieza.PEON:
            imagen="Imagenes\\PeonNegro.jpg"
        imp = pygame.image.load(imagen).convert()
        imp = pygame.transform.scale(imp, (96, 96))
        p = posicion_relativa(a.posicion)
        Pantalla.blit(imp, p)
        try:
            #if a.posicion==numero_relativo(pos):
                #la_posicion=a.posibles_movimientos()
                #pygame.draw.line(Pantalla, (0, 0, 0), [la_posicion], [100, 500], 2)
        except NameError:
            pass

    for a in range(8):
        largo = largo + 100
        pygame.draw.line(Pantalla, (0, 0, 0), [largo, 0], [largo, 800], 2)

    for a in range(8):
        altura = altura + 100
        pygame.draw.line(Pantalla, (0, 0, 0), [0, altura], [800, altura], 2)

    pygame.draw.line(Pantalla, (0, 0, 0), [0, 0], [0, 800], 2)
    pygame.draw.line(Pantalla, (0, 0, 0), [0, 800], [0, 800], 2)
    pygame.draw.line(Pantalla, (0, 0, 0), [800, 0], [0, 0], 2)
    pygame.draw.line(Pantalla, (0, 0, 0), [0, 800], [800, 800], 2)



    # --Todos los dibujos van antes de esta línea
    pygame.display.update()
    pygame.display.flip()
    reloj.tick(20)  # Limitamos a 20 fotogramas por segundo
pygame.quit()