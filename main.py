import pygame
import logging
import sys
import initialize
import time
from snake import Snake
from food import Food
from update import update


logger, screen, clock = initialize.init()
snake = Snake()
food = Food(snake)
MOVEEVENT = pygame.USEREVENT+1
pygame.time.set_timer(MOVEEVENT, snake.speed)

while snake.alive:
    if pygame.event.get(pygame.QUIT): break
    
    keys = pygame.key.get_pressed()
    for e in pygame.event.get():
        if e.type == MOVEEVENT:
            if (keys[pygame.K_w] or keys[pygame.K_UP]) and (snake.direction not in ['N', 'S']):
                # logger.debug("changing direction to north")
                snake.direction = 'N'
            elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and (snake.direction not in ['N', 'S']):
                # logger.debug("changing direction to south")
                snake.direction = 'S'
            elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and (snake.direction not in ['E', 'W']):
                # logger.debug("changing direction to west")
                snake.direction = 'W'
            elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and (snake.direction not in ['E', 'W']):
                # logger.debug("changing direction to east")
                snake.direction = 'E'
            update(screen, snake, food, MOVEEVENT)
    
    screen.fill(initialize.black)
