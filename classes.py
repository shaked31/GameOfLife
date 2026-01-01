class Cell:
    def __init__(self, alive: bool, i: int, j: int):
        self.alive = alive
        self.i = i
        self.j = j
    def __str__(self):
        if (not self.alive):
            return ""
        return "."

class Grid:
    def __init__(self, grid: list[list[Cell]]):
        self.grid = grid
    def __str__(self):
        grid = ""
        for row in self.grid:
            for cell in row:
                grid += str(cell)
        return grid