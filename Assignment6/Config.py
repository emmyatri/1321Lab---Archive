#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment 6

import pygame, sys
pygame.init()
pygame.mixer.init()

#general settings
##################################
WIDTH, HEIGHT = 480,800
RESOLUTION = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(RESOLUTION)
pygame.display.set_mode(RESOLUTION)

CLOCK = pygame.time.Clock()
CLOCK.tick(60)

#custom meteor event
METEOR_EVENT = pygame.USEREVENT + 1

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#player settings
##################################
PLAYER_SPEED = 12
PLAYER_IMAGE = pygame.image.load("player_sprite.png")
PLAYER_DEATH_SOUND = pygame.mixer.Sound("player_dead.ogg")

#meteor settings
##################################
METEOR_SPEEDS = {
    "big" : 10,
    "medium" : 11,
    "small" : 12,
    "tiny" : 12
}

PATHS = {
    "big" : ["meteor_big_1.png", "meteor_big_2.png", "meteor_big_3.png", "meteor_big_4.png"],
    "medium" : ["meteor_med_1.png", "meteor_med_2.png"],
    "small" : ["meteor_small_1.png", "meteor_small_2.png"],
    "tiny" : ["meteor_tiny_1.png", "meteor_tiny_2.png"]
}

SOUNDS = ["spawn_sound_1.ogg", "spawn_sound_2.ogg", "spawn_sound_3.ogg"]