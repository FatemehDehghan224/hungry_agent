import random
from typing import List, Tuple
from .environment import Environment

def create_random_environment(rows: int, cols: int) -> Environment:
    start = (random.randint(1, rows - 2), random.randint(1, cols - 2))
    food = (random.randint(1, rows - 2), random.randint(1, cols - 2))
    walls = {(i, j) for i in range(rows) for j in range(cols) if i == 0 or j == 0 or i == rows - 1 or j == cols - 1}

    while start in walls:
        start = (random.randint(1, rows - 2), random.randint(1, cols - 2))
    while food in walls or food == start:
        food = (random.randint(1, rows - 2), random.randint(1, cols - 2))

    for _ in range(random.randint(rows * cols // 10, rows * cols // 5)):
        new_wall = (random.randint(1, rows - 2), random.randint(1, cols - 2))
        if new_wall != start and new_wall != food:
            walls.add(new_wall)

    return Environment(rows, cols, start, food, walls)

def read_input(file_path: str) -> Tuple[int, int, Tuple[int, int], List[List[str]]]:
    with open(file_path, 'r', encoding='utf-8') as file:
        first = file.readline().strip().replace(",", " ")
        if not first:
            raise ValueError("Input file empty or invalid first line")
        m, n = map(int, first.split())
        line = file.readline().strip()
        if ',' in line:
            sx, sy = map(int, line.split(','))
        else:
            sx, sy = map(int, line.split())
        grid = []
        for line in file:
            cleaned = line.strip()
            if cleaned:
                row = [ch for ch in cleaned if ch != ' ']
                grid.append(row)

    if len(grid) != m or any(len(row) != n for row in grid):
        print(f"Warning: Grid dimensions do not match: expected {m}x{n}, got {len(grid)}x{(len(grid[0]) if grid else 0)}")

    return m, n, (sx, sy), grid

def dfs_text(grid: List[List[str]], start: Tuple[int, int]):
    """
    A stack-based DFS for text mode.
    Returns: (path_list, steps, food_pos)
    path_list contains tuples (x,y,move) and last item may be (x,y)
    """
    rows, cols = len(grid), len(grid[0])
    stack = [(start, [])]
    visited = set()
    directions = [(-1, 0, 1), (1, 0, 3), (0, -1, 4), (0, 1, 2)]
    food_pos = None

    while stack:
        (x, y), path = stack.pop()
        if not (0 <= x < rows and 0 <= y < cols):
            continue
        if (x, y) in visited:
            continue
        if grid[x][y] == '*':
            continue

        visited.add((x, y))

        if grid[x][y] in ('f', 'F'):
            food_pos = (x, y)
            path.append((x, y))
            return path, len(path) - 1, food_pos

        for dx, dy, move in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] != '*':
                stack.append(((nx, ny), path + [(x, y, move)]))

    return [], 0, (-1, -1)
