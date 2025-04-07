#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab12A

import pygame, sys
from pygame.locals import *
pygame.init()

#screen resolution
x, y = 400,400
resolution = (x, y)
screen = pygame.display.set_mode(resolution)
pygame.display.set_mode(resolution)

#framerate
clock = pygame.time.Clock()

#colors
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#heights for squares
square_size = 50

#dimensions for rectangle
rect_height = 400
rect_length = 50

#boolean logic for right / left
moving_right = True
speed = 5

#oscillating square
blue_square_surf = pygame.Surface((square_size, square_size))
blue_square_rect = blue_square_surf.get_rect()
blue_square_rect.midleft = (0,y//2)
blue_square_surf.fill(blue)


#static vertical rectangle
red_rect_surf = pygame.Surface((rect_length, rect_height))
red_rect_rect = red_rect_surf.get_rect()
red_rect_rect.midtop = (x//2,0)
red_rect_surf.fill(red)


while True:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    screen.fill(color=black)

    if moving_right:
        blue_square_rect = blue_square_rect.move(speed,0)
        if blue_square_rect.right >= 400:
            moving_right = False
    else:
        blue_square_rect = blue_square_rect.move(-speed, 0)
        if blue_square_rect.left <= 0:
            moving_right = True

    if red_rect_rect.colliderect(blue_square_rect):
        pygame.draw.rect(screen, green, red_rect_rect)
    if not red_rect_rect.colliderect(blue_square_rect):
        pygame.draw.rect(screen, red, red_rect_rect)
    pygame.draw.rect(screen, blue, blue_square_rect)



    pygame.display.flip()

    clock.tick(60)