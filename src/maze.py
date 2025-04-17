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
        ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
        self._break_entrance_and_exit()
    

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
            time.sleep(0.03)


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols -1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
