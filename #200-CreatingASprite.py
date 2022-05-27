import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("PyGame Window")
screen.fill((0, 0, 0))

sprite1 = pygame.image.load("dot.png")