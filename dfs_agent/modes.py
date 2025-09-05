from typing import Tuple
from .utils import create_random_environment, read_input, dfs_text
from .agent import Agent
from .visualization import run_visualization

def _prompt_dimensions() -> Tuple[int, int]:
    while True:
        rows_input = input("Enter number of rows: ").strip()
        cols_input = input("Enter number of columns: ").strip()
        if not rows_input or not cols_input:
            print("Error: Input cannot be empty. Please enter valid dimensions.")
            continue
        try:
            rows = int(rows_input)
            cols = int(cols_input)
        except ValueError:
            print("Error: Please enter valid integers for rows and columns.")
            continue
        if rows >= 3 and cols >= 3:
            return rows, cols
        else:
            print("Error: Number of rows and columns must be at least 3. Please enter valid dimensions.")

def text_mode():
    path = input("Enter input file path (press Enter to use data/input.txt): ").strip()
    if not path:
        path = "data/input.txt"
    try:
        m, n, start, grid = read_input(path)
    except Exception as e:
        print("Error reading input file:", e)
        return
    path_list, steps, food_pos = dfs_text(grid, start)
    print("Start Position:", start)
    print("Food Position:", food_pos)
    print("Total Moves:", steps)
    print("Path:", path_list)

def random_mode():
    rows, cols = _prompt_dimensions()
    env = create_random_environment(rows, cols)
    print("Initial situation (A = agent, F = food, * = wall):")
    env.display(env.start)
    agent = Agent(env)
    path = agent.dfs_random(env.start)  # list of (pos, direction)
    print("\nPath:")
    for pos, direction in path:
        if direction:
            print(f"{pos} --> {direction}")
        else:
            print(f"{pos} (food)")
    print("\nNumber of moves:", len(path))
    print("End game food place:", env.food)

def graphic_mode():
    rows, cols = _prompt_dimensions()
    env = create_random_environment(rows, cols)
    agent = Agent(env)
    path = agent.dfs_graphic(env.start)  # list of positions
    if not path:
        print("No path found to food.")
        return
    run_visualization(env, path)
