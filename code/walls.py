import pyglet

class Walll:
    def __init__(self, x1,y1,x2,y2,b):
        self.line = pyglet.shapes.Line(x=x1,y=y1,x2=x2, y2=y2, batch=b)

def getWalls(window_width, window_height, batch):
    line_list = []
    #outside lines
    line = Walll(472/1920 * window_width, 23/1080 * window_height, 1723/1920 * window_width, 217/1080 * window_height, batch)
    line1 = Walll(1723/1920 * window_width, 217/1080 * window_height, 1777/1920 * window_width, 295/1080 * window_height, batch)
    line2 = Walll(1777/1920 * window_width, 295/1080 * window_height, 1764/1920 * window_width, 392/1080 * window_height, batch)

    line_list = [line, line1, line2]
    return line_list