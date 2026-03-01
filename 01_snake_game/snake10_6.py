# snake game
# https://www.youtube.com/watch?v=_-KjEgCLQFw

import pygame as pg  # importuje knihovnu Pygame pro tvorbu her a grafiky
import random  # importuje modul random pro generování náhodných čísel
import sys  # importuje systémový modul sys, zde pro ukončení programu

OKNO = 1000  # definuje velikost okna aplikace na 1000x1000 pixelů
TILE_SIZE = 30  # nastavuje velikost jednoho čtverečku (dlaždice) hada a jídla na 30 pixelů

RANGE = (TILE_SIZE // 2, OKNO - TILE_SIZE // 2, TILE_SIZE)  # definuje rozsah souřadnic pro generování, aby byly zarovnané na mřížku
get_random_position = lambda: (random.randrange(*RANGE), random.randrange(*RANGE))  # lambda funkce vracející náhodnou pozici (x, y) na mřížce

snake = pg.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])  # vytvoří obdélníkový objekt hada s mírným odsazením pro vizuální oddělení
snake.center = get_random_position()  # nastaví počáteční pozici hada na náhodné místo

length = 1  # inicializuje počáteční délku hada na 1 článek
segments = [snake.copy()]  # vytvoří seznam segmentů hada, na začátku obsahuje jen hlavu

snake_dir = (0, 0)  # nastavuje počáteční směr pohybu hada na (0, 0) - had stojí
# uprava rychlosti hada
time, time_step = 0, 250  # inicializuje časovač a interval pohybu hada na 250 milisekund

food = snake.copy()  # vytvoří objekt jídla jako kopii hadího článku
food.center = get_random_position()  # umístí jídlo na náhodnou pozici

screen = pg.display.set_mode([OKNO] * 2)  # vytvoří grafické okno o rozměrech OKNO x OKNO
clock = pg.time.Clock()  # vytvoří objekt hodin pro řízení rychlosti smyčky (FPS)

while True:  # nekonečná smyčka, která udržuje hru v chodu
    for event in pg.event.get():  # prochází seznam všech událostí, které nastaly (klávesy, myš...)
        if event.type == pg.QUIT:  # pokud uživatel klikl na křížek pro zavření okna
            pg.quit()  # ukončí Pygame
            sys.exit()  # ukončí celý Python skript
        if event.type == pg.KEYDOWN:  # pokud byla stisknuta nějaká klávesa
            if event.key == pg.K_UP:  # pokud byla stisknuta šipka nahoru
                snake_dir = (0, -TILE_SIZE)  # nastaví směr pohybu nahoru (záporná osa Y)
            if event.key == pg.K_DOWN:  # pokud byla stisknuta šipka dolů
                snake_dir = (0, TILE_SIZE)  # nastaví směr pohybu dolů (kladná osa Y)
            if event.key == pg.K_LEFT:  # pokud byla stisknuta šipka vlevo
                snake_dir = (-TILE_SIZE, 0)  # nastaví směr pohybu doleva (záporná osa X)
            if event.key == pg.K_RIGHT:  # pokud byla stisknuta šipka vpravo
                snake_dir = (TILE_SIZE, 0)  # nastaví směr pohybu doprava (kladná osa X)
    screen.fill('black')  # vyplní celé okno černou barvou (vymazání předchozího snímku)
    # kontrola hran
    if snake.left < 0 or snake.right > OKNO or snake.top < 0 or snake.bottom > OKNO:  # kontroluje, zda had nenarazil do okraje okna
        snake.center, food.center = get_random_position(), get_random_position()  # pokud narazil, resetuje pozici hada i jídla
        length = 1  # resetuje délku hada na 1
        snake_dir = (0, 0)  # zastaví pohyb hada
        segments = [snake.copy()]  # resetuje seznam segmentů hada
        
        
    # kontrola kolize hada se sebou samy
    if snake in segments[1:]:  # kontroluje, zda souřadnice hlavy nejsou v seznamu souřadnic těla (náraz do sebe)
        pg.quit()  # ukončí Pygame
        sys.exit()  # ukončí program

    # kontrola kolize s jidlem
    if snake.colliderect(food):  # zjišťuje, zda se obdélník hada překrývá s obdélníkem jídla
        length += 1  # zvětší délku hada o 1
        food.center = get_random_position()  # vygeneruje novou pozici pro jídlo
        
    # malujeme jidlo
    pg.draw.rect(screen, 'red', food)  # vykreslí jídlo jako červený obdélník
    # malujeme hada
    [pg.draw.rect(screen, 'green', segment) for segment in segments]  # vykreslí každý segment hada jako zelený obdélník

    # posun hada
    time_now = pg.time.get_ticks()  # zjistí aktuální čas v milisekundách od spuštění
    if time_now - time > time_step:  # pokud uplynul dostatečný čas (time_step) od posledního pohybu
        time = time_now  # aktualizuje čas posledního pohybu
        snake.move_ip(snake_dir)  # posune obdélník hada o vektor snake_dir
        segments.insert(0, snake.copy())  # vloží novou pozici hlavy na začátek seznamu segmentů
        segments = segments[:length]  # ořízne seznam segmentů na aktuální délku hada (odstraní konec ocasu)



    pg.display.flip()  # aktualizuje celou obrazovku, aby se změny projevily
    clock.tick(60)  # omezí rychlost smyčky na 60 snímků za sekundu
