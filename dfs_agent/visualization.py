import pygame
from .constants import CELL_SIZE, WHITE, BLACK, BLUE, GREEN

def draw_grid(screen, env, agent_position):
    screen.fill(WHITE)
    for r in range(env.rows):
        for c in range(env.cols):
            pos = (r, c)
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if pos == agent_position:
                pygame.draw.rect(screen, BLUE, rect)
            elif pos == env.food:
                pygame.draw.rect(screen, GREEN, rect)
            elif pos in env.walls:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

def run_visualization(env, path, delay_ms=300):
    try:
        pygame.init()
        screen = pygame.display.set_mode((env.cols * CELL_SIZE, env.rows * CELL_SIZE))
        pygame.display.set_caption("DFS Visualization")
        clock = pygame.time.Clock()
        for agent_position in path:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            draw_grid(screen, env, agent_position)
            pygame.display.flip()
            pygame.time.delay(delay_ms)
            clock.tick(60)
    finally:
        pygame.quit()
