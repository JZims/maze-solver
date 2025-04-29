from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")

        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(
            self.root, 
            width = width, 
            height = height,
            bg="white"
        )
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False

    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def draw_line(self, line, fill_color):
        if not isinstance(line, Line):
            raise TypeError("Line input must be Line type")
        line.draw(self.canvas, fill_color)

    def close(self):
        self.running = False

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1, p2):
        if not isinstance(p1, Point) and not isinstance(p2, Point):
            raise TypeError("Input must be a Point")
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas:Canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

