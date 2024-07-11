import pygame
import constants

def drawScoreSurface(screen, score, enterScoreFont, scoreFont):
    # erase the old screen
    screen.fill(constants.BLACK)

    scoreDispStr = "SCORE: "
    ScoreDispObj = enterScoreFont.render(scoreDispStr, True, (constants.WHITE))
    ScoreDispObjRect = ScoreDispObj.get_rect()
    ScoreDispObjRect.center = (500, 280)
    screen.blit(ScoreDispObj, ScoreDispObjRect)

    scoreStr = str(score)
    scoreObj = scoreFont.render(scoreStr, True, (constants.WHITE))
    scoreObjRect = scoreObj.get_rect()
    scoreObjRect.center = (600, 280)
    screen.blit(scoreObj, scoreObjRect)

    enterStr = "Enter your initials: "
    enterObj = enterScoreFont.render(enterStr, True, (constants.WHITE))
    enterObjRect = enterObj.get_rect()
    enterObjRect.center = (500, 330)
    screen.blit(enterObj, enterObjRect)
    pygame.display.update()
    getPlayerInits(screen, enterScoreFont)

def getPlayerInits(screen, enterScoreFont):
    inits = ""
    charXpos = 680
    enteringInits = True
    while enteringInits:
        if pygame.event.get(pygame.QUIT): break
        
        # get player inits, only allow alpha chars
        for keyPress in pygame.event.get():
            if keyPress.type == pygame.KEYDOWN:
                if keyPress.key >= 97 and keyPress.key <= 122 and len(inits) < 3:
                    character = chr(keyPress.key).upper()
                    inits += character
                    charObj = enterScoreFont.render(character, True, (constants.WHITE))
                    charObjRect = charObj.get_rect()
                    charObjRect.center = (charXpos, 330)
                    charXpos += charObjRect.width + 5
                    screen.blit(charObj, charObjRect)
                    pygame.display.update()
                if keyPress.key == pygame.K_BACKSPACE and len(inits) > 0:
                    inits = ""
                    charXpos = 680
                    screen.fill(
                    constants.BLACK,
                        (
                            charXpos - 17,
                            330 - 18,
                            250,
                            36)
                    )
                    pygame.display.update()
                if keyPress.key in [pygame.K_KP_ENTER, pygame.K_RETURN] and len(inits) in range(1, 4):
                    enteringInits = False
