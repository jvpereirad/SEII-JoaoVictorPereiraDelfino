import pygame
import random
from pygame.locals import *

pygame.init()

def on_grid_randon():
    x = random.randint(0, 590)
    y = random.randint(0, 590)

    return ((x // 10) * 10, (y // 10) * 10)

def collision(c1, c2):
    return(c1[0] == c2[0] and c1[1] == c2[1])

def collision_head(snake):
    return (snake[0] in snake[2:])

screen_resolution = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

UP = 5
RIGHT = 3
DOWN = 2
LEFT = 1

snake = [(200, 200), (210, 200), (220, 200)] * 1
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

apple_pos = on_grid_randon()

direction = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    if event.type == KEYDOWN:
        if event.key == K_UP:
            direction = UP

        if event.key == K_DOWN:
            direction = DOWN
        
        if event.key == K_LEFT:
            direction = LEFT
        
        if event.key == K_RIGHT:
            direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_randon()
        snake.append((0,0))

    if len(snake) > 5:
        if collision_head(snake):
            #print('FIM DE JOGO')
            pygame.quit()


    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    
    if direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    
    if direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    
    if direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen_resolution.fill((0, 0, 0))
    screen_resolution.blit(apple, apple_pos)

    for pos in snake:
        screen_resolution.blit(snake_skin, pos)

    pygame.display.update()
