#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab11C

import pygame, sys
from pygame.locals import *

pygame.init()

#size parameters
window_width = 1000
window_height = 500
square_size = 100
speed = 5

#colors
black = (0, 0, 0)
green = (0,255,0)
blue = (0,0, 255)

#display + clock
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

#boolean right vs left logic initialization
moving_right = True

#top components
top_rect = pygame.Rect(0,0,square_size,square_size)
top_surf = pygame.Surface((square_size, square_size))
top_surf.fill(green)

#bottom components
bottom_rect = pygame.Rect(0, window_height - (2 * square_size), square_size, square_size)
bottom_surf = pygame.Surface((square_size, square_size))
bottom_surf.fill(blue)

while True:

    #user key input
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    #initial display
    screen.fill(black)

    #movement logic
    if moving_right:
        top_rect = top_rect.move(speed,0)
        bottom_rect = bottom_rect.move(speed, 0)
        if top_rect.right >= 1000 and bottom_rect.right >=1000:
            moving_right = False

    else:
        top_rect = top_rect.move(-speed, 0)
        bottom_rect = bottom_rect.move(-speed, 0)
        if top_rect.left <=0 and bottom_rect.left <= 0:
            moving_right = True

    #get blitted, nerd
    screen.blit(top_surf, top_rect.topleft)
    screen.blit(bottom_surf, bottom_rect.bottomleft)

    pygame.display.flip()

    #60fps
    clock.tick(60)