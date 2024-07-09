import pygame
import initialize
from game import Game

logger, screen, clock, scoreFont = initialize.init()
game = Game(screen, scoreFont)

game.run()


