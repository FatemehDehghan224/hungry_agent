from dfs_agent.environment import Environment
from dfs_agent.agent import Agent

def test_agent_finds_path():
    rows, cols = 5, 5
    start = (1,1)
    food = (3,3)
    walls = {(0,i) for i in range(cols)} | {(rows-1,i) for i in range(cols)} | {(i,0) for i in range(rows)} | {(i,cols-1) for i in range(rows)}
    walls.remove((1,0)) if (1,0) in walls else None
    env = Environment(rows, cols, start, food, walls)
    agent = Agent(env)
    path = agent.dfs_graphic(start)
    assert path and path[0] == start
    assert food in path
