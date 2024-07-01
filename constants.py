# we gotta establish a grid system so everything lines up
SCREEN_SIZE = WIDTH, HEIGHT = 1280, 720
GRID_SIZE = 20
X_VALS = list(range(0, int(WIDTH/GRID_SIZE), 1))
Y_VALS = list(range(0, int(HEIGHT/GRID_SIZE), 1))

# set the size of the game objects
SNAKE_SIZE = GRID_SIZE - 2
FOOD_SIZE = GRID_SIZE - 4

#some colors 
BLACK = 0, 0, 0
WHITE = 255, 255, 255
BLUE = 0, 0, 255