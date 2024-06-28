import pygame
import math
import initialize
import resources

class Snake:

    hasEaten = False
    alive = True
    
    def __init__(self) -> None:
        self.speed = 200
        self.direction = 'N'
        # put the snake in the center of the screen to start
        xIdx = math.floor(len(initialize.xVals)/2)
        yIdx = math.floor(len(initialize.yVals)/2)
        self.body = [snakeSegment(initialize.xVals[xIdx], initialize.yVals[yIdx])]

    def draw(self, screen):
        for segment in self.body:
            x, y = resources.setLocation(segment.x, segment.y, initialize.snakeSize)
            pygame.draw.rect(
                screen,
                initialize.white,
                pygame.Rect(
                    x,
                    y,
                    initialize.snakeSize,
                    initialize.snakeSize))
        pygame.display.flip()

    def move(self):
        # determine the coordinates for where the head needs to go
        newHead = snakeSegment(self.body[0].x, self.body[0].y)
        match self.direction:
            case 'N':
                newHead.y -= 1
            case 'S':
                newHead.y += 1
            case 'E':
                newHead.x += 1
            case 'W':
                newHead.x -= 1
        
        # attach the new head to the snake
        self.body.insert(0, newHead)

        # if we didn't just eat a pellet, delete the back segment
        if not self.hasEaten:
            self.body = self.body[:-1]

        self.hasEaten = False

    def checkForDeath(self):
        # check if the snake has gone off the screen
        if self.body[0].x not in initialize.xVals \
        or self.body[0].y not in initialize.yVals:
            self.alive = False
        # check if the snake has run into itself
        if len(self.body) >= 5:
            for segment in self.body[4:]:
                if self.body[0].x == segment.x \
                and self.body[0].y == segment.y:
                    self.alive = False


class snakeSegment:
    x = float(0)
    y = float(0)

    def __init__(self, x, y):
        self.x = x
        self.y = y