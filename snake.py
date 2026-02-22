# Hra snake s pomocí knihovny pygame
import pygame
import random

# Inicializace Pygame
pygame.init()

# Nastavení rozměrů okna
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Nastavení titulku okna
pygame.display.set_caption("Snake Game")

