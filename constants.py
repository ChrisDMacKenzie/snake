# we gotta establish a grid system so everything lines up
SCREEN_SIZE = WIDTH, HEIGHT = 1280, 720
GRID_SIZE = 20

# set the size of the game objects
SNAKE_SIZE = GRID_SIZE - 2
FOOD_SIZE = GRID_SIZE - 4

# set the border of the actual game area
TITLE_REGION_HEIGHT = 70
OUTSIDE_BORDER_WIDTH = 10
GAME_BORDER_WIDTH = 10

# calculate the bounds of the game area
TOP_CHEAT = int((TITLE_REGION_HEIGHT + GAME_BORDER_WIDTH) / GRID_SIZE)
SIDE_CHEAT = BOTTOM_CHEAT = int((OUTSIDE_BORDER_WIDTH + GAME_BORDER_WIDTH) / GRID_SIZE)

# valid x and y coords for the snake and food inside the game area
X_VALS = list(range(SIDE_CHEAT, int((WIDTH/GRID_SIZE)-SIDE_CHEAT), 1))
Y_VALS = list(range(TOP_CHEAT, int((HEIGHT/GRID_SIZE)-BOTTOM_CHEAT), 1))

# some colors 
BLACK = 0, 0, 0
WHITE = 255, 255, 255
BLUE = 0, 0, 255

# score width
SCORE_WIDTH = 140
