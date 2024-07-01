import logging
import pygame
import constants

def init():
    pygame.init()
    
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    screen = pygame.display.set_mode(constants.SCREEN_SIZE)
    logger.debug("initialized game screen")
    
    clock = pygame.time.Clock()

    return logger, screen, clock