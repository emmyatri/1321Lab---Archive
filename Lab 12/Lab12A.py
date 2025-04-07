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
window_height = 400
window_width = 400
resolution = (window_width,window_height)
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
square_rect = pygame.Rect(0,(rect_height/2 - rect_length/2),square_size,square_size)
square_surf = pygame.Surface((square_size,square_size))
square_surf.fill(blue)

#static vertical rectangle
rect_rect = pygame.Rect(150,0,rect_length, rect_height)
rect_surf = pygame.Surface((rect_length,rect_height))
coordinates = rect_rect.midtop
rect_surf.fill(red)

while True:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    screen.fill(color=black)

    


    pygame.display.flip()

    clock.tick(60)