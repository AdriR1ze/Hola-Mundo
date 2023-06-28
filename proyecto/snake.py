import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana del juego
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colores
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Tamaño de la serpiente y la comida
block_size = 20

# Velocidad de movimiento de la serpiente
clock = pygame.time.Clock()
snake_speed = 15

# Función principal del juego
def game():
    game_over = False
    game_quit = False

    # Posición inicial de la serpiente
    x1 = width / 2
    y1 = height / 2

    # Movimiento inicial de la serpiente
    x1_change = 0
    y1_change = 0

    # Lista para almacenar el cuerpo de la serpiente
    snake_list = []
    snake_length = 1

    # Posición aleatoria de la comida
    foodx = round(random.randrange(0, width - block_size) / block_size) * block_size
    foody = round(random.randrange(0, height - block_size) / block_size) * block_size

    while not game_quit:
        while game_over:
            # Mostrar mensaje de Game Over
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("Game Over. Presiona Q para salir o C para jugar de nuevo", True, RED)
            screen.blit(message, [width / 6, height / 3])
            pygame.display.update()

            # Manejo de eventos mientras está en el estado de Game Over
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_quit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game()

        # Manejo de eventos mientras el juego está en ejecución
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Verificar colisión con los bordes de la ventana
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True

        # Actualizar posición de la serpiente
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)

        # Dibujar comida
        pygame.draw.rect(screen, GREEN, [foodx, foody, block_size, block_size])

        # Actualizar cuerpo de la serpiente
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Verificar colisión con el propio cuerpo de la serpiente
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        # Dibujar cuerpo de la serpiente
        for segment in snake_list:
            pygame.draw.rect(screen, GREEN, [segment[0], segment[1], block_size, block_size])

        pygame.display.update()

        # Verificar si la serpiente ha comido la comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / block_size) * block_size
            foody = round(random.randrange(0, height - block_size) / block_size) * block_size
            snake_length += 1

        # Controlar la velocidad del juego
        clock.tick(snake_speed)

    # Finalizar Pygame
    pygame.quit()


# Iniciar el juego
game()
