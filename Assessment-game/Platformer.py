import pygame
import random
import sys
from pygame.locals import *

mainClock = pygame.time.Clock()


def collisionsAny(a_x, a_y, a_width, a_height, b_x, b_y, b_width, b_height):
    if (a_x + a_width > b_x) and (a_x < b_x + b_width) and (a_y + a_height > b_y) and (a_y < b_y + b_height):
        return 1
    else:
        return 0


def main():
    pygame.init()
    pygame.display.set_caption("Platformer")
    pygame.mixer.music.load("hit.wav")
    # pygame.mixer.music.play(-1)
    hit_sound = pygame.mixer.Sound("hit.wav")
    jump_sound = pygame.mixer.Sound("jump.wav")
    Lighting = pygame.image.load('light.png')
    BG = pygame.image.load('BG.jpg')
    Darkness = pygame.image.load('Darkness.jpg')
    floor = pygame.image.load('Ground.png')
    player = pygame.image.load('Player.png')
    player2 = pygame.image.load('Player2.jpg')
    DISPLAY = pygame.display.set_mode((1024, 576), 0, 32)
    particles = []
    playerX = 20
    playerY = 516
    playerWidth = 40
    playerHeight = 40
    floorX = 0
    floorY = 550
    velocityX = 0
    velocityY = 0
    left = 0
    # colour
    GREY = (19, 19, 19)
    WHITE = (255, 255, 255)
    DISPLAY.fill(WHITE)
    pygame.draw.rect(DISPLAY, GREY, [0, 576, 1024, 26])
    DISPLAY.blit(BG, (0, 0))
    DISPLAY.blit(Darkness, (0, 0))
    DISPLAY.blit(player, (playerX, playerY))

    while True:
        DISPLAY.fill(WHITE)
        DISPLAY.blit(BG, (0, 0))
        pygame.draw.rect(DISPLAY, GREY, [0, 550, 1024, 26])
        DISPLAY.blit(floor, (floorX, floorY))
        DISPLAY.blit(Lighting, (playerX + 20 - 256 / 2, playerY + 20 - 256 / 2), special_flags=BLEND_RGB_ADD)

        if left == 0:
            DISPLAY.blit(player, (playerX, playerY))
        else:
            DISPLAY.blit(player2, (playerX, playerY))

        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.1
            pygame.draw.circle(DISPLAY, (100, 100, 100), [int(particle[0][0]), int(particle[0][1])],
                               int(particle[2]))
            if particle[2] <= 0:
                particles.remove(particle)

        # if collisionsAny(playerX, playerY, playerWidth, playerHeight, dotX, dotY, dotW, dotH) == 1:

        # movement
        playerX = playerX + velocityX
        playerY = playerY + velocityY
        velocityX = velocityX * 0.85

        if playerX > 984:
            hit_sound.play()
            velocityX = 0
            playerX = 984

        if playerX < 0:
            hit_sound.play()
            velocityX = 0
            playerX = 0

        if playerY < 516:
            velocityY = velocityY + 1

        if playerY > 516:
            hit_sound.play()
            velocityY = 0
            playerY = 516
            particles.append([[playerX + 20, playerY + 40], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])
            particles.append([[playerX + 20, playerY + 40], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            velocityX = velocityX + 1
            left = 0

        if keys[pygame.K_a]:
            velocityX = velocityX + -1
            left = 1

        # event
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    if playerY == 516:
                        playerY = 517
                        jump_sound.play()
                        velocityY = velocityY - 15
                        particles.append(
                            [[playerX + 20, playerY + 40], [random.randint(0, 20) / 10 - 1, -2], random.randint(2, 4)])
                        particles.append(
                            [[playerX + 20, playerY + 40], [random.randint(0, 20) / 10 - 1, -2], random.randint(2, 4)])

            # buttons

        pygame.display.update()
        pygame.time.delay(10)


main()
