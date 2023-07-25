import pygame
#from menu import Menu
from pygame import MOUSEBUTTONDOWN, RESIZABLE, surface
from bot import Bot
from Pieza import TipoPieza,TipoBando,Pieza
from TableroConceptual import Tablero
from pygame.locals import *
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

tablero_tamano=(TAMANO, TAMANO)
NEGRO = (0, 0, 0)
tablero_primario=Tablero()
pantalla = pygame.display.set_mode(tablero_tamano)
reloj = pygame.time.Clock()
Terminar=False
posicion_ultimo_click=None
turno=TipoBando.BLANCO
pos=None
global dibuja
mover=0
global ultimo_seleccionado
ultimo_seleccionado=None
dibuja = True
def posicion_relativa(posicion: tuple[int, int]):
    x = posicion[0] * tablero_tamano[0]/8  - (tablero_tamano[0]/8)
    y = (9 - posicion[1]) * tablero_tamano[0]/8 + 2 - tablero_tamano[0]/8-1
    return (x, y)

def posicion_relativa_centrada(posicion: tuple[int, int]):
    x = posicion[0] * tablero_tamano[0]/8  - CUADRADO+tablero_tamano[0]/16
    y = (9 - posicion[1]) * tablero_tamano[0]/8 + 2 - CUADRADO+tablero_tamano[0]/16
    return (x, y)


def numero_relativo(posicion: tuple[int, int]):
    x = int((posicion[0] - CUADRADO-3) / CUADRADO + 2)
    y = 9 - int(posicion[1] / CUADRADO + 0.02 + 0.99)
    return (x, y)
def dibujar_tablero():

    imagen = "Imagenes\\Tablero.png"
    imp = pygame.image.load(imagen).convert()
    imp = pygame.transform.scale(imp, (tablero_tamano[0],tablero_tamano[1]))
    pantalla.blit(imp,(0,0))

def dibujar_posibles(posicion):
    a: Pieza=tablero_primario.encontrar_pieza(posicion)


    if a!=None:
        if tablero_primario.tiene_jaque()==False:
            la_posicion = tablero_primario.posibles_movimientos_bien(a)
        else:
            la_posicion=tablero_primario.evitar_jaque(a)

        if la_posicion!=None and len(la_posicion) > 0:
            #print("comprobante",la_posicion)
            for b in la_posicion:
                posicion_a_dibujar = posicion_relativa_centrada(b)
                #print(posicion_a_dibujar)
                pygame.draw.circle(pantalla, (40,40,40), (posicion_a_dibujar), CUADRADO/12, 0)


def mover_pieza(pieza,posicion_nueva):

    if  tablero_primario.puedo_comer(pieza,posicion_nueva)==True:

        tablero_primario.remover_pieza(tablero_primario.encontrar_pieza(posicion_nueva))
    pieza.posicion = posicion_nueva
    p11 = tablero_primario.encontrar_pieza((1, 1))
    p81 = tablero_primario.encontrar_pieza((8, 1))
    p18 = tablero_primario.encontrar_pieza((1, 8))
    p88 = tablero_primario.encontrar_pieza((8, 8))

    if pieza.tipo==TipoPieza.REY and pieza.movio==False and pieza.posicion==(3,1) and p11!=None and p11.movio==False:
        p11.posicion=(4,1)

    if pieza.tipo == TipoPieza.REY and pieza.movio == False and pieza.posicion == (7, 1) and p81 != None and p81.movio == False:
        p81.posicion = (6, 1)

    if pieza.tipo == TipoPieza.REY and pieza.movio == False and pieza.posicion == (7, 8) and p88 != None and p88.movio == False:
        p88.posicion = (6, 8)
    if pieza.tipo == TipoPieza.REY and pieza.movio == False and pieza.posicion == (3, 8) and p18 != None and p18.movio == False:
        p18.posicion = (4, 8)
    pieza.movio=True

    if tablero_primario.tiene_jaque()==True:
        print("Hay jaque")

def transformacion_de_coordenadas(letra):
    contador=1
    if letra[0] == "a":
       contador=1
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


    return (contador,int(letra[1]))
def inutil(dibuja):
    return dibuja
def enviar_peticion():
    global turno
    if turno == TipoBando.NEGRO:
        best=bot.enviar_peticion(tablero_primario, turno)
        if best!=None:
            inicial=best[0]+best[1]
            final=best[2]+best[3]
            posicion_inicial=transformacion_de_coordenadas(inicial)
            posicion_final=transformacion_de_coordenadas(final)
            if tablero_primario.encontrar_pieza(posicion_inicial)!=None:
                print("moviendo pieza a: ", posicion_final)
                print(tablero_primario.encontrar_pieza(posicion_inicial).bando,tablero_primario.encontrar_pieza(posicion_inicial).tipo)

                mover_pieza(tablero_primario.encontrar_pieza(posicion_inicial),posicion_final)
                turno=cambiar_turno(turno)

                global ultimo_seleccionado
                ultimo_seleccionado = None
                global dibuja
                dibuja = True
            else:
                print("ERROR NO HAY PIEZA")
        else:
            print("ERROR 404")



def cambiar_turno(turno):
    if turno  == TipoBando.BLANCO:
        turno = TipoBando.NEGRO
    else:
        turno = TipoBando.BLANCO
    return turno
def game_over():
    listilla=[]
    for a in tablero_primario.piezas:
        for b in tablero_primario.evitar_jaque(a):
            listilla.append(b)
            if len(listilla)>0 and tablero_primario.tiene_jaque()==True:
                return True
def dibujar_piezas():
    for a in tablero_primario.piezas:
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
        imp = pygame.transform.scale(imp, (CUADRADO, CUADRADO))
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



while not Terminar:
    for Evento in pygame.event.get():
        if Evento.type == pygame.QUIT:
            Terminar = True
        if Evento.type == MOUSEBUTTONDOWN and Evento.button==1:

            pos= numero_relativo(Evento.pos)
            if tablero_primario.encontrar_pieza(pos)!=None and turno==tablero_primario.encontrar_pieza(pos).bando:
                ultimo_seleccionado = tablero_primario.encontrar_pieza(pos)
                dibuja = True
            elif ultimo_seleccionado !=None:
                if tablero_primario.tiene_jaque()==False:
                    if pos in tablero_primario.posibles_movimientos_bien(ultimo_seleccionado):
                        mover_pieza(ultimo_seleccionado,pos)
                        turno = cambiar_turno(turno)
                        x = threading.Thread(target=enviar_peticion)
                        x.start()
                        ultimo_seleccionado=None
                        dibuja = True
                else:
                    if pos in tablero_primario.evitar_jaque(ultimo_seleccionado):
                        mover_pieza(ultimo_seleccionado,pos)
                        turno = cambiar_turno(turno)
                        x = threading.Thread(target=enviar_peticion)
                        x.start()
                        ultimo_seleccionado=None
                        dibuja = True
        if Evento.type == MOUSEBUTTONDOWN and Evento.button == 3:
            pos = numero_relativo(Evento.pos)
            if tablero_primario.encontrar_pieza(pos) != None:
                ultimo_seleccionado = tablero_primario.encontrar_pieza(pos)


            elif ultimo_seleccionado != None:
                mover_pieza(ultimo_seleccionado, pos)
                ultimo_seleccionado = None
                dibuja = True


    if dibuja==True:

        dibuja=False
        dibujar_tablero()
        dibujar_piezas()
        if ultimo_seleccionado!=None:
            dibujar_posibles(ultimo_seleccionado.posicion)







    pygame.display.update()
    pygame.display.flip()
    reloj.tick(20)  # Limitamos a 20 fotogramas por segundo
pygame.quit()