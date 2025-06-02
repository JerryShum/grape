from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        
        if seed is not None:
            random.seed(seed)
        
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        
        self.__reset_cells_visited()
    
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
        
        
    def __break_entrance_and_exit(self):
        entranceCell = self.__cells[0][0]
        exitCell = self.__cells[self.num_cols - 1][self.num_rows - 1]
        
        entranceCell.has_top_wall = False
        exitCell.has_bottom_wall = False
        
        self.__draw_cell(0, 0)
        self.__draw_cell(self.num_cols - 1, self.num_rows - 1)
        
    def __break_walls_r(self, col, row):
        current_cell = self.__cells[col][row]
        current_cell.visited = True
        
        while True:
            potentialCells = []
            
            # Check the cell to the right (next column over)
            if col + 1 <= self.num_cols  - 1:
                if self.__cells[col + 1][row].visited == False:
                    potentialCells.append(("right", col + 1, row))
            
            # Check the cell to the bottom (same column but 1 row lower)
            if row + 1 <= self.num_rows - 1:
                if self.__cells[col][row + 1].visited == False:
                    potentialCells.append(("bottom", col, row + 1))
                    
            # Check the cell to the left (one column behind)
            if col -1 <= self.num_cols - 1 and col - 1 >= 0:
                if self.__cells[col - 1][row].visited == False:
                    potentialCells.append(("left", col - 1, row))
                    
            # Check the cell above (same column but 1 row above)
            if row - 1 <= self.num_rows - 1 and row - 1 >= 0:
                if self.__cells[col][row - 1].visited == False:
                    potentialCells.append(("top", col, row - 1))
            
            if len(potentialCells) == 0:
                self.__draw_cell(col, row)
                return
                
            else:
                # pick a random cell to travel to:
                index = random.randint(0, len(potentialCells) - 1)
                next_cell_info = potentialCells[index] # ("right", col + 1, row)
                
            match next_cell_info[0]:
                case "right":
                    current_cell.has_right_wall = False
                    
                    nextCol = next_cell_info[1]
                    nextRow = next_cell_info[2]
                    
                    next_cell = self.__cells[nextCol][nextRow] 
                    next_cell.has_left_wall = False
                    
                    self.__draw_cell(col, row)
                    self.__draw_cell(nextCol, nextRow)
                    
                    self.__break_walls_r(nextCol, nextRow)
                    
                case "bottom":
                    current_cell.has_bottom_wall = False
                    
                    nextCol = next_cell_info[1]
                    nextRow = next_cell_info[2]
                    
                    next_cell = self.__cells[nextCol][nextRow] 
                    next_cell.has_top_wall = False
                    
                    self.__draw_cell(col, row)
                    self.__draw_cell(nextCol, nextRow)
                    
                    
                    self.__break_walls_r(nextCol, nextRow)
                    
                case "left":
                    current_cell.has_left_wall = False
                    
                    nextCol = next_cell_info[1]
                    nextRow = next_cell_info[2]
                    
                    next_cell = self.__cells[nextCol][nextRow] 
                    next_cell.has_right_wall = False
                    
                    self.__draw_cell(col, row)
                    self.__draw_cell(nextCol, nextRow)
                    
                    self.__break_walls_r(nextCol, nextRow)
                    
                case "top":
                    current_cell.has_top_wall = False
                    
                    nextCol = next_cell_info[1]
                    nextRow = next_cell_info[2]
                    
                    next_cell = self.__cells[nextCol][nextRow] 
                    next_cell.has_bottom_wall = False
                    
                    self.__draw_cell(col, row)
                    self.__draw_cell(nextCol, nextRow)
                    
                    self.__break_walls_r(nextCol, nextRow)

    
    def __reset_cells_visited(self):
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self.__cells[col][row].visited = False
    
    def solve(self):
        self._solve_r(0,0)

    def _solve_r(self, col, row):
        self.animate()
        
        current_cell = self.__cells[col][row]
        current_cell.visited = True
        
        if current_cell == self.__cells[self.num_cols - 1][self.num_rows - 1]:
            return True
        
            
        # Check the cell to the right (next column over)
        if col + 1 <= self.num_cols  - 1:
            if self.__cells[col + 1][row].visited == False:
                if not current_cell.has_right_wall and not self.__cells[col + 1][row].has_left_wall:
                    next_cell = self.__cells[col + 1][row]
                    current_cell.draw_move(next_cell)
                    
                    if self._solve_r(col+1, row):
                        return True
                    else:
                        current_cell.draw_move(next_cell, undo = True)

        # Check the cell above (same column but 1 row above)
        if row - 1 >= 0:
            if self.__cells[col][row - 1].visited == False:
                if not current_cell.has_top_wall and not self.__cells[col][row - 1].has_bottom_wall:
                    next_cell = self.__cells[col][row - 1]
                    current_cell.draw_move(next_cell)
                    
                    if self._solve_r(col, row-1):
                        return True
                    else:
                        current_cell.draw_move(next_cell, undo = True)

        # Check the cell below (same column but 1 row below)
        if row + 1 <= self.num_rows - 1:
            if self.__cells[col][row + 1].visited == False:
                if not current_cell.has_bottom_wall and not self.__cells[col][row + 1].has_top_wall:
                    next_cell = self.__cells[col][row + 1]
                    current_cell.draw_move(next_cell)
                    
                    if self._solve_r(col, row+1):
                        return True
                    else:
                        current_cell.draw_move(next_cell, undo = True)

        # Check the cell to the left (one column behind)
        if col - 1 >= 0:
            if self.__cells[col - 1][row].visited == False:
                if not current_cell.has_left_wall and not self.__cells[col - 1][row].has_right_wall:
                    next_cell = self.__cells[col - 1][row]
                    current_cell.draw_move(next_cell)
                    
                    if self._solve_r(col-1, row):
                        return True
                    else:
                        current_cell.draw_move(next_cell, undo = True)

        return False
                        
        
                
    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
    
           