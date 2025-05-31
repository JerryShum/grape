from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        
        self.__create_cells()
    
    def __create_cells(self):
        for col in range(self.num_cols):
            col_cells = []
            for row in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self.__cells.append(col_cells)
        
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self.__draw_cell(col, row)
        
    
    def __draw_cell(self, col, row):
        x1 = self.x1 + col * self.cell_size_x
        x2 = x1 + self.cell_size_x
        y1 = self.y1 + row * self.cell_size_y
        y2 = y1 + self.cell_size_y

        self.__cells[col][row].draw(x1, x2, y1, y2)
        
    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
    
           