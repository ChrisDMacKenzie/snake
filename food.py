import pygame
import random
import math
import initialize
import resources
from snake import Snake

class Food:
    # used so we don't spawn the food on top of the snake
    inSnake = True
    
    # food location
    x = float(0)
    y = float(0)

    # randomize the location on first spawn, make sure it's not on top of the snake
    def __init__(self, Snake):
        while self.inSnake:
            self.placeFood()
            self.checkSnakeLocation(Snake)
        
        
    def draw(self, screen):    
        x, y = resources.setLocation(self.x, self.y, initialize.foodSize)
        pygame.draw.rect(
            screen,
            initialize.blue,
            pygame.Rect(
                    x,
                    y,
                    initialize.foodSize,
                    initialize.foodSize))
        pygame.display.flip()
    
    def checkSnakeLocation(self, Snake):
        for segment in Snake.body:
            if self.x == segment.x \
            and self.y == segment.y:
                self.inSnake = True
                break

    def placeFood(self):
        self.inSnake = False
        self.x = initialize.xVals[random.randint(0, len(initialize.xVals) - 1)]
        self.y = initialize.yVals[random.randint(0, len(initialize.yVals) - 1)]


    def checkIfEaten(self, snake):
        if self.x == snake.body[0].x \
            and self.y == snake.body[0].y:
                self.inSnake = True
                snake.hasEaten = True
                while self.inSnake:
                    self.placeFood()
                    self.checkSnakeLocation(snake)