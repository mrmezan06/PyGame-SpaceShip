import pygame as pg

# Initializing py game
pg.init()
# Screen set
screen = pg.display.set_mode((800, 600))

# Title and Icon
pg.display.set_caption("Space X")
icon = pg.image.load('spaceship.png')
pg.display.set_icon(icon)

# Player
playerImg = pg.image.load('player.png')
playerX = 370
playerY = 480
playerX_Change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))

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
    player(playerX, playerY)
    # Each Time game window should update
    pg.display.update()
