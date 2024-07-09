import pygame
import constants
import surface
from snake import Snake
from food import Food


class Game:
    def __init__(self, screen, scoreFont):
        self.screen = screen
        self.gameSurface = surface.drawGameSurface()
        self.scoreFont = scoreFont
        self.moveEvent = pygame.USEREVENT+1
        self.snake = Snake()
        self.food = Food()
        # make sure the first food spawn isn't on top of the snake
        while self.snake.needsFood:
            self.food.placeFood()
            self.checkForOverlap()
        # initialize the score to zero
        self.score = 0
        self.drawScore()
    
    def run(self):
        pygame.time.set_timer(self.moveEvent, self.snake.speed)

        while self.snake.alive:
            if pygame.event.get(pygame.QUIT): break
            
            keys = pygame.key.get_pressed()
            
            # basic snake moving controls
            for e in pygame.event.get():
                if e.type == self.moveEvent:
                    if (keys[pygame.K_w] or keys[pygame.K_UP]) and (self.snake.direction not in ['N', 'S']):
                        # logger.debug("changing direction to north")
                        self.snake.direction = 'N'
                    elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and (self.snake.direction not in ['N', 'S']):
                        # logger.debug("changing direction to south")
                        self.snake.direction = 'S'
                    elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and (self.snake.direction not in ['E', 'W']):
                        # logger.debug("changing direction to west")
                        self.snake.direction = 'W'
                    elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and (self.snake.direction not in ['E', 'W']):
                        # logger.debug("changing direction to east")
                        self.snake.direction = 'E'
                    self.update()
            
            self.screen.blit(self.gameSurface, (0, 0))

    def update(self):
        self.food.draw(self.screen)
        self.snake.draw(self.screen)
        self.snake.checkForDeath()
        self.checkForEat()
        pygame.display.update()
        self.snake.move()

    # checks to see if the snake just ate
    def checkForEat(self):
        if self.food.x == self.snake.body[0].x \
            and self.food.y == self.snake.body[0].y:
                self.score += 1
                self.drawScore()
                self.snake.needsFood = True
                self.snake.needsToExtend = True
                self.snake.speedUp(self.moveEvent)
                while self.snake.needsFood:
                    self.food.placeFood()
                    self.checkForOverlap()

    # when placing new food, make sure it doesn't overlap with the snakes current location
    def checkForOverlap(self):
        for segment in self.snake.body:
            if self.food.x == segment.x \
            and self.food.y == segment.y:
                break
            self.snake.needsFood = False

    def drawScore(self):
        scoreStr = str(self.score).zfill(4)
        scoreObj = self.scoreFont.render(scoreStr, True, (constants.WHITE))
        scoreObjRect = scoreObj.get_rect()
        scoreObjRect.bottomright = constants.WIDTH - constants.OUTSIDE_BORDER_WIDTH, \
            scoreObjRect.height + (constants.TITLE_REGION_HEIGHT - scoreObjRect.height) / 2
        # erase the old score
        self.gameSurface.fill(
            constants.BLACK,
            (
                constants.WIDTH - constants.SCORE_WIDTH,
                0,
                constants.SCORE_WIDTH,
                constants.TITLE_REGION_HEIGHT)
        )
        # write the new score
        self.gameSurface.blit(scoreObj, scoreObjRect)
