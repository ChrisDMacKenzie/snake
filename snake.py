import pygame
import math
import constants
import resources

class Snake:

    # some boolean vals to hold the state of the snake
    needsFood = True
    needsToExtend = False
    alive = True
    
    def __init__(self) -> None:
        self.speed = 150
        self.direction = 'INIT'
        # put the snake in the center of the screen to start
        xIdx = math.floor(len(constants.X_VALS)/2)
        yIdx = math.floor(len(constants.Y_VALS)/2)
        self.body = [snakeSegment(constants.X_VALS[xIdx], constants.Y_VALS[yIdx])]

    def draw(self, screen):
        for segment in self.body:
            x, y = resources.setLocation(segment.x, segment.y, constants.SNAKE_SIZE)
            pygame.draw.rect(
                screen,
                constants.WHITE,
                pygame.Rect(
                    x,
                    y,
                    constants.SNAKE_SIZE,
                    constants.SNAKE_SIZE))

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
        if not self.needsToExtend:
            self.body = self.body[:-1]

        self.needsToExtend = False

    def checkForDeath(self):
        # check if the snake has gone off the screen
        if self.body[0].x not in constants.X_VALS \
        or self.body[0].y not in constants.Y_VALS:
            self.alive = False
        # check if the snake has run into itself
        if len(self.body) >= 5:
            for segment in self.body[4:]:
                if self.body[0].x == segment.x \
                and self.body[0].y == segment.y:
                    self.alive = False

    # speeds up the snake once it's eaten food
    def speedUp(self,  moveEvent):
        if self.speed >= 10:
            self.speed -= 2
            pygame.time.set_timer(moveEvent, self.speed)

    # play a quick little animation when dead before going to the high score screen
    def playDeathAnimation(self, screen):
        # get location of where the explosion needs to go
        x, y = resources.setLocation(self.body[0].x, self.body[0].y, constants.SNAKE_SIZE)
        
        # load the explosion image and display it
        deathImg = pygame.image.load('assets/images/explosion.png')
        deathRect = deathImg.get_rect()
        deathRect.center = x + (constants.SNAKE_SIZE / 2), y + (constants.SNAKE_SIZE / 2)
        screen.blit(deathImg, deathRect)
        pygame.display.update()



class snakeSegment:
    x = float(0)
    y = float(0)

    def __init__(self, x, y):
        self.x = x
        self.y = y