# snake game - Fáze 3: Pohyb hada
# https://www.youtube.com/watch?v=_-KjEgCLQFw

import pygame as pg
import random
import sys

# Konfigurace hry
OKNO = 1000
TILE_SIZE = 30

# Pomocné funkce pro generování pozic
RANGE = (TILE_SIZE // 2, OKNO - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: (random.randrange(*RANGE), random.randrange(*RANGE))

# Inicializace hada
snake = pg.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()

# Nastavení pohybu
snake_dir = (0, 0)  # Počáteční směr (0, 0) znamená, že had čeká na vstup
# Časování pohybu (rychlost hada)
time, time_step = 0, 250  # Interval pohybu v milisekundách

# Inicializace jídla
food = snake.copy()
food.center = get_random_position()

# Nastavení grafického okna
screen = pg.display.set_mode([OKNO] * 2)
clock = pg.time.Clock()

# Hlavní herní smyčka
while True:
    # Zpracování událostí (vstupy uživatele)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:  # Změna směru pohybu pomocí kláves
            if event.key == pg.K_UP:
                snake_dir = (0, -TILE_SIZE)
            if event.key == pg.K_DOWN:
                snake_dir = (0, TILE_SIZE)
            if event.key == pg.K_LEFT:
                snake_dir = (-TILE_SIZE, 0)
            if event.key == pg.K_RIGHT:
                snake_dir = (TILE_SIZE, 0)

    # Vykreslování herní plochy
    screen.fill('black')

    # Vykreslení jídla a hada
    pg.draw.rect(screen, 'red', food)
    pg.draw.rect(screen, 'green', snake)

    # Logika pohybu založená na čase (ne na FPS)
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:  # Kontrola, zda uplynul nastavený interval
        time = time_now
        snake.move_ip(snake_dir)  # Posun hada v aktuálním směru

    # Aktualizace displeje
    pg.display.flip()
    clock.tick(60)
