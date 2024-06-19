from graphics import Window
from maze import Maze  # Ensure the correct path if maze is in a different directory
import sys

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    # Create maze instance with a specific seed for reproducibility
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=1)
    print("Maze created")

    is_solvable = maze.solve()
    if not is_solvable:
        print("Maze cannot be solved!")
    else:
        print("Maze solved!")
        
    win.wait_for_close()

if __name__ == "__main__":
    main()