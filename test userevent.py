import pygame
import pygame.locals
import sys
pygame.init()
x, y = 700, 400
screen = pygame.display.set_mode((x, y))
sukien_lap = pygame.USEREVENT
pygame.time.set_timer(sukien_lap, 2000)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        elif event.type == sukien_lap:
            print("yes")
    pygame.display.flip()