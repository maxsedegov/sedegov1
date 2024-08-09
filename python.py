
import pygame
import random
import time


pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Цвета
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Настройки экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fire Fighting Game")

# Игровые объекты
class Helicopter:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.water = 0
        self.health = 3
        self.score = 0

    def move(self, dx, dy):
        self.x = (self.x + dx) % GRID_WIDTH
        self.y = (self.y + dy) % GRID_HEIGHT

    def collect_water(self):
        if self.water < 5:
            self.water += 1

    def extinguish_fire(self):
        # Логика тушения пожара
        pass

class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.on_fire = False

    def grow(self):
        # Логика роста дерева
        pass

class River:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def create_grid():
    grid = []
    for _ in range(GRID_WIDTH):
        column = []
        for _ in range(GRID_HEIGHT):
            # Генерация объектов
            entity = random.choice([None, River(random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1)), Tree(random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))])
            column.append(entity)
        grid.append(column)
    return grid

def draw_grid(grid):
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            entity = grid[x][y]
            if isinstance(entity, Tree):
                color = BROWN if not entity.on_fire else RED
                pygame.draw.rect(screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            elif isinstance(entity, River):
                pygame.draw.rect(screen, BLUE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def main():
    helicopter = Helicopter()
    grid = create_grid()

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)
        draw_grid(grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            helicopter.move(0, -1)
        if keys[pygame.K_DOWN]:
            helicopter.move(0, 1)
        if keys[pygame.K_LEFT]:
            helicopter.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            helicopter.move(1, 0)

        # Логика игры, генерация пожаров, баллов и т.д.
        
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()