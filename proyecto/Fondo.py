import pygame
import TableroConceptual as TC
pygame.init()
Pantalla = pygame.display.set_mode((802,802))
reloj = pygame.time.Clock()
Terminar=False
while not Terminar:
    # ---Manejo de eventos
    for Evento in pygame.event.get():
        if Evento.type == pygame.QUIT:
            Terminar = True
    # ---La lógica del juego

    ListaDeColumnas = [1, 2, 3, 4, 5, 6, 7, 8]
    ListaDeFilas = [1, 2, 3, 4, 5, 6, 7, 8]
    largo=0
    altura=0
    NEGRO=(0,0,0)
    def posicion_relativa(posicion: tuple[int, int]):
        x=posicion[0]*100+2-99
        y=(9 - posicion[1])*100+2-99
        return (x,y)



    # ---Código de dibujo----
    Pantalla.fill((255,255,255))
    imp = pygame.image.load("Imagenes\\CaballoNegro.png").convert()
    imp = pygame.transform.scale(imp, (96, 96))
    p = posicion_relativa((3, 4))
    Pantalla.blit(imp, p)

    # --Todos los dibujos van después de esta línea

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