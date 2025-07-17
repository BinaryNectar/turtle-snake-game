# Turtle Snake Game

A classic Snake game implemented in Python using the `turtle` module.
The game features configurable window size and speed, grid‐aligned food, score tracking, and self‐collision/border detection.

---

## Table of Contents

* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Game Controls](#game-controls)
* [Configuration](#configuration)
* [Project Structure](#project-structure)
* [Development](#development)
* [License](#license)

---

## Features

* Smooth, grid‐based movement
* Configurable frame‐rate (speed) and window size
* Randomly placed food aligned to grid
* Scoreboard with point tracking
* Border and self‐collision detection (Game Over)
* Modular design (separate `Snake` class, game controller, utils, and config)

---

## Requirements

* Python 3.7+
* Standard library only (`turtle`, `argparse`, `random`, `time`)

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/binarynectar/turtle-snake-game.git
   cd turtle-snake-game
   ```
2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

---

## Usage

Run the game via the provided `main.py` script. You can customize the window size and movement speed:

```bash
python main.py [--width WIDTH] [--height HEIGHT] [--speed MS_DELAY]
```

* `--width` : Window width in pixels (default 600)
* `--height`: Window height in pixels (default 600)
* `--speed` : Movement delay in milliseconds (default 16 for \~60 FPS)

Example, to run at 800×800 pixels and a bit slower (\~30 FPS):

```bash
python main.py --width 800 --height 800 --speed 33
```

---

## Game Controls

* **Arrow keys**: Change snake direction (`Up`, `Down`, `Left`, `Right`)
* **Close window**: Ends game immediately (also triggers Game Over on collision)

---

## Configuration

All game constants live in `config.py`:

| Constant                          | Description                                  |
| --------------------------------- | -------------------------------------------- |
| `DEFAULT_WINDOW_WIDTH/HEIGHT`     | Initial window size (px)                     |
| `DEFAULT_MOVEMENT_DELAY`          | Delay per move in ms (e.g. 16→60 FPS)        |
| `MOVEMENT_STEP`                   | Pixels moved per step                        |
| `GRID_SQUARE_SIZE`                | Grid cell size (px) for food placement       |
| `FOOD_COLLISION_DISTANCE`         | Distance threshold to eat food (px)          |
| `SELF_COLLISION_DISTANCE`         | Distance threshold for self‐collision (px)   |
| `BACKGROUND_COLOR`, etc.          | Colors and fonts for UI                      |
| `GAME_TITLE`, `GAME_OVER_MESSAGE` | Text strings for window title and end screen |

Feel free to tweak these to change look & feel.

---

## Project Structure

```
.
├── main.py           # CLI parsing and game launch
├── config.py         # All configurable constants
├── utils.py          # Helper functions (e.g. random_food_position)
├── snake.py          # `Snake` class: head, segments, movement, growth, collision
└── snake_game.py     # `SnakeGame` class: setup, loop, scoring, input, game over
```

---

## Development

1. Edit configuration in `config.py` for custom behavior.
2. Extend or modify `Snake` class (in `snake.py`) for new features (e.g. power‐ups).
3. Add new game modes or UIs in `snake_game.py`.

Run `python main.py` after changes to test.

---

## License

This project is released under the MIT License.
Feel free to fork and customize!
