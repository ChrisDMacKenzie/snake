import logging
import pygame

# we gotta establish a grid system so everything lines up
size = width, height = 1280, 720
gridSize = 20
xVals = list(range(0, int(width/gridSize), 1))
yVals = list(range(0, int(height/gridSize), 1))

# set the size of the game objects
snakeSize = gridSize - 2
foodSize = gridSize - 4

#some colors 
black = 0, 0, 0
white = 255, 255, 255
blue = 0, 0, 255

def init():
    pygame.init()
    
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    screen = pygame.display.set_mode(size)
    logger.debug("initialized game screen")
    
    clock = pygame.time.Clock()

    return logger, screen, clock