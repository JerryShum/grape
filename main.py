from graphics import Window, Line, Point
from maze import Maze
from cell import Cell

def main():
    win = Window("Sigma", 1000, 1000)
    
    maze = Maze(10,10,10,10,30,30,win, 4)
    maze.solve()
   
    win.wait_for_close()
    

main()