"""
Module defining the Snake class for the Turtle Snake Game.
Encapsulates the snake's state and behavior: head creation, movement,
growth, and self-collision detection.
"""

from turtle import Turtle
from config import (
    SELF_COLLISION_DISTANCE,
    SNAKE_SHAPE,
    SNAKE_COLOR,
    DEFAULT_WINDOW_HEIGHT,
    DEFAULT_WINDOW_WIDTH,
    DIRECTION_UP,
    DIRECTION_DOWN,
    DIRECTION_LEFT,
    DIRECTION_RIGHT,
    DIRECTION_STOP,
    GRID_SQUARE_SIZE,
    MOVEMENT_STEP
)


class Snake:
    """
    Represents the snake in the game, including the head and body segments.
    Handles movement, growth, and self-collision logic.
    """

    def __init__(self):
        """
        Initialize a new snake with a head at the origin, no body segments,
        and a stopped direction.
        """
        # Create the head turtle
        self.head = Turtle()
        self.head.shape(SNAKE_SHAPE)
        self.head.color(SNAKE_COLOR)
        self.head.penup()
        self.head.goto(0, 0)

        # Body segments stored in a list (following the head)
        self.segments = []

        # Current movement direction (one of DIRECTION_* constants)
        self.direction = DIRECTION_STOP

        # Gradient for segments
        self.gradient = list(SNAKE_COLOR)
        self.gradient_incrementor = -5

    def set_direction(self, new_direction):
        """
        Change the snake's direction, preventing a direct reversal.

        Args:
            new_direction (str): One of the direction constants.
        """
        # Prevent reversing direction instantly
        opposites = {
            DIRECTION_UP: DIRECTION_DOWN,
            DIRECTION_DOWN: DIRECTION_UP,
            DIRECTION_LEFT: DIRECTION_RIGHT,
            DIRECTION_RIGHT: DIRECTION_LEFT
        }
        if new_direction != opposites.get(self.direction):
            self.direction = new_direction

    def move(self):
        """
        Move the snake forward by one step:
        - Shift segments to follow the head's previous positions.
        - Move the head by MOVEMENT_STEP pixels in the current direction.
        """
        # Move body segments
        for i in range(len(self.segments) - 1, 0, -1):
            prev_x = self.segments[i-1].xcor()
            prev_y = self.segments[i-1].ycor()
            self.segments[i].goto(prev_x, prev_y)

        # First segment follows the head
        if self.segments:
            self.segments[0].goto(self.head.xcor(), self.head.ycor())

        # Move the head
        x, y = self.head.xcor(), self.head.ycor()
        if self.direction == DIRECTION_UP:
            self.head.sety(y + MOVEMENT_STEP)
        elif self.direction == DIRECTION_DOWN:
            self.head.sety(y - MOVEMENT_STEP)
        elif self.direction == DIRECTION_LEFT:
            self.head.setx(x - MOVEMENT_STEP)
        elif self.direction == DIRECTION_RIGHT:
            self.head.setx(x + MOVEMENT_STEP)

    def grow(self):
        """
        Grow the snake by adding a new segment at the tail's current position.
        Ensures no immediate self-collision upon growing.
        """

        # Create and position the new segment
        new_segment = Turtle()
        new_segment.shape(SNAKE_SHAPE)
        self.gradient[1] = self.gradient[1] + self.gradient_incrementor
        if self.gradient[1] == 0 or self.gradient[1] == 255:
            self.gradient_incrementor *= -1
        new_segment.color(tuple(self.gradient))
        new_segment.penup()

        self.segments.append(new_segment)

    def check_self_collision(self):
        """
        Check if the head collides with any body segment.

        Returns:
            bool: True if collision detected, False otherwise.
        """
        for segment in self.segments:
            if segment.distance(self.head) < MOVEMENT_STEP:
                return True
        return False

    def reset(self, height=DEFAULT_WINDOW_HEIGHT, width=DEFAULT_WINDOW_WIDTH):
        """
        Reset the snake to its initial state: hide segments, clear list,
        center head, and stop movement.
        """
        self.head.goto(0, 0)
        increment = 0
        for segment in self.segments:
            segment.goto(width + increment, height)
            increment += GRID_SQUARE_SIZE

        self.segments.clear()
        self.direction = DIRECTION_STOP
        self.gradient = list(SNAKE_COLOR)
        self.gradient_incrementor = -5