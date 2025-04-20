# Maze Solver

Maze solver project from boot.dev

## Objectives
- Use depth first search with recursive backtracking to create an n x n maze
- Use depth first search with recursive backtracking to navigate from entry to exit

### How to run
python3 main.py

### Notes
Python does not do tail recursion optimization and has a default recursive depth limit of 1000.
Mazes greater than 40 x 40 fail due to exceeding the recursion depth limit. I created an iterative
version of creating the maze which works for any arbitrary size. I haven't done the iterative version
of the **solve** function. May or may not get to it, but the iterative version of the create_maze function
is a template for how to do it.

