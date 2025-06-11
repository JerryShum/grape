from tkinter import *
import time
from maze import Maze

#! This window class encapsulates the GUI and Canvas that we are going to be using
#@ We define properties of the window (title,width,height)
## Using TKinter we are creating a root(which is basically the window itself)
## Canvas is what we use to draw stuff onto the screen using methods
## Redraw updates the GUI and wait_for_close is a loop that keeps calling redraw aslong as we want
class Window:
    def __init__(self, title, height, width):
        self.title = title
        self.height = height
        self.width = width
        self.__root = Tk()
        self.__root.title(self.title)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
        self.maze = None
        
        #! Canvas for drawing
        self.canvas = Canvas(self.__root, bg="white", width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=True)
        
        #! Button for generating maze
        self.createButton = Button(self.__root, text="Create Maze")
        self.createButton.config(command=self.create_maze)
        self.createButton.pack()
        self.createButtonPress = False
        
        #! Button for clearing the canvas
        self.clearButton = Button(self.__root, text="Clear Canvas")
        self.clearButton.config(command=self.clear_canvas)
        self.clearButton.pack()
        
        #! Button for solving the maze
        self.solveButton = Button(self.__root, text="Solve Maze")
        self.solveButton.config(command=self.solve_maze)
        self.solveButton.pack()
        
        
        self.windowRunning = False

    #! Function for button callback
    def create_maze(self):
        if self.createButtonPress == False:
            self.createButtonPress = True
            self.maze = Maze(10,10,10,10,30,30,self, 4)
        else:
            return
    
    def solve_maze(self):
        if self.maze != None:
            self.maze.solve()
    
    def clear_canvas(self):
        self.canvas.delete("all")
        self.createButtonPress = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    def wait_for_close(self):
        self.windowRunning = True
        
        while self.windowRunning:
            self.redraw()
            time.sleep(1/60)
    
    def close(self):
        self.windowRunning = False
                

