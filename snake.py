import pygame
import initialize

segmentSize = float(19)
moveDistance = segmentSize + 1

class Snake:

    moveDistance = segmentSize + 1
    hasEaten = False
    
    def __init__(self) -> None:
        self.speed = 200
        self.direction = 'N'
        self.body = [snakeSegment(initialize.width/2, initialize.height/2)]

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(
                screen,
                "white",
                pygame.Rect(
                    segment.x-(segmentSize/2),
                    segment.y-(segmentSize/2),
                    segmentSize,
                    segmentSize))
        pygame.display.flip()

    def move(self):
        # determine the coordinates for where the head needs to go
        newHead = snakeSegment(self.body[0].x, self.body[0].y)
        match self.direction:
            case 'N':
                newHead.y -= moveDistance
            case 'S':
                newHead.y += moveDistance
            case 'E':
                newHead.x += moveDistance
            case 'W':
                newHead.x -= moveDistance
        
        # attach the new head to the snake
        self.body.insert(0, newHead)

        # if we didn't just eat a pellet, delete the back segment
        if not self.hasEaten:
            self.body = self.body[:-1]

        self.hasEaten = False


class snakeSegment:
    x = float(0)
    y = float(0)

    def __init__(self, x, y):
        self.x = x
        self.y = y