import logging
import pygame

size = width, height = 1280, 720
black = 0, 0, 0

def init():
    pygame.init()
    
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    screen = pygame.display.set_mode(size)
    logger.debug("initialized game screen")
    
    clock = pygame.time.Clock()

    return logger, screen, clock