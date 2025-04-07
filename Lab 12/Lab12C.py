#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab12C

import pygame, sys
from pygame.locals import *
pygame.init()

#screen resolution
x, y = 500,500
resolution = (x, y)
screen = pygame.display.set_mode(resolution)
pygame.display.set_mode(resolution)

#framerate
clock = pygame.time.Clock()
speed = 5

#colors
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#heights for squares
square_size = 50

#moveable square
square_surf = pygame.Surface((square_size, square_size))
blue_square = square_surf.get_rect()
blue_square.center = (x//2, y//2)

while True:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

        if keys[pygame.K_w]:

            if blue_square.top > 0:
                blue_square.y -= speed
                print("[EVENT] KEY STATE: W KEY IS BEING PRESSED -> MOVING PLAYER UP")
            else:
                print("[EVENT] KEY STATE: W KEY IS BEING PRESSED -> CANNOT MOVE PLAYER OUT OF BOUNDS")
        if keys[pygame.K_s]:
            if blue_square.bottom < 500:
                blue_square.y += speed
                print("[EVENT] KEY STATE: S KEY IS BEING PRESSED -> MOVING PLAYER DOWN")
            else:
                print("[EVENT] KEY STATE: S KEY IS BEING PRESSED -> CANNOT MOVE PLAYER OUT OF BOUNDS")
        if keys[pygame.K_a]:
            if blue_square.left > 0:
                blue_square.x -= speed
                print("[EVENT] KEY STATE: A KEY IS BEING PRESSED -> MOVING PLAYER TO THE LEFT")
            else:
                print("[EVENT] KEY STATE: A KEY IS BEING PRESSED -> CANNOT MOVE PLAYER OUT OF BOUNDS")
        if keys[pygame.K_d]:
            if blue_square.right < 500:
                blue_square.x += speed
                print("[EVENT] KEY STATE: D KEY IS BEING PRESSED -> MOVING PLAYER TO THE RIGHT")
            else:
                print("[EVENT] KEY STATE: D KEY IS BEING PRESSED -> CANNOT MOVE PLAYER OUT OF BOUNDS")
        if keys[pygame.K_r]:
            print("[EVENT] KEYDOWN: USER PRESSED BUTTON R -> RESETTING PLAYER POSITION")
            blue_square.center = (x//2, y//2)


    #initial screen color
    screen.fill(color=black)

    pygame.draw.rect(screen, blue, blue_square)

    pygame.display.flip()

    clock.tick(60)