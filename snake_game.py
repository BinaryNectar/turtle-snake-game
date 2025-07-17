"""
Main game controller for Turtle Snake Game.
Handles initialization, input binding, game loop, scoring, and game-over display.
"""

import turtle
import time
from utils import random_food_position
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
    TEXT_COLOR,
    FOOD_COLOR,
    FOOD_SHAPE,
    GAME_TITLE,
    GAME_OVER_MESSAGE,
    DIRECTION_UP,
    DIRECTION_DOWN,
    DIRECTION_LEFT,
    DIRECTION_RIGHT
)
from snake import Snake


class SnakeGame:
    """
    Controller for the Snake Game: sets up screen, snake, food, scoreboard,
    processes input, and runs the main game loop.
    """

    def __init__(self, width=DEFAULT_WINDOW_WIDTH, height=DEFAULT_WINDOW_HEIGHT, delay=DEFAULT_MOVEMENT_DELAY):
        """
        Initialize game window, snake, food, and scoreboard.

        Args:
            width (int): Window width in pixels.
            height (int): Window height in pixels.
            delay (int): Movement delay in milliseconds.
        """
        self.width = width
        self.height = height
        self.delay = delay / MS_TO_SECONDS  # convert to seconds
        self.score = 0

        # Allow RGB color values
        turtle.colormode(255)

        # Screen setup
        self.screen = turtle.Screen()
        self.screen.title(GAME_TITLE)
        self.screen.bgcolor(BACKGROUND_COLOR)
        self.screen.setup(width=self.width, height=self.height)
        self.screen.tracer(0)

        # Create snake instance
        self.snake = Snake()

        # Create and place food
        self.food = turtle.Turtle()
        self.food.shape(FOOD_SHAPE)
        self.food.color(FOOD_COLOR)
        self.food.penup()
        self._place_food()

        # Scoreboard setup
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.color(TEXT_COLOR)
        self.pen.goto(0, self.height // 2 - SCOREBOARD_Y_OFFSET)
        self._update_score()

        # Input bindings
        self.screen.listen()
        self.screen.onkey(lambda: self.snake.set_direction(DIRECTION_UP), 'Up')
        self.screen.onkey(lambda: self.snake.set_direction(DIRECTION_DOWN), 'Down')
        self.screen.onkey(lambda: self.snake.set_direction(DIRECTION_LEFT), 'Left')
        self.screen.onkey(lambda: self.snake.set_direction(DIRECTION_RIGHT), 'Right')

    def _place_food(self):
        """
        Position the food at a random grid-aligned location.
        """
        x, y = random_food_position(self.width, self.height)
        self.food.goto(x, y)

    def _update_score(self):
        """
        Refresh the score display at the top of the screen.
        """
        self.pen.clear()
        self.pen.write(
            f"Score: {self.score}",
            align='center',
            font=(FONT_FAMILY, SCOREBOARD_FONT_SIZE, FONT_STYLE)
        )

    def start(self):
        """
        Run the main game loop until a collision occurs.
        """
        while True:
            self.screen.update()

            # Check for border collision
            head_x, head_y = self.snake.head.xcor(), self.snake.head.ycor()
            if abs(head_x) > self.width/2 - BORDER_COLLISION_MARGIN or abs(head_y) > self.height/2 - BORDER_COLLISION_MARGIN:
                break

            # Check for food collision
            if self.snake.head.distance(self.food) < FOOD_COLLISION_DISTANCE:
                self.snake.grow()
                self.score += SCORE_INCREMENT
                self._update_score()
                self._place_food()

            # Move the snake
            self.snake.move()
            time.sleep(self.delay)

            # Check for self collision
            if self.snake.check_self_collision():
                break

        self._game_over()

    def _game_over(self):
        """
        Display the game-over message and close the game after a pause.
        """
        self.pen.goto(0, 0)
        self.pen.write(
            GAME_OVER_MESSAGE,
            align='center',
            font=(FONT_FAMILY, GAME_OVER_FONT_SIZE, FONT_STYLE)
        )
        self.screen.update()
        time.sleep(GAME_OVER_DISPLAY_TIME)
        self.screen.bye()