
import pygame
from snake import Snake

def update(screen, snake, food, MOVEEVENT):
    food.draw(screen)
    snake.draw(screen)
    snake.checkForDeath()
    food.checkIfEaten(snake)
    # if the snake just ate and the speed isn't already too fast,
    # speed up the snake
    if snake.hasEaten and snake.speed >= 10:
        snake.speed -= 2
        pygame.time.set_timer(MOVEEVENT, snake.speed)
    snake.move()