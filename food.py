import pygame
import random
import constants
import resources

class Food:
    
    # food location
    x = float(0)
    y = float(0)

    # randomize the location on first spawn
    def __init__(self):
            self.placeFood()
        
        
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

    def placeFood(self):
        self.x = constants.X_VALS[random.randint(0, len(constants.X_VALS) - 1)]
        self.y = constants.Y_VALS[random.randint(0, len(constants.Y_VALS) - 1)]