import pygame
import random

pygame.init()

SCREEN = pygame.display.set_mode((500, 750))

Bg_Img = pygame.image.load('background.jpg')

Bird_Img = pygame.image.load('Spare Bird.png')
Bird_x = 50
Bird_y = 300
Bird_y_change = 0

def display_bird(x, y):
    SCREEN.blit(Bird_Img, (x, y))

OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(150,450)
OBSTACLE_COLOR = (211, 253, 117)
OBSTACE_X_CHANGE = -0.4
obstacle_x = 500

def display_obstacle(height):
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    bottom_obstacle_height = 520 - height - 1200
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 622, OBSTACLE_WIDTH, -bottom_obstacle_height))

def collision_detection (obstacle_x, obstacle_height, Bird_y, bottom_obstacle_height):
    if obstacle_x >= 50 and obstacle_x <= (50 + 64):
        if Bird_y <= obstacle_height  or Bird_y >= (bottom_obstacle_height ):
            return True
    return False

score = 0
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 32)

def score_display(score):
    display = SCORE_FONT.render(f"Score: {score}", True, (255,255,255))
    SCREEN.blit(display, (10, 10))

startFont = pygame.font.Font('freesansbold.ttf', 32)
def start():
    display = startFont.render(f"PRESS SPACE BAR TO START", True, (255, 255, 255))
    SCREEN.blit(display, (20, 200))
    pygame.display.update()

score_list = [0]

game_over_font1 = pygame.font.Font('freesansbold.ttf', 64)
game_over_font2 = pygame.font.Font('freesansbold.ttf', 32)

def game_over():
    maximum = max(score_list)
    display1 = game_over_font1.render(f"GAME OVER", True, (200,35,35))
    SCREEN.blit(display1, (50, 300))
    display2 = game_over_font2.render(f"SCORE: {score} MAX SCORE: {maximum}", True, (255, 255, 255))
    SCREEN.blit(display2, (50, 400))
    if score == maximum:
        display3 = game_over_font2.render(f"NEW HIGH SCORE!!", True, (200,35,35))
        SCREEN.blit(display3, (80, 100))

running = True
waiting = True
collision = False

while running:

    SCREEN.fill((0, 0, 0))

    SCREEN.blit(Bg_Img, (0, 0))

    while waiting:
        if collision:
            game_over()
            start()
        else:
            start()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score = 0
                    Bird_y = 300
                    obstacle_x = 500
                    waiting = False

            if event.type == pygame.QUIT:
                waiting = False
                running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Bird_y_change = -0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                Bird_y_change = 0.2


    Bird_y += Bird_y_change

    if Bird_y <= -60:
        Bird_y = -60
    if Bird_y >= 522:
        Bird_y = 522


    obstacle_x += OBSTACE_X_CHANGE


    collision = collision_detection(obstacle_x, OBSTACLE_HEIGHT, Bird_y, OBSTACLE_HEIGHT + 150)

    if collision:

        score_list.append(score)
        waiting = True


    if obstacle_x <= -10:
        obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(200, 400)
        score += 1

    display_obstacle(OBSTACLE_HEIGHT)


    display_bird(Bird_x, Bird_y)


    score_display(score)


    pygame.display.update()


pygame.quit()