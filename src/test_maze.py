import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):

        # Arrange
        num_cols = 12
        num_rows = 10

        # Act
        m = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Assert
        self.assertEqual(
            len(m._cells),
            num_cols,
        )
        self.assertEqual(
            len(m._cells[0]),
            num_rows,
        )

    
    def test_maze_create_cells_large(self):

        # Arrange
        num_cols = 175
        num_rows = 80

        # Act
        m = Maze(100, 50, num_rows, num_cols, 25, 25)

        # Assert
        self.assertEqual(
            len(m._cells),
            num_cols,
        )
        self.assertEqual(
            len(m._cells[0]),
            num_rows,
        )

    
    def test_maze_break_entrance_and_exit(self):

        # Arrange
        num_cols = 12
        num_rows = 10

        # Act
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Assert
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )



if __name__ == "__main":
    unittest.main()