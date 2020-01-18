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
enemyImg = []
enemyX = []
enemyY = []
enemyX_Change = []
enemyY_Change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pg.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_Change.append(0.1)
    enemyY_Change.append(40)

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
font = pg.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


def showScore(x, y):
    scr = font.render("Score : " + str(score), True, (0, 255, 0))
    screen.blit(scr, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


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
    # Checking boundary of enemy and movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_Change[i]
        if enemyX[i] <= 0:
            enemyX_Change[i] = 0.1
            enemyY[i] += enemyY_Change[i]
        # Spaceship size 64 x 64
        elif enemyX[i] > 736:
            enemyX_Change[i] = -0.1
            enemyY[i] += enemyY_Change[i]

        # Collided or not
        collision = isCollided(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
            print(score)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_Change

    player(playerX, playerY)
    showScore(textX, textY)
    # Each Time game window should update
    pg.display.update()
