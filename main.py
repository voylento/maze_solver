from src.window import Window 
from src.maze import Maze

def main():
    top_bar = 40
    right_bar = 20
    bottom_bar = 40
    left_bar = 20

    columns = 40
    rows = 40 

    width = 1600
    height = 1200
    window = Window(width + left_bar + right_bar, height + top_bar + bottom_bar)

    cell_width = width / columns
    cell_height = height / rows

    maze = Maze(left_bar, top_bar, columns, rows, cell_width, cell_height, window)
    result = maze.solve()
    if not result:
        print("You LOSE!")
    else:
        print("YOU WIN!!!")

    window.wait_for_close()


if __name__=="__main__":
    main()
