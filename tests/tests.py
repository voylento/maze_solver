import unittest

from src.maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_1x1(self):
        cols = 1
        rows = 1
        m1 = Maze(0, 0, cols, rows, 1, 1)
        self.assertEqual(
                len(m1.cells),
                cols
            )
        self.assertEqual(
                len(m1.cells[0]),
                rows
            )

    def test_maze_create_12x10(self):
        cols = 12
        rows = 10
        m1 = Maze(0, 0, cols, rows, 10, 10)
        print(f"{cols}x{rows} maze, max depth = {m1.max_depth}")
        self.assertEqual(
                len(m1.cells),
                cols
            )
        self.assertEqual(
                len(m1.cells[0]),
                rows
            )

    def test_maze_create_cells_100x100(self):
        cols = 25
        rows = 25
        cell_size_x = 10
        cell_size_y = 10
        m1 = Maze(100, 100, cols, rows, cell_size_x, cell_size_y)
        print(f"{cols}x{rows} maze, max depth = {m1.max_depth}")
        self.assertEqual(
                len(m1.cells),
                cols
            )
        self.assertEqual(
                len(m1.cells[0]),
                rows
            )

        for cell in m1.cells[0]:
            cell_width = abs(cell.p2.x - cell.p1.x)
            cell_height = abs(cell.p2.y - cell.p1.y)
            self.assertEqual(
                    cell_width,
                    cell_size_x
                )
            self.assertEqual(
                    cell_height,
                    cell_size_y
                )

    def test_maze_entrance_exit_walls(self):
        cols = 20
        rows = 20
        maze = Maze(0, 0, cols, rows, 10, 10)
        print(f"{cols}x{rows} maze, max depth = {maze.max_depth}")
        self.assertTrue(maze.cells[0][0].has_top_wall == False)
        self.assertTrue(maze.cells[maze.c_cols - 1][maze.c_rows -1].has_bottom_wall == False)

    def test_no_cell_closed(self):
        cols = 45
        rows = 45
        maze = Maze(0, 0, cols, rows, 10, 10)
        print(f"{cols}x{rows} maze, max depth = {maze.max_depth}")
        for i in range(0, cols):
            for j in range(0, rows):
                c_walls = 0
                if maze.cells[i][j].has_top_wall:
                    c_walls += 1
                if maze.cells[i][j].has_right_wall:
                    c_walls += 1
                if maze.cells[i][j].has_bottom_wall:
                    c_walls += 1
                if maze.cells[i][j].has_left_wall:
                    c_walls += 1
                self.assertTrue(c_walls != 4)

    def test_cells_visited_reset(self):
        cols = 30
        rows = 30
        maze = Maze(0, 0, cols, rows, 10, 10)
        for i in range(0, cols):
            for j in range(0, rows):
                self.assertTrue(maze.cells[i][j].visited == False)


if __name__=="__main__":
    unittest.main()

