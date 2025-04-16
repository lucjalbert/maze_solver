from window import Window
from components import Point, Line, Cell
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 12, 8, 50, 50, win)

    win.wait_for_close()



if __name__ == "__main__":
    main()