#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab11B


import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (600, 600)
screen = pygame.display.set_mode(resolution)

pygame.display.set_mode(resolution)

clock = pygame.time.Clock()

while True:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    screen.fill(color=(0, 0, 0))

    # surface 1
    surf1 = pygame.Surface((60, 60))
    surf1.fill((255, 0, 0))

    screen.blit(surf1, (0, 0))
    screen.blit(surf1, (540, 0))
    screen.blit(surf1, (0, 540))
    screen.blit(surf1, (540, 540))
    screen.blit(surf1, (270, 270))

    pygame.display.flip()

    clock.tick(60)

