#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment 6

import pygame, sys, random
from Config import *
from Meteor import Meteor
from Player import Player

def main():

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Meteor Dodge")

    pygame.time.set_timer(METEOR_EVENT, 1000)

    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 48)
    game_over = font.render("You Lost!", True, WHITE)
    game_over_rect = game_over.get_rect(center=(WIDTH//2, HEIGHT//2))

    game_over_screen = pygame. Surface((WIDTH, HEIGHT))
    game_over_screen.set_alpha(100)
    game_over_screen.fill(BLACK)

    background = pygame.image.load(BACKGROUND_IMAGE).convert()

    meteors = []
    player = Player()

    running = True

    while running:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)

            if event.type == METEOR_EVENT:

                meteor = Meteor()
                meteors.append(meteor)
                meteor.spawn_sound.play()

                pygame.time.set_timer(METEOR_EVENT, random.randint(800, 1500))

        screen.blit(background, (0,0))

        for meteor in meteors[:]:
            meteor.fall()
            meteor.draw(screen)

            if meteor.rect.top > HEIGHT:
                meteors.remove(meteor)

            if player.alive and meteor.rect.colliderect(player.rect):
                player.deadSound.play()
                player.alive = False


        if player.alive:
            player.move()
            player.draw()
        else:
            screen.blit(game_over_screen, (0,0))
            screen.blit(game_over, game_over_rect)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()




