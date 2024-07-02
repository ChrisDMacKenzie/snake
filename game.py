import pygame
import constants
from snake import Snake
from food import Food


class Game:
    def __init__(self, screen):
        self.snake = Snake()
        self.food = Food()
        self.moveEvent = pygame.USEREVENT+1
        self.screen = screen
    
    def run(self):
        pygame.time.set_timer(self.moveEvent, self.snake.speed)

        while self.snake.alive:
            if pygame.event.get(pygame.QUIT): break
            
            keys = pygame.key.get_pressed()
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
            
            self.screen.fill(constants.BLACK)

    def update(self):
        self.food.draw(self.screen)
        self.snake.draw(self.screen)
        pygame.display.flip()
        self.snake.checkForDeath()
        self.checkForEat()
        self.snake.move()

    # checks to see if the snake just ate
    def checkForEat(self):
        if self.food.x == self.snake.body[0].x \
            and self.food.y == self.snake.body[0].y:
                self.snake.ateCurrentFood = True
                while self.snake.ateCurrentFood:
                    self.snake.speedUp(self.moveEvent)
                    self.food.placeFood()
                    self.checkForOverlap()

    # when placing new food, make sure it doesn't overlap with the snakes current location
    def checkForOverlap(self):
        for segment in self.snake.body:
            if self.food.x == segment.x \
            and self.food.y == segment.y:
                break
            self.snake.ateCurrentFood = False
            self.snake.needsToExtend = True