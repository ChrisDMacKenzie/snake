import pygame
import constants
from snake import Snake
from food import Food


class Game:
    def __init__(self, screen):
        self.snake = Snake()
        self.food = Food(self.snake)
        self.MOVEEVENT = pygame.USEREVENT+1
        self.screen = screen
    
    def run(self):
        pygame.time.set_timer(self.MOVEEVENT, self.snake.speed)

        while self.snake.alive:
            if pygame.event.get(pygame.QUIT): break
            
            keys = pygame.key.get_pressed()
            for e in pygame.event.get():
                if e.type == self.MOVEEVENT:
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
        self.snake.checkForDeath()
        self.food.checkIfEaten(self.snake)
        # if the snake just ate and the speed isn't already too fast,
        # speed up the snake
        if self.snake.hasEaten and self.snake.speed >= 10:
            self.snake.speed -= 2
            pygame.time.set_timer(self.MOVEEVENT, self.snake.speed)
        self.snake.move()

