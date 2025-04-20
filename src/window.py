from tkinter import Tk, BOTH, Canvas
from src.line import Line

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Amazing Maze Solver"
        self.__canvas = Canvas(self.__root, bg="gray60", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

