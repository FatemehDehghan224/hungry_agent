import random
from typing import List, Tuple, Optional
from .environment import Environment

class Agent:
    def __init__(self, environment: Environment):
        self.environment = environment

    def dfs_random(self, position: Tuple[int, int]) -> List[Tuple[Tuple[int, int], Optional[str]]]:
        """
        DFS with random neighbor order.
        Returns list of (position, direction) from start to food. Last item has direction=None.
        """
        visited = set()
        path: List[Tuple[Tuple[int,int], Optional[str]]] = []
        directions = [((-1, 0), "Up"), ((0, 1), "Right"), ((1, 0), "Down"), ((0, -1), "Left")]

        def dfs(pos):
            if pos == self.environment.food:
                path.append((pos, None))
                return True
            visited.add(pos)
            dirs = directions[:]
            random.shuffle(dirs)
            for move, name in dirs:
                new = (pos[0] + move[0], pos[1] + move[1])
                if new not in visited and self.environment.is_valid(new):
                    if dfs(new):
                        path.append((pos, name))
                        return True
            visited.remove(pos)
            return False

        dfs(position)
        path.reverse()
        return path

    def dfs_graphic(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Deterministic DFS used for visualization.
        Returns list of positions from start to food (inclusive).
        """
        visited = set()
        path: List[Tuple[int, int]] = []
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(pos):
            if pos == self.environment.food:
                path.append(pos)
                return True
            visited.add(pos)
            for move in directions:
                new = (pos[0] + move[0], pos[1] + move[1])
                if new not in visited and self.environment.is_valid(new):
                    if dfs(new):
                        path.append(pos)
                        return True
            return False

        dfs(position)
        path.reverse()
        return path
