# snake game - Fáze 1: Základní okno a smyčka
# https://www.youtube.com/watch?v=_-KjEgCLQFw

import pygame as pg  # importuje knihovnu Pygame pro tvorbu her a grafiky
import sys  # importuje systémový modul sys, zde pro ukončení programu

OKNO = 1000  # definuje velikost okna aplikace na 1000x1000 pixelů

screen = pg.display.set_mode([OKNO] * 2)  # vytvoří grafické okno o rozměrech OKNO x OKNO
clock = pg.time.Clock()  # vytvoří objekt hodin pro řízení rychlosti smyčky (FPS)

while True:  # nekonečná smyčka, která udržuje hru v chodu
    for event in pg.event.get():  # prochází seznam všech událostí, které nastaly (klávesy, myš...)
        if event.type == pg.QUIT:  # pokud uživatel klikl na křížek pro zavření okna
            pg.quit()  # ukončí Pygame
            sys.exit()  # ukončí celý Python skript

    screen.fill('black')  # vyplní celé okno černou barvou

    pg.display.flip()  # aktualizuje celou obrazovku
    clock.tick(60)  # omezí rychlost smyčky na 60 snímků za sekundu
