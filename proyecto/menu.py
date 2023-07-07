import pygame
pygame.display.set_caption("Menú del Juego")
font_title = pygame.font.Font(None, 64)
font_button = pygame.font.Font(None, 32)
blanco = (255, 255, 255)
negro = (0, 0, 0)
ancho = (802)
largo = (802)

# Función para mostrar el menú
def mostrar_menu():
    pantalla.fill(blanco)

    # Dibujar el título del menú
    title_text = font_title.render("Ajedrez", True, negro)
    title_rect = title_text.get_rect(center=(ancho // 2, largo // 3))
    pantalla.blit(title_text, title_rect)

    # Dibujar los botones del menú
    button_jugar = font_button.render("Jugar", True, negro)
    button_salir = font_button.render("Salir", True, negro)
    button_rect_jugar = button_jugar.get_rect(center=(ancho // 2, largo // 2))
    button_rect_salir = button_salir.get_rect(center=(ancho // 2, largo // 2 + 100))
    pantalla.blit(button_jugar, button_rect_jugar)
    pantalla.blit(button_salir, button_rect_salir)

    # Actualizar la pantalla
    pygame.display.flip()

# Función para detectar los clics del mouse
def verificar_clic(pos):
    if button_rect_jugar.collidepoint(pos):
        # Acción al hacer clic en el botón "Jugar"
        print("Haz clic en Jugar")
        # Aquí puedes agregar la lógica para pasar a la pantalla del juego
        iniciar_juego()

    elif button_rect_salir.collidepoint(pos):
        # Acción al hacer clic en el botón "Salir"
        print("Haz clic en Salir")
        # Aquí puedes agregar la lógica para salir del juego
        pygame.quit()


    # Función para iniciar el juego
def iniciar_juego():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Lógica y dibujado del juego...

        pygame.display.flip()


# Bucle principal del menú
mostrar_menu()
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Verificar si se hizo clic en el menú
            pos = pygame.mouse.get_pos()
            verificar_clic(pos)