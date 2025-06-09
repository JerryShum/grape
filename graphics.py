from tkinter import Tk, BOTH, Canvas
import time

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
        
        self.canvas = Canvas(self.__root, bg="white", width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=True)
        
        self.windowRunning = False

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
                

#! Simple class that stores a point on a cartesian grid (x,y) coordinates in pixels
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
#! Class that takes 2 points as input and draws a line between the two using canvas methods

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.pont2 = point2
        
        self.x1 = point1.x
        self.x2 = point2.x
        self.y1 = point1.y
        self.y2 = point2.y
    
    def draw(self, canvas, color):
        # draw lines -> x = distance from the left of the screen
        # y = distance from the top of the screen
        canvas.create_line(
            self.x1, self.y1, self.x2, self.y2, fill = color, width=2
        )
        