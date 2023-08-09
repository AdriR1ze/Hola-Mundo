import pygame
#from menu import Menu
from pygame import MOUSEBUTTONDOWN, RESIZABLE, surface, display, transform
from bot import Bot
from Pieza import TipoPieza,TipoBando,Pieza
from TableroConceptual import Tablero
from pygame.locals import *
from pygame import *
import os
import sys
import threading

pos_inicial = None
pos_destino = None
bot=Bot()
CUADRADO=100
TAMANO=8*CUADRADO
pygame.init()

if (pygame.display.Info().current_w <= 800 or pygame.display.Info().current_h <= 800):
    TAMANO=min(pygame.display.Info().current_h - 100, pygame.display.Info().current_w - 100)
    CUADRADO=TAMANO/8
termino=0
tablero_tamano=(TAMANO, TAMANO)
NEGRO = (0, 0, 0)
tablero_primario=Tablero()
pantalla = pygame.display.set_mode(tablero_tamano)
reloj = pygame.time.Clock()
Terminar=False
posiewcion_ultimo_click=None
turno=TipoBando.BLANCO
pos=None
global dibuja
mover=0
global ultimo_seleccionado
ultimo_seleccionado=None
dibuja = True
bot_juega=True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)


def menu_inicial():

    def juego_principal():
        pos_inicial = None
        pos_destino = None
        bot = Bot()

        pygame.init()


        termino = 0

        NEGRO = (0, 0, 0)
        tablero_primario = Tablero()

        pantalla = pygame.display.set_mode((tablero_tamano[0] + 200, tablero_tamano[1]))
        reloj = pygame.time.Clock()
        Terminar = False
        posiewcion_ultimo_click = None
        turno = TipoBando.BLANCO
        pos = None
        global dibuja
        mover = 0
        global ultimo_seleccionado
        ultimo_seleccionado = None
        dibuja = True
        bot_juega = True

        print("Fen: ", tablero_primario.notacion_fen(turno))

        def resource_path(relative_path):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return os.path.join(os.path.abspath("."), relative_path)

        def posicion_relativa(posicion: tuple[int, int]):
            x = posicion[0] * tablero_tamano[0] / 8 - (tablero_tamano[0] / 8)
            y = (9 - posicion[1]) * tablero_tamano[0] / 8 + 2 - tablero_tamano[0] / 8 - 1
            return (x, y)

        def posicion_relativa_centrada(posicion: tuple[int, int]):
            x = posicion[0] * tablero_tamano[0] / 8 - CUADRADO + tablero_tamano[0] / 16
            y = (9 - posicion[1]) * tablero_tamano[0] / 8 + 2 - CUADRADO + tablero_tamano[0] / 16
            return (x, y)

        def dibujar_boton():
            imagen = resource_path("Imagenes\BotonMas.png")
            imp = pygame.image.load(imagen).convert()
            imp = pygame.transform.scale(imp, (tablero_tamano[0] / 8, tablero_tamano[1] / 8))
            pantalla.blit(imp, (500, 500))

        def numero_relativo(posicion: tuple[int, int]):
            x = int((posicion[0] - CUADRADO - 3) / CUADRADO + 2)
            y = 9 - int(posicion[1] / CUADRADO + 0.02 + 0.99)
            return (x, y)

        def dibujar_tablero():

            imagen = resource_path("Imagenes/Tablero.png")
            imp = pygame.image.load(imagen).convert()
            imp = pygame.transform.scale(imp, (tablero_tamano[0], tablero_tamano[1]))
            pantalla.blit(imp, (0, 0))

        def dibujar_posibles(posicion):
            a: Pieza = tablero_primario.encontrar_pieza(posicion)

            if a != None:
                if tablero_primario.tiene_jaque(turno) == False:
                    la_posicion = tablero_primario.posibles_movimientos_bien(a, turno)
                else:
                    la_posicion = tablero_primario.evitar_jaque(a, turno)

                if la_posicion != None and len(la_posicion) > 0:
                    # print("comprobante",la_posicion)
                    for b in la_posicion:
                        posicion_a_dibujar = posicion_relativa_centrada(b)
                        # print(posicion_a_dibujar)
                        pygame.draw.circle(pantalla, (40, 40, 40), (posicion_a_dibujar), CUADRADO / 12, 0)

        def salir_al_menu(boton_salir):
            pass

        def mover_pieza(pieza, posicion_nueva):

            if tablero_primario.puedo_comer(pieza, posicion_nueva) == True:
                tablero_primario.remover_pieza(tablero_primario.encontrar_pieza(posicion_nueva))
            pieza.posicion = posicion_nueva
            p11 = tablero_primario.encontrar_pieza((1, 1))
            p81 = tablero_primario.encontrar_pieza((8, 1))
            p18 = tablero_primario.encontrar_pieza((1, 8))
            p88 = tablero_primario.encontrar_pieza((8, 8))

            if pieza.tipo == TipoPieza.REY and pieza.movio == False and pieza.posicion == (
            3, 1) and p11 != None and p11.movio == False:
                p11.posicion = (4, 1)

            if pieza.tipo == TipoPieza.REY and pieza.movio == False and pieza.posicion == (
            7, 1) and p81 != None and p81.movio == False:
                p81.posicion = (6, 1)

            if pieza.tipo == TipoPieza.REY and pieza.movio == False and pieza.posicion == (
            7, 8) and p88 != None and p88.movio == False:
                p88.posicion = (6, 8)
            if pieza.tipo == TipoPieza.REY and pieza.movio == False and pieza.posicion == (
            3, 8) and p18 != None and p18.movio == False:
                p18.posicion = (4, 8)
            pieza.movio = True

            if tablero_primario.tiene_jaque(turno) == True:
                print("Hay jaque")

        def transformacion_de_coordenadas(letra):
            contador = 1
            if letra[0] == "a":
                contador = 1
            if letra[0] == "b":
                contador = 2
            if letra[0] == "c":
                contador = 3
            if letra[0] == "d":
                contador = 4

            if letra[0] == "e":
                contador = 5

            if letra[0] == "f":
                contador = 6

            if letra[0] == "g":
                contador = 7

            if letra[0] == "h":
                contador = 8

            return (contador, int(letra[1]))

        def dibujar_boton(posicion, tamanio, texto):
            # pygame.draw.rect(pantalla,(0,0,0),posicion,tamanio)
            # mostrar_texto(texto,posicion)
            return None

        def mostrar_texto(texto, pos_x, pos_y, color=(255, 255, 255), tamano_fuente=30):
            fuente = pygame.font.Font(None, tamano_fuente)
            superficie_texto = fuente.render(texto, True, color)
            pantalla.blit(superficie_texto, (pos_x, pos_y))

        def enviar_peticion():
            global turno
            if turno == TipoBando.NEGRO:
                best = bot.enviar_peticion(tablero_primario, turno)
                if best != None:
                    inicial = best[0] + best[1]
                    final = best[2] + best[3]
                    posicion_inicial = transformacion_de_coordenadas(inicial)
                    posicion_final = transformacion_de_coordenadas(final)
                    if tablero_primario.encontrar_pieza(posicion_inicial) != None:
                        print("moviendo pieza a: ", posicion_final)
                        print(tablero_primario.encontrar_pieza(posicion_inicial).bando,
                              tablero_primario.encontrar_pieza(posicion_inicial).tipo)

                        mover_pieza(tablero_primario.encontrar_pieza(posicion_inicial), posicion_final)
                        turno = cambiar_turno(turno)

                        global ultimo_seleccionado
                        ultimo_seleccionado = None
                        global dibuja
                        dibuja = True
                    else:
                        print("ERROR NO HAY PIEZA")
                else:
                    print("ERROR 404")

        def cambiar_turno(turno):
            if turno == TipoBando.BLANCO:
                turno = TipoBando.NEGRO
            else:
                turno = TipoBando.BLANCO
            return turno

        def dibujar_piezas():
            for a in tablero_primario.piezas:
                if a.bando == TipoBando.BLANCO:
                    # print("comprobante")
                    if a.tipo == TipoPieza.CABALLO:
                        imagen = resource_path("Imagenes/CaballoBlanco.png")
                        # print("otroooo")
                    if a.tipo == TipoPieza.ALFIL:
                        imagen = resource_path("Imagenes/AlfilBlanco.png")
                    if a.tipo == TipoPieza.REY:
                        imagen = resource_path("Imagenes/ReyBlanco.png")
                    if a.tipo == TipoPieza.REINA:
                        imagen = resource_path("Imagenes/ReinaBlanca.png")
                    if a.tipo == TipoPieza.TORRE:
                        imagen = resource_path("Imagenes/TorreBlanca.png")
                    if a.tipo == TipoPieza.PEON:
                        imagen = resource_path("Imagenes/PeonBlanco.png")
                else:
                    if a.tipo == TipoPieza.CABALLO:
                        imagen = resource_path("Imagenes/CaballoNegro.png")
                    if a.tipo == TipoPieza.ALFIL:
                        imagen = resource_path("Imagenes/AlfilNegro.png")
                    if a.tipo == TipoPieza.REY:
                        imagen = resource_path("Imagenes/ReyNegro.png")
                    if a.tipo == TipoPieza.REINA:
                        imagen = resource_path("Imagenes/ReinaNegra.png")
                    if a.tipo == TipoPieza.TORRE:
                        imagen = resource_path("Imagenes/TorreNegra.png")
                    if a.tipo == TipoPieza.PEON:
                        imagen = resource_path("Imagenes/PeonNegro.png")
                imp = pygame.image.load(imagen).convert_alpha()
                imp = pygame.transform.scale(imp, (CUADRADO, CUADRADO))
                p = posicion_relativa(a.posicion)
                pantalla.blit(imp, p)

        def dibujar_game_over(pantalla):

            imagen = resource_path("Imagenes\\PantallaNegra.png")
            imp = pygame.image.load(imagen).convert()
            imp = pygame.transform.scale(imp, (tablero_tamano[0], tablero_tamano[1]))
            pantalla.blit(imp, (0, 0))
            for a in tablero_primario.piezas:
                tablero_primario.remover_pieza(a)

        pantalla.fill((255, 255, 255))
        pygame.draw.rect(pantalla, (100, 100, 100), [710, 200, 150, 100])
        while not Terminar:
            for Evento in pygame.event.get():
                if Evento.type == pygame.QUIT:
                    Terminar = True
                if Evento.type == MOUSEBUTTONDOWN and Evento.button == 1:
                    boton = Rect(710, 200, 150, 100)
                    if boton.collidepoint(mouse.get_pos()):
                        pygame.draw.rect(pantalla, (200, 200, 150), [710, 200, 150, 100])

                    if turno == TipoBando.BLANCO:
                        antiturno = TipoBando.NEGRO
                    if turno == TipoBando.NEGRO:
                        antiturno = TipoBando.BLANCO
                    if tablero_primario.game_over(turno) == False:
                        pos = numero_relativo(Evento.pos)
                        if tablero_primario.encontrar_pieza(pos) != None and turno == tablero_primario.encontrar_pieza(
                                pos).bando:
                            ultimo_seleccionado = tablero_primario.encontrar_pieza(pos)
                            dibuja = True
                        elif ultimo_seleccionado != None:
                            if tablero_primario.tiene_jaque(turno) == False:
                                if pos in tablero_primario.posibles_movimientos_bien(ultimo_seleccionado, turno):
                                    mover_pieza(ultimo_seleccionado, pos)
                                    turno = cambiar_turno(turno)
                                    if bot_juega:
                                        x = threading.Thread(target=enviar_peticion)
                                        x.start()
                                    ultimo_seleccionado = None
                                    dibuja = True
                            else:
                                if pos in tablero_primario.evitar_jaque(ultimo_seleccionado, turno):
                                    mover_pieza(ultimo_seleccionado, pos)
                                    turno = cambiar_turno(turno)
                                    if bot_juega:
                                        x = threading.Thread(target=enviar_peticion)
                                        x.start()
                                    ultimo_seleccionado = None
                                    dibuja = True
                    else:

                        termino = 1
                        print("game over:", tablero_primario.game_over(turno))
                if Evento.type == MOUSEBUTTONDOWN and Evento.button == 3:
                    pos = numero_relativo(Evento.pos)
                    if tablero_primario.encontrar_pieza(pos) != None:
                        ultimo_seleccionado = tablero_primario.encontrar_pieza(pos)


                    elif ultimo_seleccionado != None:
                        mover_pieza(ultimo_seleccionado, pos)
                        ultimo_seleccionado = None
                        dibuja = True

            if dibuja == True and termino == 0:

                if pos == (tablero_tamano[0] / 8, tablero_tamano[1] / 8):
                    break

                dibuja = False
                dibujar_tablero()
                dibujar_piezas()
                if ultimo_seleccionado != None:
                    dibujar_posibles(ultimo_seleccionado.posicion)
            elif termino == 1:

                dibujar_game_over(pantalla)
                mostrar_texto(f"GAME OVER", 100, 200)
                mostrar_texto(f"EL GANADOR ES ----> EL BLANCO", 250, 100)

            pygame.display.update()
            pygame.display.flip()
            reloj.tick(20)  # Limitamos a 20 fotogramas por segundo
        pygame.quit()

    font = pygame.font.Font(None, 40)

    def dibujar_boton(posicion, color, texto, texto_color):
        pygame.draw.rect(pantalla, color, posicion)
        text_surface = font.render(texto, True, texto_color)
        text_rect = text_surface.get_rect(center=posicion.center)
        pantalla.blit(text_surface, text_rect)

    boton_posicion = Rect(300, 250, 200, 100)
    boton_color = GRAY

    pantalla.fill(GRAY)
    pygame.draw.rect(pantalla, (200, 200, 150), [300, 250, 200, 100])


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()



            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boton_posicion.collidepoint(mouse.get_pos()):
                    juego_principal()
                    return None

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_1]:
            juego_principal()

        pygame.display.flip()



pygame.display.update()
pygame.display.flip()
reloj.tick(20)  # Limitamos a 20 fotogramas por segundo

menu_inicial()
pygame.quit()