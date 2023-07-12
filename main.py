import pygame
import random

# Define the size of the grid and the screen
GRID_SIZE = (800, 600)
CELL_SIZE = 20
GRID_WIDTH = GRID_SIZE[0] // CELL_SIZE
GRID_HEIGHT = GRID_SIZE[1] // CELL_SIZE

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode(GRID_SIZE)
pygame.display.set_caption("Slime Mold Pathfinding")

# Create a 2D grid to represent the environment
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Create the start and goal positions
start_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
goal_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Set the start and goal positions in the grid
grid[start_pos[1]][start_pos[0]] = 1
grid[goal_pos[1]][goal_pos[0]] = 2

# Define the directions (N, E, S, W)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Define the slime mold class
class SlimeMold:
    def __init__(self, position):
        self.position = position
        self.strength = 100

    def move(self):
        neighbors = []
        for direction in directions:
            neighbor_x = self.position[0] + direction[0]
            neighbor_y = self.position[1] + direction[1]
            if 0 <= neighbor_x < GRID_WIDTH and 0 <= neighbor_y < GRID_HEIGHT:
                neighbors.append((neighbor_x, neighbor_y))

        if neighbors:
            next_position = random.choice(neighbors)
            self.position = next_position
            self.strength -= 1

# Create a list of slime molds
slime_molds = [SlimeMold(start_pos) for _ in range(50)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the slime molds
    for slime_mold in slime_molds:
        slime_mold.move()
        grid[slime_mold.position[1]][slime_mold.position[0]] = 1

    # Display the grid
    screen.fill(BLACK)
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if grid[row][col] == 0:
                color = WHITE
            elif grid[row][col] == 1:
                color = GREEN
            else:
                color = RED
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

# Quit the program
pygame.quit()
