from turtle import Turtle
from model.scoreboard import ScoreboardLogic
from config import (
    SCOREBOARD_FONT_SIZE,
    GAME_OVER_FONT_SIZE,
    GAME_OVER_DISPLAY_TIME,
    GAME_OVER_MESSAGE,
    FONT_FAMILY,
    FONT_STYLE,
    TEXT_COLOR
)

class ScoreboardView(Turtle):
    def __init__(self, logic:ScoreboardLogic):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(TEXT_COLOR)
        self.logic = logic
        self.sync

    def sync(self):
        self.goto(self.logic.x, self.logic.y)
        
        self.clear()
        self.write(
            f"Score: {self.logic.score}",
            align='center',
            font=(FONT_FAMILY, SCOREBOARD_FONT_SIZE, FONT_STYLE)
        )

    def game_over(self):
        self.goto(0, 0)
        self.write(
            GAME_OVER_MESSAGE,
            align='center',
            font=(FONT_FAMILY, GAME_OVER_FONT_SIZE, FONT_STYLE)
        )