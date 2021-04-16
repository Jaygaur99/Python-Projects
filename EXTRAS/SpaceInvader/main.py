import pygame
import random
import math
from pygame import mixer

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))  # Setting the height and width of the screen

# Adding Background
background = pygame.image.load('background.jpg')

# Background Music
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("spaceship.png")
playerX = 395
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 10

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("monster.png"))
    enemyX.append(random.randint(0, 765))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# Bullet (States :- Ready = Cant see the bullet, Fire = Firing bullet)
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1.5
bullet_state = "ready"

# Score
score_value = 0
font_score = pygame.font.Font('Ragila.otf', 32)
textX = 10
textY = 10


def show_score(x, y):
    score = font_score.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 6, y + 5))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if  distance < 27:
        return True
    return False


# Game Over
over_font = pygame.font.Font('Ragila.otf', 64)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text,(250, 250))


# Game Loop
running = True
while running:

    # RGB
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.6
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.6
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    # Making Boundaries
    if playerX <= 0:
        playerX = 0
    if playerX >= 765:
        playerX = 765

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        # Enemy Movement
        enemyX[i] += enemyX_change[i]
        if enemyX[i] >= 770:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
        if enemyX[i] <= 0:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = 0.3

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound('explosion.wav')
            collision_sound.play()
            bullet_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0, 765)
            enemyY[i] = random.randint(50, 150)

        # Making Enemy
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == 'ready':
        bulletY = playerY

    # Making player on the Screen by calling a function
    player(playerX, playerY)
    show_score(textX, textY)
    # Update Screen otherwise screen will hang
    pygame.display.update()
