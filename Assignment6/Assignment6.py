#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment 6

import pygame, sys, random
from Config import *
from Meteor import *
from Player import *

pygame.init()
pygame.mixer.init()

pygame.display.set_mode(RESOLUTION)
CLOCK.tick(60)

while True:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    SCREEN.fill(color=BLACK)
    pygame.display.flip()
    CLOCK.tick(60)



