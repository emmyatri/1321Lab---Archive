#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment 6

import pygame, sys
from Config import *

class Player:
    def __init__(self):
        self.speed = PLAYER_SPEED
        self.sprite = PLAYER_IMAGE
        self.rect = self.sprite.get_rect()
        self.alive = True
        self.deadSound = PLAYER_DEATH_SOUND

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if self.rect.left > 0:
                self.rect.x -= self.speed

        if keys[pygame.K_d]:
            if self.rect.right < WIDTH:
                self.rect.X += self.speed

    def draw(self):
        SCREEN.blit(self.sprite, self.rect)