import pygame as pg
import random
import math

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

# Enemy
enemyImg = pg.image.load('enemy.png')
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_Change = 0.1
enemyY_Change = 40

# Bullet
# ready - invisible bullet
# fire - bullet is currently moving
bulletImg = pg.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_Change = 0
bulletY_Change = 1
bullet_state = "ready"

# Score
score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollided(en_x, en_y, bul_x, bul_y):
    distance = math.sqrt(math.pow((en_x - bul_x), 2) + math.pow((en_y - bul_y), 2))
    if distance < 27:
        return True
    else:
        return False


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
                playerX_Change = -0.2
            if event.key == pg.K_RIGHT:
                # print("Right Arrow Pressed!")
                playerX_Change = 0.2
            if event.key == pg.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
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

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_Change

    # Collided or not
    collision = isCollided(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)
        print(score)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    # Each Time game window should update
    pg.display.update()
