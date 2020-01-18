import pygame as pg
import random

# Initializing py game
pg.init()
# Screen set
screen = pg.display.set_mode((800, 600))
# Adding Background
bg = pg.image.load('background.png')

# Title and Icon
pg.display.set_caption("Space X")
icon = pg.image.load('spaceship.png')
pg.display.set_icon(icon)

# Player
playerImg = pg.image.load('player.png')
playerX = 370
playerY = 480
playerX_Change = 0

# Player
enemyImg = pg.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_Change = 0.1
enemyY_Change = 40


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    # background image
    screen.blit(bg, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # key Stroke is pressed then check whether its right or left
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                # print("Left Arrow Pressed!")
                playerX_Change = -0.1
            if event.key == pg.K_RIGHT:
                # print("Right Arrow Pressed!")
                playerX_Change = 0.1
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                # print("Key Stroke has been released!")
                playerX_Change = 0
    playerX += playerX_Change
    if playerX <= 0:
        playerX = 0
    # Spaceship size 64 x 64
    if playerX > 736:
        playerX = 736
    # Checking boundary of enemy
    enemyX += enemyX_Change
    if enemyX <= 0:
        enemyX_Change = 0.1
        enemyY += enemyY_Change
    # Spaceship size 64 x 64
    if enemyX > 736:
        enemyX_Change = -0.1
        enemyY += enemyY_Change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    # Each Time game window should update
    pg.display.update()
