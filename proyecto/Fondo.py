import pygame
import TableroConceptual as TC
pygame.init()
Pantalla = pygame.display.set_mode((1000,1000))
reloj = pygame.time.Clock()
Terminar=False
while not Terminar:
    # ---Manejo de eventos
    for Evento in pygame.event.get():
        if Evento.type == pygame.QUIT:
            Terminar = True
    # ---La lógica del juego

    ListaDeColumnas = ["1", "2", "3", "4", "5", "6", "7", "8"]
    ListaDeFilas = ["1", "2", "3", "4", "5", "6", "7", "8"]
    largo=50
    altura=50
    NEGRO=(0,0,0)
    # ---Código de dibujo----
    Pantalla.fill((255,255,255))
    # --Todos los dibujos van después de esta línea

    for a in range(1):
        largo = largo + 125
        pygame.draw.line(Pantalla, (0, 0, 0), [largo, 0], [largo, 1000], 2)

    for a in range(1):
        altura = altura + 125
        pygame.draw.line(Pantalla, (0, 0, 0), [0, altura], [1000, altura], 2)



    # --Todos los dibujos van antes de esta línea
    pygame.display.flip()
    reloj.tick(20)  # Limitamos a 20 fotogramas por segundo
pygame.quit()