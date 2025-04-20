from src.window import Window
from src.point import Point
from src.line import Line

class Cell:
    def __init__(self, point1, point2, window=None):
        self.p1 = point1
        self.p2 = point2
        self.has_top_wall = self.has_right_wall = self.has_bottom_wall = self.has_left_wall = True
        self.window = window
        self.visited = False
        self.wall_color = "black"

    def draw(self):
        if self.has_top_wall:
            top_wall_left = self.p1
            top_wall_right = Point(self.p2.x, self.p1.y)
            top_wall = Line(top_wall_left, top_wall_right)
            if self.window:
                self.window.draw_line(top_wall, self.wall_color)

        if self.has_right_wall:
            top_right_wall = Point(self.p2.x, self.p1.y)
            bottom_right_wall = self.p2
            right_wall = Line(top_right_wall, bottom_right_wall)
            if self.window:
                self.window.draw_line(right_wall, self.wall_color)

        if self.has_bottom_wall:
            bottom_wall_left = Point(self.p1.x, self.p2.y)
            bottom_wall_right = self.p2
            bottom_wall = Line(bottom_wall_left, bottom_wall_right)
            if self.window:
                self.window.draw_line(bottom_wall, self.wall_color)

        if self.has_left_wall:
            left_wall_top = self.p1
            left_wall_bottom = Point(self.p1.x, self.p2.y)
            left_wall = Line(left_wall_top, left_wall_bottom)
            if self.window:
                self.window.draw_line(left_wall, self.wall_color)

    def draw_move(self, to_cell, undo=False):
        mid1 = abs(self.p2.x - self.p1.x) // 2
        mid2 = abs(to_cell.p2.x - to_cell.p1.x) // 2

        x_center = mid1 + self.p1.x
        y_center = mid1 + self.p1.y

        x_center2 = mid2 + to_cell.p1.x
        y_center2 = mid2 + to_cell.p1.y


        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        if self.window:
            self.window.draw_line(line, "red" if undo else "green3")

    def get_center_point(self):
        midx = abs(self.p2.x - self.p1.x) // 2
        midy = abs(self.p2.y - self.p1.y) // 2

        return midx + self.p1.x, midy + self.p1.y

