from window import Window
from components import Point, Line, Cell


def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.draw(100, 50, 150, 100)

    c3 = Cell(win)
    c3.draw(100, 100, 150, 150)

    c1.draw_move(c2)
    c2.draw_move(c3, undo=True)

    win.wait_for_close()



if __name__ == "__main__":
    main()