import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (400,400)

screen = pygame.display.set_mode(resolution)

clock = pygame.time.Clock()


def fade_screen():

    color = 1
    fade_to_white = True
    fade_speed = 1

    while True:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)

            if keys[pygame.K_ESCAPE]:
                sys.exit(0)

        if fade_to_white:
            color += fade_speed
            if color >= 255:
                color = 255
                fade_to_white = False


        else:
            color -= fade_speed
            if color <= 0:
                color = 0
                fade_to_white = True

        current_color = (color, color, color)
        screen.fill(current_color)

        pygame.display.flip()
        clock.tick(60)

def main():
    fade_screen()

if __name__ == "__main__":
    main()