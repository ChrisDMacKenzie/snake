import pygame
import logging
import sys
import initialize
import constants
import time
from snake import Snake
from food import Food
from game import Game


logger, screen, clock = initialize.init()
game = Game(screen)

game.run()


