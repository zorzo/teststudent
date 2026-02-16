
import sys
import pygame
# pip install pygame
# initialize pygame

pygame.init()

# set up the display
screen = pygame.display.set_mode((400, 300))

# set up the square
square = pygame.Rect(0, 0, 5, 5)

# set up the clock
clock = pygame.time.Clock()

# set up the speed
speed = 1

# main game loop
while True:
  # handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  # move the square
  square.move_ip(speed, 0)

  # check if the square is off the screen
  if square.right > screen.get_width():
    square.left = 0

  # draw the square
  screen.fill((255, 255, 255))
  pygame.draw.rect(screen, (0, 0, 0), square)

  # update the display
  pygame.display.update()

  # tick the clock
  clock.tick(60)


