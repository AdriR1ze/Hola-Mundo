
import pygame
from pygame.locals import *
from utils import Utils

class Menu:
    def __init__(self):
        pass
    def menu(self):
        bg_color = (255, 255, 255)
        self.screen.fill(bg_color)
        black_color = (0, 0, 0)
        start_btn = pygame.Rect(270, 300, 100, 50)
        pygame.draw.rect(self.screen, black_color, start_btn)

        white_color = (255, 255, 255)
        big_font = pygame.font.SysFont("comicsansms", 50)
        small_font = pygame.font.SysFont("comicsansms", 20)
        welcome_text = big_font.render("Ajedrez", False, black_color)
        created_by = small_font.render("Creado por Adriano Mancuso y Tomas Nuñez", True, black_color)
        start_btn_label = small_font.render("Jugar", True, white_color)

        self.screen.blit(welcome_text,
                     ((self.screen.get_width() - welcome_text.get_width()) // 2,
                      150))

        self.screen.blit(created_by,
                     ((self.screen.get_width() - created_by.get_width()) // 2,
                      self.screen.get_height() - created_by.get_height() - 100))

        self.screen.blit(start_btn_label,
                     ((start_btn.x + (start_btn.width - start_btn_label.get_width()) // 2,
                       start_btn.y + (start_btn.height - start_btn_label.get_height()) // 2)))


        key_pressed = pygame.key.get_pressed()

        util = Utils()

        if util.left_click_event():
        # call function to get mouse event
            mouse_coords = util.get_mouse_event()

        # check if "Play" button was clicked
        if start_btn.collidepoint(mouse_coords[0], mouse_coords[1]):
            # change button behavior as it is hovered
            pygame.draw.rect(self.screen, white_color, start_btn, 3)

            # change menu flag
            self.menu_showed = True
        # check if enter or return key was pressed
        elif key_pressed[K_RETURN]:
            self.menu_showed = True