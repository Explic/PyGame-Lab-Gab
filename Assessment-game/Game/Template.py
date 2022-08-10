import pygame, sys, random
from pygame.locals import *


def main():
    def setup():
        pygame.init()

        DISPLAY = pygame.display.set_mode((500, 400), 0, 32)

        # colour
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        DISPLAY.fill(WHITE)


    def loop():

        # event
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # buttons
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

        pygame.display.update()
        pygame.time.delay(10)
        loop()

    setup()
    loop()


main()
