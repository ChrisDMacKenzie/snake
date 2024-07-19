import pygame
import constants
from sqlalchemy import select
from model.scores import Score
from model.base import Base

def drawHighScoresSurface(screen, score, session, enterScoreFont, scoreFont):
    # erase the old screen
    screen.fill(constants.BLACK)

    highScoreStr = "HIGH SCORES"
    highScoreObj = enterScoreFont.render(highScoreStr, True, (constants.WHITE))
    highScoreObjRect = highScoreObj.get_rect()
    highScoreObjRect.center = (640, 50)
    screen.blit(highScoreObj, highScoreObjRect)
    
    highScores = getHighScores(session)
    writeHighScores(screen, highScores, enterScoreFont, scoreFont)
    
    pygame.display.update()

    viewingHighScores = True
    while viewingHighScores:
        if pygame.event.get(pygame.QUIT): break
        # exit the game on any key press
        for keyPress in pygame.event.get():
            if keyPress.type == pygame.KEYDOWN:
                viewingHighScores = False
    
def getHighScores(session):
    stmt = (
        select(Score.initials, Score.score)
        .order_by(Score.score.desc())
        .limit(5)
    )
    results = session.execute(stmt)
    return results

def writeHighScores(screen, highScores, enterScoreFont, scoreFont):
    ypos = 150
    for row in highScores:
        initsStr = row.initials
        initsObj = enterScoreFont.render(initsStr, True, (constants.WHITE))
        initsObjRect = initsObj.get_rect()
        initsObjRect.center = (520, ypos)
        screen.blit(initsObj, initsObjRect)

        scoreStr = str(row.score)
        scoreObj = scoreFont.render(scoreStr, True, (constants.WHITE))
        scoreObjRect = scoreObj.get_rect()
        scoreObjRect.center = (750, ypos)
        screen.blit(scoreObj, scoreObjRect)

        ypos += 70
