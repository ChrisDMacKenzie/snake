import constants
import pygame

def drawGameSurface():
    gameSurface = pygame.Surface(constants.SCREEN_SIZE)
    gameSurface.fill(constants.BLACK)
    
    titleImg = pygame.image.load('assets/images/gameScreenTitle.png')
    tiRect = titleImg.get_rect()
    tiRect.bottomleft = constants.OUTSIDE_BORDER_WIDTH, \
        tiRect.height + (constants.TITLE_REGION_HEIGHT - tiRect.height) / 2
    gameSurface.blit(titleImg, tiRect)
    
    scoreImg = pygame.image.load('assets/images/gameScore.png')
    scoreRect = scoreImg.get_rect()
    scoreRect.bottomright = constants.WIDTH - constants.SCORE_WIDTH, \
        scoreRect.height + (constants.TITLE_REGION_HEIGHT - scoreRect.height) / 2
    gameSurface.blit(scoreImg, scoreRect)
    
    pygame.draw.rect(
                gameSurface,
                constants.WHITE,
                pygame.Rect(
                    constants.OUTSIDE_BORDER_WIDTH,
                    constants.TITLE_REGION_HEIGHT,
                    constants.WIDTH - (constants.OUTSIDE_BORDER_WIDTH * 2),
                    constants.HEIGHT -(constants.TITLE_REGION_HEIGHT + constants.OUTSIDE_BORDER_WIDTH)),
                    constants.GAME_BORDER_WIDTH)

    return gameSurface