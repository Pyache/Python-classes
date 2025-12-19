import pygame
import random
import math
import time

pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Best Game by Talin")
background = pygame.image.load('road.png')
background = pygame.transform.scale(background, (700, 500))
icon = pygame.image.load('game_icon.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player_sprite.png')
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 37
playerY = 38
playerX_change = 0
playerY_change = 0
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 3

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_change_timer = []
num_of_enemies = 4

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 636))
    enemyY.append(random.randint(50, 400))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(random.choice([-ENEMY_SPEED_Y, ENEMY_SPEED_Y]))
    enemy_change_timer.append(time.time() + random.uniform(1, 3))
font = pygame.font.Font(None, 32)
over_font = pygame.font.Font(None, 64)
score_value = 0

def player(x, y):
    screen.blit(playerImg, (x, y))
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (200, 250))
def is_collision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt((enemyX - playerX)**2 + (enemyY - playerY)**2)
    return distance < 27
clock = pygame.time.Clock()
running = True
game_over = False

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                playerY_change = 5
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                playerX_change = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                playerY_change = 0

    if not game_over:
        playerX += playerX_change
        playerY += playerY_change
        playerX = max(0, min(playerX, 636))
        playerY = max(0, min(playerY, 436))
        for i in range(num_of_enemies):
            enemyX[i] += enemyX_change[i]
            enemyY[i] += enemyY_change[i]
            if enemyX[i] <= 0 or enemyX[i] >= 636:
                enemyX_change[i] *= -1
            if enemyY[i] <= 0 or enemyY[i] >= 436:
                enemyY_change[i] *= -1
            current_time = time.time()
            if current_time > enemy_change_timer[i]:
                enemyY_change[i] *= random.choice([-1, 1])
                enemy_change_timer[i] = current_time + random.uniform(1, 3)
            if is_collision(enemyX[i], enemyY[i], playerX, playerY):
                game_over = True
            enemy(enemyX[i], enemyY[i], i)
        player(playerX, playerY)
        show_score(10, 10)
        score_value += 1
    else:
        game_over_text()
    pygame.display.update()
    clock.tick(60)
pygame.quit()