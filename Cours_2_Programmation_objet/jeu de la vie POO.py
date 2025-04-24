class Cell:
    """
    Représente une cellule individuelle de la grille.
    Elle possède un attribut alive qui indique si la cellule est vivante (True) ou morte (False).
    Par défaut, une cellule est morte.
    """
    def __init__(self, alive=False):
        self.alive = alive

    def __str__(self):
        return '■' if self.alive else ' '

import random
import copy

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(random.choice([True, False])) for _ in range(cols)] for _ in range(rows)]

    def display(self):
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))
        print()

    def count_alive_neighbors(self, x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < self.rows) and (0 <= ny < self.cols):
                if self.grid[nx][ny].alive:
                    count += 1
        return count

    def update(self):
        new_grid = copy.deepcopy(self.grid)
        for x in range(self.rows):
            for y in range(self.cols):
                alive_neighbors = self.count_alive_neighbors(x, y)
                if self.grid[x][y].alive:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_grid[x][y].alive = False
                else:
                    if alive_neighbors == 3:
                        new_grid[x][y].alive = True
        self.grid = new_grid


import time

class Game:
    def __init__(self, rows, cols, generations=50, delay=0.3):
        self.grid = Grid(rows, cols)
        self.generations = generations
        self.delay = delay

    def run(self):
        for _ in range(self.generations):
            self.grid.display()
            self.grid.update()
            time.sleep(self.delay)

game = Game(rows=20, cols=40, generations=100)
game.run()
