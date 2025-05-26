#!/usr/bin/env python3

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

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
    
    def draw(self, x1, x2, y1, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        
        if self.has_left_wall:
            point1 = Point(x1, y1)
            point2 = Point(x1, y2)
            
            line = Line(point1, point2)
            self.__win.draw_line(line, "green")
           

        if self.has_right_wall:
            point1 = Point(x2, y1)
            point2 = Point(x2, y2)

            line = Line(point1, point2)
            self.__win.draw_line(line, "blue")


        if self.has_top_wall:
            point1 = Point(x1, y1)
            point2 = Point(x2, y1)

            line = Line(point1, point2)
            self.__win.draw_line(line, "black")


        if self.has_bottom_wall:
            point1 = Point(x1, y2)
            point2 = Point(x2, y2)

            line = Line(point1, point2)
            self.__win.draw_line(line, "green")

        

def main():
    window = Window(800, 600)
    # Create cells
    cell1 = Cell(window)
    cell2 = Cell(window)
    cell3 = Cell(window)

    # Draw the cells on the window's canvas
    cell1.draw(100, 200, 150, 300)
    cell2.draw(300, 400, 350, 500)
    cell3.draw(100, 300, 350, 500)


    window.wait_for_close()

main()
