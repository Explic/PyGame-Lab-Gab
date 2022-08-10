import pygame, sys, random
from pygame.locals import *


def main():
    pygame.init()

    DISPLAY = pygame.display.set_mode((500, 400), 0, 32)

    sprite1 = pygame.image.load('Dot.png')

    # colour
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)

    DISPLAY.fill(WHITE)

    DISPLAY.blit(sprite1, (100, 100))
    x = 100
    y = 100
    velocity = 0
    acceleration = 0.1

    while True:

        DISPLAY.fill(WHITE)
        DISPLAY.blit(sprite1, (x, y, 50, 50))
        y += velocity
        velocity += acceleration

        # event
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # buttons
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if keys[pygame.K_SPACE]:
                    velocity = -3

        pygame.display.update()
        pygame.time.delay(10)


main()
