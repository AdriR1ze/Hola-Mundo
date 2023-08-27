import pygame
import pygame_menu
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
pantalla = pygame.display.set_mode((tablero_tamano[0]+200,tablero_tamano[1]))
reloj = pygame.time.Clock()
Terminar=False
posiewcion_ultimo_click=None
turno=TipoBando.BLANCO
pos=None
global dibuja
mover=0
global dificultad
dificultad=0
global quien_juega
quien_juega=TipoBando.NEGRO
global ultimo_seleccionado
ultimo_seleccionado=None
dibuja = True

bot_juega=True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
global mostrar

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
def menu_de_inicio():
    menu = pygame_menu.Menu('Ajedrez', 400,300,theme=pygame_menu.themes.THEME_GREEN)
    menu.add.button('Jugar', menu_de_eleccion)
    menu.add.button('Salir', pygame_menu.events.EXIT)
    pantalla.fill((128, 0, 0))
    menu.mainloop(pantalla)
def cambiar_dificultad(valor,dificulta):
    global dificultad
    dificultad=valor
def menu_de_eleccion():
    menu_de_eleccion = pygame_menu.Menu('Ajedrez', 400, 300, theme=pygame_menu.themes.THEME_DARK)
    menu_de_eleccion.add.button('1 Jugador', menu_un_jugador)
    menu_de_eleccion.add.button('2 Jugadores', menu_dos_jugadores)
    menu_de_eleccion.add.button('Atras', menu_de_inicio)
    menu_de_eleccion.mainloop(pantalla)
def menu_un_jugador():
    menu_de_un_jugador = pygame_menu.Menu('Ajedrez', 400, 300, theme=pygame_menu.themes.THEME_DARK)
    menu_de_un_jugador.add.selector('Elija:',[('Blanco', TipoBando.BLANCO),('Negro', TipoBando.NEGRO)], onchange=elegir_bando)
    menu_de_un_jugador.add.selector('Dificultad :',[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8),('9', 9)], onchange=cambiar_dificultad)
    menu_de_un_jugador.add.button('Empezar Partida', juego_principal)
    menu_de_un_jugador.add.button('Atras', menu_de_eleccion)
    menu_de_un_jugador.mainloop(pantalla)
def elegir_bando(valor, bando):
    global quien_juega
    if valor==TipoBando.BLANCO:
        quien_juega=TipoBando.NEGRO
    else:
        quien_juega=TipoBando.BLANCO
def menu_dos_jugadores():
    global bot_juega
    bot_juega=False
    juego_principal()
def juego_principal():
    puntos_negras = 0
    puntos_blancas = 0
    bot = Bot()
    termino = 0
    NEGRO = (0, 0, 0)
    tablero_primario = Tablero()
    pantalla = pygame.display.set_mode((tablero_tamano[0]+200, tablero_tamano[1]))
    reloj = pygame.time.Clock()
    Terminar = False
    global turno
    turno = TipoBando.BLANCO
    pos = None
    global dibuja
    global ultimo_seleccionado
    ultimo_seleccionado = None
    dibuja = True
    def posicion_relativa(posicion: tuple[int, int]):

        x = posicion[0] * tablero_tamano[0] / 8 - (tablero_tamano[0] / 8)
        y = (9 - posicion[1]) * tablero_tamano[0] / 8 + 2 - tablero_tamano[0] / 8 - 1
        if posicion[0]>8 or posicion[0]<1 or posicion[1]>8 or posicion[1]<1:
            print("MAL")
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
                for b in la_posicion:
                    posicion_a_dibujar = posicion_relativa_centrada(b)
                    pygame.draw.circle(pantalla, (40, 40, 40), (posicion_a_dibujar), CUADRADO / 12, 0)

    def salir_al_menu(boton_salir):
        pass

    def mover_pieza(pieza, posicion_nueva):

        if tablero_primario.puedo_comer(pieza, posicion_nueva) == True:
            piezas_comidas(tablero_primario.encontrar_pieza(posicion_nueva),tablero_primario.encontrar_pieza(posicion_nueva).bando)
            dibujar_piezas_comidas(tablero_primario.encontrar_pieza(posicion_nueva))
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
    def mostrar_texto(texto, pos_x, pos_y, color=(255, 255, 255), tamano_fuente=30):
        fuente = pygame.font.Font(None, tamano_fuente)
        superficie_texto = fuente.render(texto, True, color)
        pantalla.blit(superficie_texto, (pos_x, pos_y))

    def enviar_peticion():

        global turno
        if quien_juega==TipoBando.NEGRO and turno == TipoBando.NEGRO:
            best = bot.enviar_peticion(tablero_primario, turno, dificultad,quien_juega)
        elif quien_juega==TipoBando.BLANCO and turno==TipoBando.BLANCO:
            best = bot.enviar_peticion(tablero_primario, turno, dificultad, quien_juega)
        #print(best)
        if best != None and len(best)==4:
            inicial = best[0] + best[1]
            final = best[2] + best[3]
            posicion_inicial = transformacion_de_coordenadas(inicial)
            posicion_final = transformacion_de_coordenadas(final)
            if tablero_primario.encontrar_pieza(posicion_inicial) != None:
                mover_pieza(tablero_primario.encontrar_pieza(posicion_inicial), posicion_final)
                turno = cambiar_turno(turno)
                global ultimo_seleccionado
                ultimo_seleccionado = None
                global dibuja
                dibuja = True
    def cambiar_turno(turno):
        if turno == TipoBando.BLANCO:
            turno = TipoBando.NEGRO
        else:
            turno = TipoBando.BLANCO
        return turno

    def dibujar_piezas():
        for a in tablero_primario.piezas:
            if a.bando == TipoBando.BLANCO:
                if a.tipo == TipoPieza.CABALLO:
                    imagen = resource_path("Imagenes/CaballoBlanco.png")
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

    font = pygame.font.Font(None, 36)
    def dibujar_bien_boton(posicion, color, texto, texto_color):
        pygame.draw.rect(pantalla, color, posicion)
        text_surface = font.render(texto, True, texto_color)
        text_rect = text_surface.get_rect(center=posicion.center)
        pantalla.blit(text_surface, text_rect)
    def dibujar_game_over(pantalla):
        imagen = resource_path("Imagenes\\Buena 1.png")
        imp = pygame.image.load(imagen).convert()
        imp = pygame.transform.scale(imp, (tablero_tamano[0]+225, tablero_tamano[1]))
        pantalla.blit(imp, (0, 0))
        for a in tablero_primario.piezas:
            tablero_primario.remover_pieza(a)
    if quien_juega==TipoBando.BLANCO:
        x = threading.Thread(target=enviar_peticion)
        x.start()

    def piezas_comidas(pieza, bando):
        global lista_de_piezas_comidas_blancas
        lista_de_piezas_comidas_blancas = []
        global lista_de_piezas_comidas_negras
        lista_de_piezas_comidas_negras = []
        if bando==TipoBando.BLANCO:
            lista_de_piezas_comidas_blancas.append(pieza)
        else:
            lista_de_piezas_comidas_negras.append(pieza)

    def dibujar_piezas_comidas(pieza):
        #puntos_blancas=lista_de_piezas_comidas
        pantalla.fill((41, 36, 33))
        if pieza in lista_de_piezas_comidas:
            if pieza.bando == TipoBando.BLANCO:
                if pieza.tipo == TipoPieza.CABALLO:
                   # global puntos_negras
                    #puntos_negras=puntos_negras+3
                    imagen = resource_path("Imagenes/CaballoBlanco.png")
                if pieza.tipo == TipoPieza.ALFIL:
                   # global puntos_negras
                    #puntos_negras = puntos_negras + 3
                    imagen = resource_path("Imagenes/AlfilBlanco.png")
                if pieza.tipo == TipoPieza.REY:
                    imagen = resource_path("Imagenes/ReyBlanco.png")
                if pieza.tipo == TipoPieza.REINA:
                  #  global puntos_negras
                    #puntos_negras = puntos_negras + 9
                    imagen = resource_path("Imagenes/ReinaBlanca.png")
                if pieza.tipo == TipoPieza.TORRE:
                  #  global puntos_negras
                   # puntos_negras = puntos_negras + 5
                    imagen = resource_path("Imagenes/TorreBlanca.png")
                if pieza.tipo == TipoPieza.PEON:
                #    global puntos_negras
                   # puntos_negras = puntos_negras + 1
                    imagen = resource_path("Imagenes/PeonBlanco.png")
            else:
                if pieza.tipo == TipoPieza.CABALLO:
                  #  global puntos_blancas
                    #puntos_blancas = puntos_blancas + 3
                    imagen = resource_path("Imagenes/CaballoNegro.png")
                if pieza.tipo == TipoPieza.ALFIL:
                    #global puntos_blancas
                    #puntos_blancas = puntos_blancas + 3
                    imagen = resource_path("Imagenes/AlfilNegro.png")
                if pieza.tipo == TipoPieza.REY:
                    imagen = resource_path("Imagenes/ReyNegro.png")
                if pieza.tipo == TipoPieza.REINA:
                  #  global puntos_blancas
                    #puntos_blancas = puntos_blancas + 9
                    imagen = resource_path("Imagenes/ReinaNegra.png")
                if pieza.tipo == TipoPieza.TORRE:
                  #  global puntos_blancas
                   # puntos_blancas = puntos_blancas + 5
                    imagen = resource_path("Imagenes/TorreNegra.png")
                if pieza.tipo == TipoPieza.PEON:
                   # global puntos_blancas
                    #puntos_blancas = puntos_blancas + 1
                    imagen = resource_path("Imagenes/PeonNegro.png")
            imp = pygame.image.load(imagen).convert_alpha()
            imp = pygame.transform.scale(imp, (60, 60))
            if puntos_negras>puntos_blancas:
                puntos_mostrados=puntos_negras-puntos_blancas
            elif puntos_blancas>puntos_negras:
                puntos_mostrados=puntos_blancas-puntos_negras
            else:
                puntos_mostrados=0
            if pieza.bando == TipoBando.BLANCO:
                if puntos_mostrados!=0:
                    mostrar_texto(f"+{puntos_mostrados}",810,20)
                p = (820, 20)
            else:
                if puntos_mostrados != 0:
                    mostrar_texto(f"+{puntos_mostrados}",810,700)
                p = (820, 700)

            pantalla.blit(imp, p)
    def salir_menu():
        menu_de_inicio()

    def reiniciar_juego():
        juego_principal()

    #new_partida_bot = Rect(810, 250, 180, 100)
    pantalla.fill((41, 36, 33))
    #dibujar_bien_boton(new_partida_bot, (150,150,150), "Nueva Partida", BLACK)

    menu_bot = Rect(810, 450, 180, 100)
    dibujar_bien_boton(menu_bot, (150,150,150), "Salir al Menu", BLACK)
    while not Terminar:

        for Evento in pygame.event.get():
            if turno == TipoBando.BLANCO:
                antiturno = TipoBando.NEGRO
            if turno == TipoBando.NEGRO:
                antiturno = TipoBando.BLANCO
            if Evento.type == pygame.QUIT:
                Terminar = True
            if Evento.type == MOUSEBUTTONDOWN and Evento.button == 1:
                if menu_bot.collidepoint(mouse.get_pos()):
                    turno = antiturno
                    salir_menu()

                #if new_partida_bot.collidepoint(mouse.get_pos()):
                    #turno=antiturno
                    #reiniciar_juego()



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
                                if bot_juega==True:
                                    x = threading.Thread(target=enviar_peticion)
                                    x.start()
                                ultimo_seleccionado = None
                                dibuja = True
                        else:
                            if pos in tablero_primario.evitar_jaque(ultimo_seleccionado, turno):
                                mover_pieza(ultimo_seleccionado, pos)
                                turno = cambiar_turno(turno)
                                if bot_juega==True:
                                    x = threading.Thread(target=enviar_peticion)
                                    x.start()
                                ultimo_seleccionado = None
                                dibuja = True
                else:
                    termino = 1
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
        pygame.display.update()
        pygame.display.flip()
        reloj.tick(20)

    pygame.quit()
menu_de_inicio()
