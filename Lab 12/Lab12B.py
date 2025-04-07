#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab12B

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
moving_right_top = True
moving_right_middle = True
moving_right_bottom = True
middle_speed = 5
top_speed = 10
bottom_speed = 20

#oscillating square
square_surf = pygame.Surface((square_size, square_size))
square_surf.fill(blue)
top_blue = square_surf.get_rect()
top_blue.topleft = (0,0)
middle_blue = square_surf.get_rect()
middle_blue.midleft = (0,y//2)
bottom_blue = square_surf.get_rect()
bottom_blue.bottomleft = (0,y)


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

    if moving_right_top:
        top_blue = top_blue.move(top_speed,0)
        if top_blue.right >= 400:
            moving_right_top = False
    else:
        top_blue = top_blue.move(-top_speed, 0)
        if top_blue.left <= 0:
            moving_right_top = True

    if moving_right_middle:
        middle_blue = middle_blue.move(middle_speed, 0)
        if middle_blue.right >= 400:
            moving_right_middle = False

    else:
        middle_blue = middle_blue.move(-middle_speed, 0)
        if middle_blue.left <= 0:
            moving_right_middle = True

    if moving_right_bottom:
        bottom_blue = bottom_blue.move(bottom_speed, 0)
        if bottom_blue.right >= 400:
            moving_right_bottom = False

    else:
        bottom_blue = bottom_blue.move(-bottom_speed, 0)
        if bottom_blue.left <= 0:
            moving_right_bottom = True



    if red_rect_rect.colliderect(top_blue) or red_rect_rect.colliderect(middle_blue) or red_rect_rect.colliderect(bottom_blue):
        pygame.draw.rect(screen, green, red_rect_rect)
    else:
        pygame.draw.rect(screen, red, red_rect_rect)
    pygame.draw.rect(screen, blue, top_blue)
    pygame.draw.rect(screen, blue, middle_blue)
    pygame.draw.rect(screen, blue, bottom_blue)



    pygame.display.flip()

    clock.tick(60)