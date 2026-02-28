# snake game - Fáze 5: Pojídání jídla
# https://www.youtube.com/watch?v=_-KjEgCLQFw

import pygame as pg
import random
import sys

# --- KONFIGURACE HRY ---
OKNO = 1000
TILE_SIZE = 30

# Rozsah pro náhodné generování pozice (zarovnáno na mřížku definovanou TILE_SIZE)
RANGE = (TILE_SIZE // 2, OKNO - TILE_SIZE // 2, TILE_SIZE)
# Lambda funkce pro snadné vygenerování náhodných souřadnic x a y pro objekty
get_random_position = lambda: (random.randrange(*RANGE), random.randrange(*RANGE))

# --- INICIALIZACE HADA ---
# Hlava hada reprezentovaná jako pygame obdélník (Rect) - menší než TILE_SIZE pro vizuální mezery
snake = pg.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()

# Na začátku má had velikost 1 a tělo (segments) obsahuje jen hlavu
length = 1
segments = [snake.copy()]

# Počáteční směr (0, 0 = stojí) a nastavení rychlosti pomocí časovače
snake_dir = (0, 0)
time, time_step = 0, 250 # time_step definuje interval pohybu v ms

# --- INICIALIZACE JÍDLA ---
food = snake.copy()
food.center = get_random_position()

# --- NASTAVENÍ OKNA PYGAME ---
screen = pg.display.set_mode([OKNO] * 2)
clock = pg.time.Clock()

# --- HLAVNÍ HERNÍ SMYČKA ---
while True:
    # 1. Zpracování událostí (vstup od uživatele)
    for event in pg.event.get():
        if event.type == pg.QUIT: # Uživatel zavřel okno
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN: # Zpracování stisku kláves pro změnu směru
            if event.key == pg.K_UP:
                snake_dir = (0, -TILE_SIZE)
            if event.key == pg.K_DOWN:
                snake_dir = (0, TILE_SIZE)
            if event.key == pg.K_LEFT:
                snake_dir = (-TILE_SIZE, 0)
            if event.key == pg.K_RIGHT:
                snake_dir = (TILE_SIZE, 0)

    # 2. Vykreslování
    screen.fill('black') # Smazání obrazovky (na černo) v každém snímku

    # 3. Logika hry: kontrola kolize s jídlem (pokud obdélník hlavy protne obdélník jídla)
    if snake.colliderect(food):
        length += 1  # zvětší hada
        food.center = get_random_position()  # přesune jídlo na novou náhodnou pozici

    # malujeme jidlo
    pg.draw.rect(screen, 'red', food)
    # malujeme hada - procházíme list těla (segments) a pro každý vypíšeme zelený čtverec
    [pg.draw.rect(screen, 'green', segment) for segment in segments]

    # 4. Pohyb hada na základě závislého časovače
    time_now = pg.time.get_ticks()
    # Pohneme hadem pouze pokud uběhl definovaný krok (time_step)
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir) # posune hlavu o nastavený směr
        segments.insert(0, snake.copy()) # do těla přidáme novou pozici hlavy
        segments = segments[:length] # ořízne se konec hada, pokud list překročí délku

    # 5. Aktualizace obrazovky
    pg.display.flip()
    clock.tick(60) # Omezení běhu na 60 FPS
