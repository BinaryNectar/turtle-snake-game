import argparse
from snake_game import SnakeGame
from config import DEFAULT_MOVEMENT_DELAY, DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT


def parse_args():
    parser = argparse.ArgumentParser(description='Play the Turtle Snake Game')
    parser.add_argument('--speed', type=int, default=DEFAULT_MOVEMENT_DELAY, help='Movement delay in ms')
    parser.add_argument('--width', type=int, default=DEFAULT_WINDOW_WIDTH, help='Window width')
    parser.add_argument('--height', type=int, default=DEFAULT_WINDOW_HEIGHT, help='Window height')
    return parser.parse_args()


def main():
    args = parse_args()
    game = SnakeGame(width=args.width, height=args.height, delay=args.speed)
    game.start()


if __name__ == '__main__':
    main()
