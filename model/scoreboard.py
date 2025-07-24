from config import (
    DEFAULT_WINDOW_WIDTH,
    DEFAULT_WINDOW_HEIGHT,
    DEFAULT_MOVEMENT_DELAY,
    MS_TO_SECONDS,
    BORDER_COLLISION_MARGIN,
    FOOD_COLLISION_DISTANCE,
    SCORE_INCREMENT,
    SCOREBOARD_Y_OFFSET,
    SCOREBOARD_FONT_SIZE,
    GAME_OVER_FONT_SIZE,
    GAME_OVER_DISPLAY_TIME,
    FONT_FAMILY,
    FONT_STYLE,
    BACKGROUND_COLOR,
    TEXT_COLOR
)

class ScoreboardLogic:
    def __init__(self, height=DEFAULT_WINDOW_HEIGHT, width=DEFAULT_WINDOW_WIDTH):
        self.score = 0
        self.height = height
        self.width = width
        self.x = 0
        self.y = self.height // 2 - SCOREBOARD_Y_OFFSET
        
    def update_score(self):
        self.score += SCORE_INCREMENT
