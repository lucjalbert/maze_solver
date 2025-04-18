from window import Window
from components import Point, Line, Cell
from maze import Maze


def main():
    win = Window(2000, 1200)

    maze = Maze(50, 50, 12, 15, 50, 50, win, 19)

    win.wait_for_close()


if __name__ == "__main__":
    main()