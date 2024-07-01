import pygame
import random
import constants
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
        x, y = resources.setLocation(self.x, self.y, constants.FOOD_SIZE)
        pygame.draw.rect(
            screen,
            constants.BLUE,
            pygame.Rect(
                    x,
                    y,
                    constants.FOOD_SIZE,
                    constants.FOOD_SIZE))
        pygame.display.flip()
    
    def checkSnakeLocation(self, Snake):
        for segment in Snake.body:
            if self.x == segment.x \
            and self.y == segment.y:
                self.inSnake = True
                break

    def placeFood(self):
        self.inSnake = False
        self.x = constants.X_VALS[random.randint(0, len(constants.X_VALS) - 1)]
        self.y = constants.Y_VALS[random.randint(0, len(constants.Y_VALS) - 1)]


    def checkIfEaten(self, snake):
        if self.x == snake.body[0].x \
            and self.y == snake.body[0].y:
                self.inSnake = True
                snake.hasEaten = True
                while self.inSnake:
                    self.placeFood()
                    self.checkSnakeLocation(snake)