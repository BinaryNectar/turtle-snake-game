from entity import Entity
from model.scoreboard import ScoreboardLogic
from view.scoreboard import ScoreboardView
from config import (
    DEFAULT_WINDOW_HEIGHT,
    DEFAULT_WINDOW_WIDTH
)

class Scoreboard(Entity):
    def __init__(self, screen_height=DEFAULT_WINDOW_HEIGHT, screen_width=DEFAULT_WINDOW_WIDTH):

        self.logic = ScoreboardLogic(screen_height, screen_width)
        self.view = ScoreboardView(self.logic)

    def sync(self) -> None:
        self.view.sync()

    def game_over(self) -> None:
        self.view.game_over();
               