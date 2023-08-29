import time as t
#import multiprocessing
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
bot=Bot()
#Tamaño de cada cuadrado del tablero
CUADRADO=100
#Tamaño del tablero
TAMANO=8*CUADRADO
pygame.init()
#En el caso de que la resolucion del usuario sea menor que 800x800 seteamos el tamaño del tablero al tamaño de la resolucion del usuario - 100
if (pygame.display.Info().current_w <= 800 or pygame.display.Info().current_h <= 800):
    TAMANO=min(pygame.display.Info().current_h - 100, pygame.display.Info().current_w - 100)
    CUADRADO=TAMANO/8
termino=0
tablero_tamano=(TAMANO, TAMANO)
NEGRO = (0, 0, 0)
#Creamos el objeto "Tablero"
tablero_primario=Tablero()
#Creamos la pantalla, y le damos sus medidas
pantalla = pygame.display.set_mode((tablero_tamano[0]+200,tablero_tamano[1]))
reloj = pygame.time.Clock()
Terminar=False
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
global thread_enviar
thread_enviar=None
corona=False
posicion_coronacion=None
coronacion_rectangulo = None

#Le agrega al path relativo el directorio meipass, es una variable de entorno que contiene el path del directorio donde va a estar descomprimido el programa cuando se ejecuta el instalador

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
#Crea el menu inicial
def menu_de_inicio():
    menu = pygame_menu.Menu('Ajedrez', 400,300,theme=pygame_menu.themes.THEME_GREEN)
    menu.add.button('Jugar', menu_de_eleccion)
    menu.add.button('Salir', pygame_menu.events.EXIT)
    pantalla.fill((128, 0, 0))
    menu.mainloop(pantalla)
#Crea el menu en donde se elije el modo de juego
def menu_de_eleccion():
    menu_de_eleccion = pygame_menu.Menu('Ajedrez', 400, 300, theme=pygame_menu.themes.THEME_DARK)
    menu_de_eleccion.add.button('1 Jugador', menu_un_jugador)
    menu_de_eleccion.add.button('2 Jugadores', menu_dos_jugadores)
    menu_de_eleccion.add.button('Atras', menu_de_inicio)
    menu_de_eleccion.mainloop(pantalla)
#Crea el menu en el caso de que hayas elegido un solo jugador
def menu_un_jugador():
    menu_de_un_jugador = pygame_menu.Menu('Ajedrez', 400, 300, theme=pygame_menu.themes.THEME_DARK)
    menu_de_un_jugador.add.selector('Elija:',[('Blanco', TipoBando.BLANCO),('Negro', TipoBando.NEGRO)], onchange=elegir_bando)
    menu_de_un_jugador.add.selector('Dificultad :',[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8),('9', 9)], onchange=cambiar_dificultad)
    menu_de_un_jugador.add.button('Empezar Partida', juego_principal)
    menu_de_un_jugador.add.button('Atras', menu_de_eleccion)
    menu_de_un_jugador.mainloop(pantalla)
#Es la funcion que contiene la dificultad elegida
def cambiar_dificultad(valor,dificulta):
    global dificultad
    dificultad=valor
#Es la funcion que permite saber a que bando pertenece el bot
def elegir_bando(valor, bando):
    global quien_juega
    if valor==TipoBando.BLANCO:
        quien_juega=TipoBando.NEGRO
    else:
        quien_juega=TipoBando.BLANCO
#Deshabilita el bot y empieza el juego
def menu_dos_jugadores():
    global bot_juega
    bot_juega=False
    juego_principal()
#La funcion que empieza el juego
def juego_principal():
    global thread_enviar
    global corona
    corona=False
    global coronacion_rectangulo
    coronacion_rectangulo = None
    thread_enviar = None
    enviando=False
    reinicar_toco=False
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
    global posicion_n
    posicion_n=None
    tablas=False
    global posicion_coronacion
    #Calcula dada una posicion teorica de un tablero, y la transforma a una posicion real en la pantalla
    def posicion_relativa(posicion: tuple[int, int]):

        x = posicion[0] * tablero_tamano[0] / 8 - (tablero_tamano[0] / 8)
        y = (9 - posicion[1]) * tablero_tamano[0] / 8 + 2 - tablero_tamano[0] / 8 - 1
        if posicion[0]>8 or posicion[0]<1 or posicion[1]>8 or posicion[1]<1:
            print("MAL")
        return (x, y)
    #Hace lo mismo que la funcion posicion relativa, pero centrado
    def posicion_relativa_centrada(posicion: tuple[int, int]):
        x = posicion[0] * tablero_tamano[0] / 8 - CUADRADO + tablero_tamano[0] / 16
        y = (9 - posicion[1]) * tablero_tamano[0] / 8 + 2 - CUADRADO + tablero_tamano[0] / 16
        return (x, y)
    #Transforma una posicion real en la pantalla a una coordenada teorica en el tablero
    def numero_relativo(posicion: tuple[int, int]):
        x = int((posicion[0] - CUADRADO - 3) / CUADRADO + 2)
        y = 9 - int(posicion[1] / CUADRADO + 0.02 + 0.99)
        return (x, y)
    #Dibuja el tablero
    def dibujar_tablero():

        imagen = resource_path("Imagenes/Tablero.png")
        imp = pygame.image.load(imagen).convert()
        imp = pygame.transform.scale(imp, (tablero_tamano[0], tablero_tamano[1]))
        pantalla.blit(imp, (0, 0))

    #Dibuja los posibles movimientos de una pieza
    def dibujar_posibles(posicion):
        a: Pieza = tablero_primario.encontrar_pieza(posicion)
        print("dibujar posibles: ", turno)
        if a != None:
            if tablero_primario.tiene_jaque(turno) == False:
                print("no hay jaque")
                la_posicion = tablero_primario.posibles_movimientos_bien(a, turno)
            else:
                la_posicion = tablero_primario.evitar_jaque(a, turno)

            if la_posicion != None and len(la_posicion) > 0:
                for b in la_posicion:
                    posicion_a_dibujar = posicion_relativa_centrada(b)
                    pygame.draw.circle(pantalla, (40, 40, 40), (posicion_a_dibujar), CUADRADO / 12, 0)
    #Dibuja todas las piezas en el tablero
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
    #Dibuja las posibles piezas a elegir, cuando se corona a un peon
    def dibujar_coronacion(posicion, color, taman, turno):

        if turno == TipoBando.NEGRO:
            global posicion_n
            posicion_n = posicion_relativa((posicion[0], posicion[1]))
            print("posicion nueva", posicion_n)
            global coronacion_rectangulo
            coronacion_rectangulo = pygame.Rect(posicion_n[0], posicion_n[1]-(tablero_tamano[0]/8)*3, taman[0], taman[1])
            print("Rectangulo", coronacion_rectangulo)
            pygame.draw.rect(pantalla, color, coronacion_rectangulo, 0, 5)
            imagen = resource_path("Imagenes/AlfilNegro.png")
            imp = pygame.image.load(imagen).convert_alpha()
            imp = pygame.transform.scale(imp, (tablero_tamano[0] / 8, (tablero_tamano[0] / 8)))
            pantalla.blit(imp, (posicion_n[0],posicion_n[1]-(tablero_tamano[0]/8)*3))
            imagen = resource_path("Imagenes/TorreNegra.png")
            imp = pygame.image.load(imagen).convert_alpha()
            imp = pygame.transform.scale(imp, (tablero_tamano[0] / 8, (tablero_tamano[0] / 8)))
            pantalla.blit(imp, (posicion_n[0],posicion_n[1]-(tablero_tamano[0]/8)*3 + int(tablero_tamano[0] / 16) + 47))
            imagen = resource_path("Imagenes/CaballoNegro.png")
            imp = pygame.image.load(imagen).convert_alpha()
            imp = pygame.transform.scale(imp, (tablero_tamano[0] / 8, (tablero_tamano[0] / 8) + 10))
            pantalla.blit(imp, (posicion_n[0],posicion_n[1]-(tablero_tamano[0]/8)*3 + int((tablero_tamano[0] / 16) * 2) + 92))
            imagen = resource_path("Imagenes/ReinaNegra.png")
            imp = pygame.image.load(imagen).convert_alpha()
            imp = pygame.transform.scale(imp, (tablero_tamano[0] / 8, (tablero_tamano[0] / 8)))
            pantalla.blit(imp, (posicion_n[0],posicion_n[1]-(tablero_tamano[0]/8)*3 + int((tablero_tamano[0] / 16) * 3) + 145))
        else:
            posicion_n = posicion_relativa((posicion[0], posicion[1]))
            print("posicion nueva", posicion_n)
            coronacion_rectangulo = pygame.Rect(posicion_n[0], posicion_n[1], taman[0], taman[1])
            print("Rectangulo", coronacion_rectangulo)
            pygame.draw.rect(pantalla, color, coronacion_rectangulo,0,5)
            imagen = resource_path("Imagenes/ReinaBlanca.png")
            imp = pygame.image.load(imagen).convert_alpha()
            imp = pygame.transform.scale(imp, (tablero_tamano[0] / 8, (tablero_tamano[0] / 8)))
            pantalla.blit(imp, posicion_n)
            imagen = resource_path("Imagenes/CaballoBlanco.png")
            imp = pygame.image.load(imagen).convert_alpha()
            imp = pygame.transform.scale(imp, (tablero_tamano[0] / 8, (tablero_tamano[0] / 8)))
            pantalla.blit(imp, (posicion_n[0],posicion_n[1] + int(tablero_tamano[0] / 16) + 47))
            imagen = resource_path("Imagenes/TorreBlanca.png")
            imp = pygame.image.load(imagen).convert_alpha()
            imp = pygame.transform.scale(imp, (tablero_tamano[0] / 8, (tablero_tamano[0] / 8) + 10))
            pantalla.blit(imp, (posicion_n[0],posicion_n[1] + int((tablero_tamano[0] / 16) * 2) + 92))
            imagen = resource_path("Imagenes/AlfilBlanco.png")
            imp = pygame.image.load(imagen).convert_alpha()
            imp = pygame.transform.scale(imp, (tablero_tamano[0] / 8, (tablero_tamano[0] / 8)))
            pantalla.blit(imp, (posicion_n[0],posicion_n[1] + int((tablero_tamano[0] / 16) * 3) + 145))
    #Determina a que pieza se va a coronar el peon
    def pieza_elegida_al_coronar(pos_y,turno):
        if turno==TipoBando.BLANCO:
            if pos_y <= tablero_tamano[1]/8:
                return TipoPieza.REINA
            elif pos_y <= tablero_tamano[1]/8 * 2:
                return TipoPieza.CABALLO
            elif pos_y <= tablero_tamano[1]/8 * 3:
                return TipoPieza.TORRE
            elif pos_y <= tablero_tamano[1]/8 * 4:
                return TipoPieza.ALFIL
        else:
            if pos_y <= tablero_tamano[1]/8:
                return TipoPieza.ALFIL
            elif pos_y <= tablero_tamano[1]/8 * 2:
                return TipoPieza.TORRE
            elif pos_y <= tablero_tamano[1]/8 * 3:
                return TipoPieza.CABALLO
            elif pos_y <= tablero_tamano[1]/8 * 4:
                return TipoPieza.REINA
    #Es la funcion que mueve las piezas
    def mover_pieza(pieza, posicion_nueva,turno):
        if pieza.tipo==TipoPieza.PEON and (posicion_nueva[1]==8 or posicion_nueva[1]==1) and (tablero_primario.puedo_comer(pieza, posicion_nueva) == True or tablero_primario.encontrar_pieza(posicion_nueva) == None):
            global corona
            corona=True
            global posicion_coronacion
            posicion_coronacion=posicion_nueva
            print(posicion_coronacion)


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
    #Es la funcion que usamos para transformar las jugadas que nos da el bot, a coordenadas que podamos utilizar dentro del codigo
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
    #Envia la peticion de jugada al bot
    def enviar_peticion():
        global enviando
        enviando=True
        try:
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
                    mover_pieza(tablero_primario.encontrar_pieza(posicion_inicial), posicion_final,turno)
                    turno = cambiar_turno(turno)
                    global ultimo_seleccionado
                    ultimo_seleccionado = None
                    global dibuja
                    dibuja = True
        finally:
            enviando=False
    #Cambia el turno de la partida
    def cambiar_turno(turno):
        if turno == TipoBando.BLANCO:
            turno = TipoBando.NEGRO
        else:
            turno = TipoBando.BLANCO
        return turno



    #Dibuja botones
    def dibujar_boton(posicion, color, texto, texto_color):

        pygame.draw.rect(pantalla, color, posicion, 0 , 5)
        pygame.draw.rect(pantalla, (100, 100, 100), (posicion[0]+2, posicion[1]+2, posicion[2]-4, posicion[3]-4), 0 , 5)

        text_surface = font.render(texto, True, texto_color)
        text_rect = text_surface.get_rect(center=posicion.center)
        pantalla.blit(text_surface, text_rect)

    #Dibuja en caso de que sea game over
    def dibujar_game_over(pantalla):
        imagen = resource_path("Imagenes/Buena_1.png")
        imp = pygame.image.load(imagen).convert()
        imp = pygame.transform.scale(imp, (tablero_tamano[0]+225, tablero_tamano[1]))
        pantalla.blit(imp, (0, 0))
        for a in tablero_primario.piezas:
            tablero_primario.remover_pieza(a)
    #Vuelve al menu inicial
    def salir_menu():
        menu_de_inicio()

    #Reinicia el juego
    def reiniciar_juego():
        juego_principal()

    #Se crean los botones de nueva partida y salir al menu
    #font = pygame.font.Font(None, int( CUADRADO * 30.0/100.0))
    font=pygame.font.SysFont("FreeMono, Monospace", 20)
    new_partida_bot = Rect(810, 250, 180, 100)
    pantalla.fill((41, 36, 33))
    dibujar_boton(new_partida_bot, (150,150,150), "Nueva Partida", BLACK)

    menu_bot = Rect(810, 450, 180, 100)
    dibujar_boton(menu_bot, (150,150,150), "Salir al Menu", BLACK)
    #En caso de que en el menu se haya elegido un jugador y que vos seas del bando negro, el bot hace una jugada
    if quien_juega==TipoBando.BLANCO:
        thread_enviar = threading.Thread(target=enviar_peticion)
        thread_enviar.start()

    #Empieza el bucle
    while not Terminar:
        #Itera por todos los eventos que ocurren
        for Evento in pygame.event.get():
            #En caso de cerrar la aplicacion, se cambia el valor de la variable Terminar
            if Evento.type == pygame.QUIT:
                Terminar = True
            #Pregunta si tocaste el click izquierdo
            if Evento.type == MOUSEBUTTONDOWN and Evento.button == 1:
                if menu_bot.collidepoint(mouse.get_pos()):
                    salir_menu()

                if new_partida_bot.collidepoint(mouse.get_pos()):
                    reiniciar_juego()
                if corona == True:
                    #Pregunta si toco el cuadrado de la coronacion y en donde
                    if coronacion_rectangulo.collidepoint(mouse.get_pos()):
                        pieza_elegida = pieza_elegida_al_coronar(mouse.get_pos()[1] - coronacion_rectangulo[1],turno)
                        tablero_primario.coronacion(ultimo_seleccionado, pieza_elegida)
                        corona=False
                        ultimo_seleccionado=None
                        dibuja=True
                        coronacion_rectangulo=None
                        posicion_n=None
                        turno = cambiar_turno(turno)
                    continue
                #Pregunta si es game over
                if tablero_primario.game_over(turno) == False:
                    #Obtiene la posicion del mouse
                    pos = numero_relativo(Evento.pos)
                    #Seleccionar una pieza
                    if tablero_primario.encontrar_pieza(pos) != None and turno == tablero_primario.encontrar_pieza(
                            pos).bando:
                        ultimo_seleccionado = tablero_primario.encontrar_pieza(pos)
                        dibuja = True
                    #Mover pieza seleccionada
                    elif ultimo_seleccionado != None:
                        #Caso en donde no hay jaque
                        if tablero_primario.tiene_jaque(turno) == False:
                            if pos in tablero_primario.posibles_movimientos_bien(ultimo_seleccionado, turno):
                                mover_pieza(ultimo_seleccionado, pos,turno)

                                if corona==False:
                                    turno = cambiar_turno(turno)
                                print("Movi, cheque tablas")
                                if tablero_primario.tablas(turno)==True:
                                    print("TABLAS")
                                    tablas=True
                                #Envia la peticion al bot, en otro thread, para no dejar clavado el actual
                                if bot_juega==True:
                                    thread_enviar = threading.Thread(target=enviar_peticion)
                                    thread_enviar.start()
                                if corona==False:
                                    ultimo_seleccionado = None
                                dibuja = True
                        #Caso en donde hay jaque
                        else:
                            if pos in tablero_primario.evitar_jaque(ultimo_seleccionado, turno):
                                mover_pieza(ultimo_seleccionado, pos,turno)
                                if corona==False:
                                    turno = cambiar_turno(turno)
                                print("Movi, cheque2 tablas")
                                if tablero_primario.tablas(turno) == True:
                                    print("TABLAS")
                                    tablas = True
                                if bot_juega==True:
                                    thread_enviar = threading.Thread(target=enviar_peticion)
                                    thread_enviar.start()

                                ultimo_seleccionado = None
                                dibuja = True
                else:
                    termino = 1
            #Esta parte del codigo es para mover libremente las piezas, y poder debuggear con mayor comodidad el codigo
            if Evento.type == MOUSEBUTTONDOWN and Evento.button == 3:
                pos = numero_relativo(Evento.pos)
                if tablero_primario.encontrar_pieza(pos) != None:
                    ultimo_seleccionado = tablero_primario.encontrar_pieza(pos)
                elif ultimo_seleccionado != None:
                    mover_pieza(ultimo_seleccionado, pos,turno)
                    ultimo_seleccionado = None
                    dibuja = True
        #Dibuja todas las cosas necesarias si no hay jaque mate o tablas
        if dibuja == True and termino == 0:
            if pos == (tablero_tamano[0] / 8, tablero_tamano[1] / 8):
                break

            dibuja = False
            dibujar_tablero()
            dibujar_piezas()
            print("Corona para printear", corona, posicion_coronacion)
            if corona==True:
                dibujar_coronacion(posicion_coronacion, (255, 255, 255), (tablero_tamano[0] / 8, (tablero_tamano[0] / 8) * 4), turno)

            if ultimo_seleccionado != None:
                dibujar_posibles(ultimo_seleccionado.posicion)

            turno_de_bot = Rect(806, 100, 187, 50)
            if turno == TipoBando.BLANCO:
                dibujar_boton(turno_de_bot, (255, 255, 255), "Turno: BLANCO", BLACK)
            else:
                dibujar_boton(turno_de_bot, (255, 255, 255), "Turno: NEGRO ", BLACK)
            if tablas==True:
                termino=1
        #Dibuja en caso de jaque mate o tablas
        elif termino == 1:
            if tablas==False:
                t.sleep(0.7)
                dibujar_game_over(pantalla)
            else:
                t.sleep(0.7)
                dibujar_game_over(pantalla)
        pygame.display.update()
        pygame.display.flip()
        reloj.tick(20)

    pygame.quit()
#Inicia el programa
menu_de_inicio()
