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
        self.rect