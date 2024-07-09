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

    scoreFont = pygame.font.Font('fonts/Seven Segment.ttf', 60)

    return logger, screen, clock, scoreFont