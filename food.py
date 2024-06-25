import pygame
import initialize
import random
import math
from snake import Snake, segmentSize

foodSize = 16

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
        pygame.draw.rect(
            screen,
            "blue",
            pygame.Rect(
                    self.x,
                    self.y,
                    foodSize,
                    foodSize))
        pygame.display.flip()
    
    def checkSnakeLocation(self, Snake):
        for segment in Snake.body:
            if self.x in range(int(segment.x), int(segment.x + segmentSize)) \
            and self.y in range(int(segment.y), int(segment.y + segmentSize)):
                self.inSnake = True
                break

    def placeFood(self):
        self.inSnake = False
        self.x = random.randint(0, math.floor(initialize.width-(foodSize/2)))
        self.y = random.randint(0, math.floor(initialize.height-(foodSize/2)))
        print(self.x, self.y)


    def checkIfEaten(self, Snake):
        if self.x in range(int(Snake.body[0].x), int(Snake.body[0].x + segmentSize)) \
            and self.y in range(int(Snake.body[0].y), int(Snake.body[0].y + segmentSize)):
                self.inSnake = True
                Snake.hasEaten = True
                while self.inSnake:
                    self.placeFood()
                    self.checkSnakeLocation(Snake)
                for segment in Snake.body:
                    print(segment.x, segment.y)