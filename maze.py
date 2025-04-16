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
            win,
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
    

    def _create_cells(self):
        self._cells = []

        # Generate a list of lists containing cells
        for x in range(self._num_rows):
            temp = []
            for y in range(self._num_cols):
                cell = Cell(self._win)
                temp.append(cell)
            
            self._cells.append(temp)
        
        # Draw all cells
        for x in range(self._num_rows):
            for y in range(self._num_cols):
                self._draw_cell(x, y)
        
    
    def _draw_cell(self, x, y):
        cell_x1 = self._x1 + (self._cell_size_x * x)
        cell_y1 = self._y1 + (self._cell_size_y * y)
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y

        self._cells[x][y].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)


