# snake game - Fáze 2: Přidání hada a jídla
# https://www.youtube.com/watch?v=_-KjEgCLQFw

import pygame as pg  # importuje knihovnu Pygame pro tvorbu her a grafiky
import random  # importuje modul random pro generování náhodných čísel
import sys  # importuje systémový modul sys, zde pro ukončení programu

OKNO = 1000  # definuje velikost okna aplikace na 1000x1000 pixelů
TILE_SIZE = 30  # nastavuje velikost jednoho čtverečku (dlaždice) hada a jídla na 30 pixelů

RANGE = (TILE_SIZE // 2, OKNO - TILE_SIZE // 2, TILE_SIZE)  # definuje rozsah souřadnic pro generování
get_random_position = lambda: (random.randrange(*RANGE), random.randrange(*RANGE))  # lambda funkce vracející náhodnou pozici

snake = pg.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])  # vytvoří obdélníkový objekt hada
snake.center = get_random_position()  # nastaví počáteční pozici hada na náhodné místo

food = snake.copy()  # vytvoří objekt jídla jako kopii hadího článku
food.center = get_random_position()  # umístí jídlo na náhodnou pozici

screen = pg.display.set_mode([OKNO] * 2)  # vytvoří grafické okno
clock = pg.time.Clock()  # vytvoří objekt hodin

while True:  # nekonečná smyčka
    for event in pg.event.get():  # prochází seznam událostí
        if event.type == pg.QUIT:  # zavření okna
            pg.quit()
            sys.exit()

    screen.fill('black')  # vymazání obrazovky

    # malujeme jidlo
    pg.draw.rect(screen, 'red', food)  # vykreslí jídlo červeně
    # malujeme hada
    pg.draw.rect(screen, 'green', snake)  # vykreslí hada zeleně (zatím jen jeden čtverec)

    pg.display.flip()  # aktualizace obrazovky
    clock.tick(60)  # omezení FPS
