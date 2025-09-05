from typing import Set, Tuple

class Environment:
    def __init__(self, rows: int, cols: int, start: Tuple[int, int], food: Tuple[int, int], walls: Set[Tuple[int, int]]):
        self.rows = rows
        self.cols = cols
        self.start = start
        self.food = food
        self.walls = set(walls)

    def is_valid(self, position: Tuple[int, int]) -> bool:
        r, c = position
        return 0 <= r < self.rows and 0 <= c < self.cols and position not in self.walls

    def display(self, agent_position: Tuple[int, int]):
        for r in range(self.rows):
            for c in range(self.cols):
                pos = (r, c)
                if pos == agent_position:
                    print("A", end=" ")
                elif pos == self.food:
                    print("F", end=" ")
                elif pos in self.walls:
                    print("*", end=" ")
                else:
                    print(".", end=" ")
            print()
