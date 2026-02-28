# snake game - Fáze 5: Pojídání jídla
# https://www.youtube.com/watch?v=_-KjEgCLQFw

import pygame as pg
import random
import sys

OKNO = 1000
TILE_SIZE = 30

RANGE = (TILE_SIZE // 2, OKNO - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: (random.randrange(*RANGE), random.randrange(*RANGE))

snake = pg.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()

length = 1
segments = [snake.copy()]

snake_dir = (0, 0)
time, time_step = 0, 250

food = snake.copy()
food.center = get_random_position()

screen = pg.display.set_mode([OKNO] * 2)
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                snake_dir = (0, -TILE_SIZE)
            if event.key == pg.K_DOWN:
                snake_dir = (0, TILE_SIZE)
            if event.key == pg.K_LEFT:
                snake_dir = (-TILE_SIZE, 0)
            if event.key == pg.K_RIGHT:
                snake_dir = (TILE_SIZE, 0)

    screen.fill('black')

    # kontrola kolize s jidlem
    if snake.colliderect(food):
        length += 1  # zvětší hada
        food.center = get_random_position()  # nové jídlo

    # malujeme jidlo
    pg.draw.rect(screen, 'red', food)
    # malujeme hada
    [pg.draw.rect(screen, 'green', segment) for segment in segments]

    # posun hada
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.insert(0, snake.copy())
        segments = segments[:length]

    pg.display.flip()
    clock.tick(60)
