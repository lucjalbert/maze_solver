import random
import time
from components import Cell


class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None,
        ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
    

    def _create_cells(self):
        # Generate a list of lists containing cells
        for x in range(self._num_cols):
            temp = []
            for y in range(self._num_rows):
                cell = Cell(self._win)
                temp.append(cell)
            
            self._cells.append(temp)
        
        # Draw all cells
        for x in range(self._num_cols):
            for y in range(self._num_rows):
                self._draw_cell(x, y)
        
    
    def _draw_cell(self, x, y):
        cell_x1 = self._x1 + (self._cell_size_x * x)
        cell_y1 = self._y1 + (self._cell_size_y * y)
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y

        self._cells[x][y].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    
    def _animate(self):
        if self._win:
            self._win.redraw()
            time.sleep(0.002)


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols -1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)


    def _break_walls_r(self, x, y):
        self._cells[x][y]._visited = True

        while True:
            cells_to_visit = []
            
            # If adjacent cell exists and has not been visited, add it to the list
            if x > 0 and not self._cells[x - 1][y]._visited:
                    cells_to_visit.append((x - 1, y, "left"))

            if x < self._num_cols - 1 and not self._cells[x + 1][y]._visited:
                    cells_to_visit.append((x + 1, y, "right"))

            if y > 0 and not self._cells[x][y - 1]._visited:
                    cells_to_visit.append((x, y - 1, "up"))

            if y < self._num_rows - 1 and not self._cells[x][y + 1]._visited:
                    cells_to_visit.append((x, y + 1, "down"))

            if len(cells_to_visit) == 0:
                self._draw_cell(x, y)
                return

            direction = random.randrange(len(cells_to_visit))

            match (cells_to_visit[direction][2]):
                case "left":
                    self._cells[x][y].has_left_wall = False
                    self._cells[x - 1][y].has_right_wall = False
                case "up":
                    self._cells[x][y].has_top_wall = False
                    self._cells[x][y - 1].has_bottom_wall = False
                case "right":
                    self._cells[x][y].has_right_wall = False
                    self._cells[x + 1][y].has_left_wall = False
                case "down":
                    self._cells[x][y].has_bottom_wall = False
                    self._cells[x][y + 1].has_top_wall = False

            self._break_walls_r(cells_to_visit[direction][0], cells_to_visit[direction][1])