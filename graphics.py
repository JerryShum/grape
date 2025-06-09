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
        