# import
import pygame
import random
import sys
import button
# import Box
import Hitbox
import HitboxDirectionProperties
import time
from pygame.locals import *

# Setup pygame/window -----------------------------------------
highscore = 0
pygame.init()
pygame.mixer.music.load("460432__jay-you__music-elevator.mp3")
back_sound = pygame.mixer.Sound("270324__littlerobotsoundfactory__menu-navigate-00.wav")
button_sound = pygame.mixer.Sound("270322__littlerobotsoundfactory__menu-navigate-02.wav")
mainClock = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((1024, 576), pygame.NOFRAME, 32)
info_img = pygame.image.load("info.png")
menu_img = pygame.image.load("menu.png")
help_img = pygame.image.load("help.png")
pause_img = pygame.image.load("pause.png")
quit_img = pygame.image.load("button_quit.png").convert_alpha()
quit_button = button.Button(448, 375, quit_img, 1)
info_button = button.Button(448, 275, help_img, 1)
play_img = pygame.image.load("button_play.png").convert_alpha()
play_button = button.Button(448, 175, play_img, 1)
menu = 1
back_img = pygame.image.load("back.png")
back_button = button.Button(448, 475, back_img, 1)
lives = 3
death_img = pygame.image.load("death.png")
alive = 1


# collision detector ----------------------------------------
def collisions_any(a_x, a_y, a_width, a_height, b_x, b_y, b_width, b_height):
    if (a_x + a_width > b_x) and (a_x < b_x + b_width) and (a_y + a_height > b_y) and (a_y < b_y + b_height):
        return 1
    else:
        return 0


# menu -----------------------------------------------------
def inmenu(started):

    helpMenu = 0
    if started == 0:
        DISPLAY.blit(menu_img, (0, 0))
    else:
        DISPLAY.blit(pause_img, (0, 0))

    while menu == 1:
        if quit_button.draw(DISPLAY):
            back_sound.play()
            pygame.quit()
            sys.exit()
        if play_button.draw(DISPLAY):
            pygame.mixer.music.stop()
            button_sound.play()
            return

        if helpMenu == 1:
            DISPLAY.blit(info_img, (0, 0))

        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if helpMenu == 1:
            if back_button.draw(DISPLAY):
                back_sound.play()
                helpMenu = 0
                if started == 0:
                    DISPLAY.blit(menu_img, (0, 0))
                else:
                    # set to what it was like before
                    DISPLAY.fill((50, 50, 100))
                    DISPLAY.blit(pause_img, (0, 0))
        else:
            if info_button.draw(DISPLAY):
                button_sound.play()
                helpMenu = 1

        pygame.display.update()


# main
def main():
    global menu, lives, highscore, alive
    pygame.init()
    # load assets ------------------------------------------
    pygame.display.set_caption("Platformer")
    # pygame.mixer.music.play(-1)
    hit_sound = pygame.mixer.Sound("hit.wav")
    coin_sound = pygame.mixer.Sound("coin.wav")
    jump_sound = pygame.mixer.Sound("jump.wav")

    Lighting = pygame.image.load('light.png')
    BG = pygame.image.load('BG.jpg')
    coin = pygame.image.load('Coin.png')
    Darkness = pygame.image.load('Darkness.jpg')
    floor = pygame.image.load('Ground.png')
    player = pygame.image.load('Player.png')
    player2 = pygame.image.load('Player2.jpg')
    hitboxN = pygame.image.load('HitboxNorth.png')
    hitboxE = pygame.image.load('HitboxEast.png')
    hitboxS = pygame.image.load('HitboxSouth.png')
    hitboxW = pygame.image.load('HitboxWest.png')
    box1 = pygame.image.load('box1.png')
    cogA_img = pygame.image.load('cog1.png')
    cogB_img = pygame.image.load('cog2.png')
    health3 = pygame.image.load('Heart3.png')
    health2 = pygame.image.load('Heart2.png')
    health1 = pygame.image.load('Heart1.png')

    # define variables ---------------------------------------
    particles = []
    # hitbox = Hitbox()

    hitboxNX = 0
    hitboxNY = 0
    hitboxNW = 40
    hitboxNH = 2
    hitboxEX = 0
    hitboxEY = 0
    hitboxEW = 2
    hitboxEH = 40
    hitboxSX = 0
    hitboxSY = 0
    hitboxSW = 32
    hitboxSH = 2
    hitboxWX = 0
    hitboxWY = 0
    hitboxWW = 2
    hitboxWH = 40
    cogW = 40
    cogH = 40
    cog1X = 477
    cog1Y = 477
    box1X = 422
    box1Y = 497
    box1W = 180
    box1H = 60
    northC = 0
    eastC = 0
    southC = 0
    westC = 0
    coins = 0
    coinX = random.randint(0, 1024)
    coinY = random.randint(416, 500)
    coinW = 16
    coinH = 16
    playerX = 20
    playerY = 516
    playerWidth = 40
    playerHeight = 40
    floorX = 0
    floorY = 550
    velocityX = 0
    velocityY = 0
    left = 0
    showHitbox = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    coinsText = '0'
    turn = 0
    alive = 1
    # colours
    GREY = (19, 19, 19)
    WHITE = (255, 255, 255)
    text = font.render(coinsText, True, WHITE, GREY)
    textRect = text.get_rect()

    # other setup
    DISPLAY.fill(WHITE)
    pygame.draw.rect(DISPLAY, GREY, [0, 576, 1024, 26])
    DISPLAY.blit(BG, (0, 0))
    DISPLAY.blit(Darkness, (0, 0))
    DISPLAY.blit(player, (playerX, playerY))
    inmenu(0)
    menu = 0

    # game (runs in while true loop) --------------------------
    while True:
        # setup
        DISPLAY.fill(WHITE)
        DISPLAY.blit(BG, (0, 0))
        pygame.draw.rect(DISPLAY, GREY, [0, 550, 1024, 26])
        if turn == 0:
            DISPLAY.blit(cogA_img, (cog1X, cog1Y))
            turn = 1
        else:
            DISPLAY.blit(cogB_img, (cog1X, cog1Y))
            turn = 0
        DISPLAY.blit(floor, (floorX, floorY))
        DISPLAY.blit(text, textRect)
        DISPLAY.blit(box1, (box1X, box1Y))
        text = font.render(coinsText, True, WHITE)
        textRect = text.get_rect()
        coinsText = str(coins)
        hitboxNX = playerX
        hitboxNY = playerY - 2
        hitboxEX = playerX + 40
        hitboxEY = playerY
        hitboxSX = playerX + 4
        hitboxSY = playerY + 40
        hitboxS2Y = playerY + 41
        hitboxWX = playerX - 2
        hitboxWY = playerY
        pygame.display.set_caption("Game")

        # hitbox check
        if 1 == 1:
            northC = 0
            eastC = 0
            southC = 0
            southC2 = 0
            westC = 0
            if collisions_any(box1X, box1Y, box1W, box1H, hitboxNX, hitboxNY, hitboxNW, hitboxNH) == 1:
                northC = 1

            if collisions_any(box1X, box1Y, box1W, box1H, hitboxEX, hitboxEY, hitboxEW, hitboxEH) == 1:
                eastC = 1

            if collisions_any(box1X, box1Y, box1W, box1H, hitboxSX, hitboxSY, hitboxSW, hitboxSH) == 1:
                southC = 1
                playerY = box1Y - 40

            if collisions_any(box1X, box1Y, box1W, box1H, hitboxSX, hitboxS2Y, hitboxSW, hitboxSH) == 1:
                southC2 = 1

            if collisions_any(box1X, box1Y, box1W, box1H, hitboxWX, hitboxWY, hitboxWW, hitboxWH) == 1:
                westC = 1

        # coin collisions / getting coins ----------------------
        if collisions_any(playerX, playerY, playerWidth, playerHeight, coinX, coinY, coinW, coinH) == 1:
            for i in range(40):
                particles.append(
                    [[coinX + 8, coinY + 8], [random.randint(0, 20) / 10 - 1, -2], random.randint(2, 10)])
            coinX = random.randint(0, 1024)
            coinY = random.randint(416, 500)
            coin_sound.play()
            DISPLAY.blit(coin, (coinX, coinY))
            coins = coins + 1

        # box collision ----------------------------------------
        if collisions_any(box1X, box1Y, box1W, box1H, coinX, coinY, coinW, coinH):
            coinX = random.randint(0, 1024)
            coinY = random.randint(416, 500)

        # if hitbox collision
        if northC == 1:
            velocityY = 3
            playerY = playerY + 5
            hit_sound.play()

        if westC == 1:
            playerX = playerX + 1
            velocityX = 0

        if eastC == 1:
            playerX = playerX - 1
            velocityX = 0

        if southC == 1:
            velocityY = 0
            playerY = playerY - 1

        DISPLAY.blit(coin, (coinX, coinY))

        # lighting (Blend RGB add makes the RGB values of the image add to the things below it making a lighting
        # effect)
        DISPLAY.blit(Lighting, (playerX + 20 - 256 / 2, playerY + 20 - 256 / 2), special_flags=BLEND_RGB_ADD)

        # display player looking left or right -----------------
        if left == 0:
            DISPLAY.blit(player, (playerX, playerY))
        else:
            DISPLAY.blit(player2, (playerX, playerY))

        # Hitbox Display
        if showHitbox == 1:
            DISPLAY.blit(hitboxN, (hitboxNX, hitboxNY))
            DISPLAY.blit(hitboxE, (hitboxEX, hitboxEY))
            DISPLAY.blit(hitboxS, (playerX, hitboxSY))
            DISPLAY.blit(hitboxW, (hitboxWX, hitboxWY))

        # particle effects ------------------------------------
        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.1
            pygame.draw.circle(DISPLAY, (255, 255, 0), [int(particle[0][0]), int(particle[0][1])],
                               int(particle[2]))
            if particle[2] <= 0:
                particles.remove(particle)

        # movement (velocity calculations) --------------------
        playerX = playerX + velocityX
        playerY = playerY + velocityY
        velocityX = velocityX * 0.81

        if playerX > 984:
            hit_sound.play()
            velocityX = 0
            playerX = 984

        if playerX < 0:
            hit_sound.play()
            velocityX = 0
            playerX = 0

        if playerY < 516 and southC == 0 and southC2 == 0 and velocityY < 10:
            velocityY = velocityY + 1

        if playerY > 516:
            hit_sound.play()
            velocityY = 0
            playerY = 516
            particles.append(
                [[playerX + 20, playerY + 40], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])
            particles.append(
                [[playerX + 20, playerY + 40], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])

        keys = pygame.key.get_pressed()

        # move right -------------------------------------------
        if keys[pygame.K_d]:
            if eastC == 0:
                velocityX = velocityX + 1
            left = 0

        # move left --------------------------------------------
        if keys[pygame.K_a]:
            if westC == 0:
                velocityX = velocityX - 1
            left = 1

        # event ------------------------------------------------
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Jump --------------------------------------------
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    if playerY == 516 or southC == 1 or southC2 == 1:
                        playerY = playerY - 1
                        jump_sound.play()
                        velocityY = velocityY - 14
                        particles.append(
                            [[playerX + 20, playerY + 40], [random.randint(0, 20) / 10 - 1, -2],
                             random.randint(2, 4)])
                        particles.append(
                            [[playerX + 20, playerY + 40], [random.randint(0, 20) / 10 - 1, -2],
                             random.randint(2, 4)])

            # Toggle hitboxes ---------------------------------
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_h]:
                    if showHitbox == 1:
                        showHitbox = 0
                    else:
                        showHitbox = 1

            # if esc pressed go to menu ----------------------
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    back_sound.play()
                    pygame.mixer.music.play(-1)
                    menu = 1
                    inmenu(1)
                    menu = 0

        if lives == 3:
            DISPLAY.blit(health3, (826, 0))
        elif lives == 2:
            DISPLAY.blit(health2, (826, 0))
        else:
            DISPLAY.blit(health1, (826, 0))

        if collisions_any(playerX, playerY, playerWidth, playerHeight, cog1X, cog1Y, cogW, cogH):
            if lives == 1:
                alive = 0
                lives = 3
                if coins > highscore:
                    highscore = coins
                DISPLAY.blit(death_img, (0, 0))
                pygame.display.update()
                pygame.quit()
                sys.exit()

            else:
                lives = lives - 1
                playerY = 516
                playerX = 20

        # update the display
        pygame.display.update()
        pygame.time.delay(10)


# runs the program
main()
