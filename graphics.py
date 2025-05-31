from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.rootwidget = Tk()
        self.rootwidget.title("rootwidget")
        self.rootwidget.protocol("WM_DELETE_WINDOW", self.close)

        self.canvaswidget = Canvas(self.rootwidget, width=self.width, height=self.height)
        self.canvaswidget.pack(fill=BOTH, expand=True)

        self.windowRunning = False
    
    def redraw(self):
        self.rootwidget.update_idletasks()
        self.rootwidget.update()
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvaswidget, fill_color)
    
    def wait_for_close(self):
        self.windowRunning = True
        while self.windowRunning:
            self.redraw()
    
    def close(self):
        self.windowRunning = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x, 
            self.point2.y,
            fill=fill_color,
            width=2
        )
