import time
import random
from tkinter import Canvas
from src.window import Window
from src.cell import Cell
from src.point import Point
from src.line import Line

class Maze:
    def __init__(self, x, y, c_cols, c_rows, cell_size_x, cell_size_y, window=None, seed=None):
        self.x = x
        self.y = y
        self.c_cols = c_cols
        self.c_rows = c_rows
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.max_depth = 0
        if seed:
            random.seed(self.seed)
        else:
            random.seed()

        self.cells = self.create_cells()
        self.break_entrance_and_exit()
        self.create_path_iter()
        # self.create_path_r(
        #         random.randrange(0, self.c_cols), 
        #         random.randrange(0, self.c_rows)
        #     )
        self.reset_cells_to_unvisited()
        self.draw_cells()
    
    def create_cells(self):
        maze = []
        x_col_pos = self.x
        y_col_pos = self.y

        for i in range(self.c_cols):
            column = []
            curr_y_pos = self.y
            for j in range(self.c_rows):
                p1 = Point(x_col_pos, curr_y_pos)
                p2 = Point(x_col_pos + self.cell_size_x, curr_y_pos + self.cell_size_y)
                cell = Cell(p1, p2, self.window)
                column.append(cell)
                curr_y_pos += self.cell_size_y

            maze.append(column)
            x_col_pos += self.cell_size_x

        return maze

    def break_entrance_and_exit(self):
        entrance_cell = self.cells[0][0]
        entrance_cell.has_top_wall = False
        # entrance_cell.draw()

        exit_cell = self.cells[self.c_cols-1][self.c_rows-1]
        exit_cell.has_bottom_wall = False

    def create_path_iter(self):
        # iterative solution for creating maze after having written recursive one. Recursive exceeded Python's 
        # maximum recursive depth (default 1000) with a 50x50 maze.
        start = (random.randrange(self.c_cols), random.randrange(self.c_rows))
        stack = [start]

        while stack:
            i, j = stack[-1]
            self.cells[i][j].visited = True

            neighbors = []
            for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                ni, nj = i+di, j+dj
                if 0 <= ni < self.c_cols and 0 <= nj < self.c_rows:
                    if not self.cells[ni][nj].visited:
                        neighbors.append((ni, nj))

            if not neighbors:
                stack.pop()
            else:
                ni, nj = random.choice(neighbors)
                self.break_walls((i, j), (ni, nj))
                stack.append((ni, nj))

    def create_path_r(self, i, j, depth=0):
        # DFS recursive solution. Found that it has problems with mazes greater than 40x40 as Python's max recursive depth
        # is reached. Python doesn't have tail recursion optimization, sadly
        if depth > self.max_depth:
            self.max_depth = depth
        self.cells[i][j].visited = True

        while True:
            neighbors = []
            for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                ni, nj = i+di, j+dj
                if 0 <= ni < self.c_cols and 0 <= nj < self.c_rows:
                    if not self.cells[ni][nj].visited:
                        neighbors.append((ni, nj))

            if not neighbors:
                return

            ni, nj = random.choice(neighbors)
            self.break_walls((i, j), (ni, nj))

            self.create_path_r(ni, nj, depth+1)

    def break_walls(self, home_cell, adjacent_cell):
        i, j = home_cell
        ni, nj = adjacent_cell
        if i == ni:
            if j < nj:
                self.cells[i][j].has_bottom_wall = False
                self.cells[ni][nj].has_top_wall = False
            else:
                self.cells[i][j].has_top_wall = False
                self.cells[ni][nj].has_bottom_wall = False
        elif i < ni:
            self.cells[i][j].has_right_wall = False
            self.cells[ni][nj].has_left_wall = False
        else:
            self.cells[i][j].has_left_wall = False
            self.cells[ni][nj].has_right_wall = False


    def reset_cells_to_unvisited(self):
        for i in range(0, self.c_cols):
            for j in range(0, self.c_rows):
                self.cells[i][j].visited = False

    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, i, j):
        self.animate(.03)
        self.cells[i][j].visited = True

        if i == self.c_cols - 1 and j == self.c_rows - 1:
            return True

        while True:
            neighbors = []
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < self.c_cols and 0 <= nj < self.c_rows:
                    if self.no_wall(i, j, ni, nj) and not self.cells[ni][nj].visited:
                        neighbors.append((ni, nj))

            if not neighbors:
                return False

            next_i, next_j = neighbors[0]
            neighbors = neighbors[1:-1]
            self.cells[i][j].draw_move(self.cells[next_i][next_j])
            if not self.solve_r(next_i, next_j):
                self.cells[i][j].draw_move(self.cells[next_i][next_j], undo=True)
                self.animate(0.03)
            else:
                return True

        
    def no_wall(self, i, j, ni, nj):
        if i == ni:
            if j < nj:
                return self.cells[i][j].has_bottom_wall == False and self.cells[ni][nj].has_top_wall == False 
            else:
                return self.cells[i][j].has_top_wall == False and self.cells[ni][nj].has_bottom_wall == False
        elif i < ni:
            return self.cells[i][j].has_right_wall == False and self.cells[ni][nj].has_left_wall == False
        else:
            return self.cells[i][j].has_left_wall == False and self.cells[ni][nj].has_right_wall == False

    def solve_iter(self):
        pass

    def draw_cells(self):
        for col in self.cells:
            for cell in col:
                cell.draw()
                self.animate()

    def animate(self, sleep_time=None):
        if self.window:
            self.window.redraw()
            if sleep_time:
                time.sleep(sleep_time)
        
