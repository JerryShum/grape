import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
        
    def test_maze_create_cells2(self):
        
        num_cols = 20
        test_num_rows = 22
        m1 = Maze(0, 0, 20, 20, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_cols,
        )
        self.assertNotEqual(
            len(m1._Maze__cells),
            test_num_rows,
        )
    def test_maze_create_cells3(self):
        
        num_cols = 30
        num_rows = 30
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells),
            num_rows,
        )
    
    def test_maze_reset_visited(self):
        num_cols = 30
        num_rows = 30
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        for row in range(num_rows):
            for col in range(num_cols):
                self.assertEqual(m1._Maze__cells[row][col].visited, False)
        
    
    
#! Only trigger if this file is ran directly (python3 tests.py)
if __name__ == "__main__":
    # unittest.main triggers all the tests that we created above
    unittest.main()