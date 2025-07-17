import random
from config import GRID_SQUARE_SIZE

def random_food_position(width, height):
    """
    Returns a random position within the screen boundaries aligned to the grid.
    
    Args:
        width: Screen width in pixels
        height: Screen height in pixels
        
    Returns:
        tuple: (x, y) coordinates for the food position
    """
    max_x = (width // 2 - GRID_SQUARE_SIZE)
    max_y = (height // 2 - GRID_SQUARE_SIZE)
    x = random.randint(-max_x//GRID_SQUARE_SIZE, max_x//GRID_SQUARE_SIZE) * GRID_SQUARE_SIZE
    y = random.randint(-max_y//GRID_SQUARE_SIZE, max_y//GRID_SQUARE_SIZE) * GRID_SQUARE_SIZE
    return x, y
