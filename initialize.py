import logging
import sqlalchemy as sa
import pygame
import constants
import os

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
    ENDPOINT="snakegamedb.clqkgwy8krgw.us-east-1.rds.amazonaws.com"
    PORT=3306
    USER= os.getenv("SNAKE_DB_USER")
    PASSWORD = os.getenv("SNAKE_DB_PASSWORD")
    DBNAME="snake_game"

    try:
        url = "mysql+pymysql://{}:{}@{}:{}/{}".format(USER, PASSWORD, ENDPOINT, PORT, DBNAME)
        return sa.create_engine(url=url)
    except Exception as e:
        print("Database connection failed due to {}".format(e))