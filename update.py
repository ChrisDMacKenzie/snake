from snake import Snake

def update(screen, snake, food):
    snake.draw(screen)
    food.draw(screen)
    food.checkIfEaten(snake)
    snake.move()