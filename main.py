import initialize
import scoreSurface
from game import Game

logger, screen, clock, scoreFont, enterScoreFont = initialize.init()
session = initialize.initDB()
game = Game(screen, scoreFont)
score = game.run()
scoreSurface.drawScoreSurface(screen, score, session, enterScoreFont, scoreFont)




