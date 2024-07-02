import initialize
from game import Game

logger, screen, clock = initialize.init()
game = Game(screen)

game.run()


