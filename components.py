class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

class Line():
    def __init__(self, start, end):
        self.start = start
        self.end = end
    

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )

    def __repr__(self):
        return f"p1 = ({self.start.x}, {self.start.y}) p2 = ({self.end.x}, {self.end.y})"


class Cell():
    def __init__(self, win):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
        self._win = win


    def draw(self,  x1, y1, x2, y2, fill_color="black"):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            l = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(l, fill_color)

        if self.has_top_wall:
            l = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(l, fill_color)

        if self.has_right_wall:
            l = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(l, fill_color)

        if self.has_bottom_wall:
            l = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(l, fill_color)

    
    def draw_move(self, to_cell, undo=False):
        if not undo:
            fill_color = "red"
        else:
            fill_color = "gray"

        # Calculate cell center in order to generate points for draw line
        self_center_x = self._x1 + (self._x2 - self._x1) / 2
        self_center_y = self._y1 + (self._y2 - self._y1) / 2
        other_center_x = to_cell._x1 + (to_cell._x2 - to_cell._x1) / 2
        other_center_y = to_cell._y1 + (to_cell._y2 - to_cell._y1) / 2
        l = Line(Point(self_center_x, self_center_y), Point(other_center_x, other_center_y))

        self._win.draw_line(l, fill_color)