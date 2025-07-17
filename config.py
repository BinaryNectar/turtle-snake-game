"""
Configuration constants for the Snake Game.

This module contains all the configuration constants used throughout the game,
making it easier to modify game parameters and avoid magic numbers in the code.
"""

# Window settings
DEFAULT_WINDOW_WIDTH = 600  # pixels
DEFAULT_WINDOW_HEIGHT = 600  # pixels

# Game timing
DEFAULT_MOVEMENT_DELAY = 16  # milliseconds
MS_TO_SECONDS = 1000.0
GAME_OVER_DISPLAY_TIME = 2  # seconds

# Movement and positioning
GRID_SQUARE_SIZE = 20  # pixels
MOVEMENT_STEP = 3  # pixels per move
BORDER_COLLISION_MARGIN = 10  # pixels from edge

# Collision detection
FOOD_COLLISION_DISTANCE = 20  # pixels
SELF_COLLISION_DISTANCE = 10  # pixels

# Scoring
SCORE_INCREMENT = 10  # points per food eaten

# UI positioning
SCOREBOARD_Y_OFFSET = 40  # pixels from top

# Font settings
SCOREBOARD_FONT_SIZE = 24
GAME_OVER_FONT_SIZE = 36
FONT_FAMILY = 'Courier'
FONT_STYLE = 'normal'

# Colors
BACKGROUND_COLOR = 'black'
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = 'red'
TEXT_COLOR = 'white'

# Shapes
SNAKE_SHAPE = 'square'
FOOD_SHAPE = 'circle'

# Direction constants
DIRECTION_UP = 'up'
DIRECTION_DOWN = 'down'
DIRECTION_LEFT = 'left'
DIRECTION_RIGHT = 'right'
DIRECTION_STOP = 'stop'

# Game title
GAME_TITLE = 'Turtle Snake Game'

# Game over message
GAME_OVER_MESSAGE = 'GAME OVER'
