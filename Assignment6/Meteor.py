#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment 6

import pygame, random
from Config import *

class Meteor:
    def __init__(self):

        #meteor types
        self.types = ["big", "medium", "small", "tiny"]
        self.type = random.choice(self.types)

        #meteor speed by type
        self.speed = METEOR_SPEEDS[self.type]

        #image loading
        sprite_choice = PATHS[self.type]
        sprite_final = random.choice(sprite_choice)
        self.sprite = pygame.image.load(sprite_final)

        #create rectangle
        self.rect = self.sprite.get_rect()

        #random spawn sound
        rand_sound = random.choice(SOUNDS)
        self.spawn_sound = pygame.mixer.Sound(rand_sound)

        #spawn location

        screen_width = WIDTH
        random_x = random.randint(0, screen_width - self.rect.width)
        self.rect.topleft = (random_x, 0)

    def fall(self):
        self.rect.y += self.speed
        return self.rect.top < HEIGHT

    def draw(self,surface):
        surface.blit(self.sprite, self.rect)



