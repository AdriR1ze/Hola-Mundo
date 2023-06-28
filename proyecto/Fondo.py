import pygame
import Posicion
pygame.init()
Pantalla = pygame.display.set_mode((500,500))
reloj = pygame.time.Clock()
Terminar=False
while not Terminar:
    # ---Manejo de eventos
    for Evento in pygame.event.get():
        if Evento.type == pygame.QUIT:
            Terminar = True
    # ---La lógica del juego


    largo=50
    altura=50
    NEGRO=(0,0,0)
    # ---Código de dibujo----
    Pantalla.fill((255,255,255))
    # --Todos los dibujos van después de esta línea
    for a in range(10):
        pygame.draw.line(Pantalla, (0, 0, 0), [largo, 0], [largo, 500], 2)
        largo=largo+50
    for a in range(10):
        pygame.draw.line(Pantalla, (0, 0, 0), [0, altura], [500, altura], 2)
        altura = altura + 50
    pygame.draw.circle(Pantalla, NEGRO, (150, 250), 100, 0)

    # --Todos los dibujos van antes de esta línea
    pygame.display.flip()
    reloj.tick(20)  # Limitamos a 20 fotogramas por segundo
pygame.quit()