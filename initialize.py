import logging
import sqlalchemy as sa
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
    EnterScoreFont = pygame.font.Font('fonts/Tomorrow-Regular.ttf', 36)

    return logger, screen, clock, scoreFont, EnterScoreFont

def initDB():
    return sa.create_engine(
        url="mysql+pymysql://user:password@localhost:3306/snake_game"
    )