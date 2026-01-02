import random


class Cell:
    def __init__(self, alive: bool, i: int, j: int):
        self.alive = alive
        self.i = i
        self.j = j

    def __str__(self):
        if not self.alive:
            return " "
        return "#"

    def set_alive(self, alive):
        self.alive = alive


class Grid:
    def __init__(self, rows: int, columns: int, grid_option: int):
        self.rows = rows
        self.columns = columns
        if grid_option == 1:
            self.grid = self.random()
        elif grid_option == 2:
            self.grid = self.glider()
        elif grid_option == 3:
            self.grid = self.whole()

    def __str__(self):
        grid = ""
        for row in self.grid:
            for cell in row:
                grid += str(cell)
            grid += "\n"
        return grid

    def count_alive_neighbors(self, row, col):
        neighbors_count = 0

        for neighbor_row in range(row - 1, row + 2):  # going through upper row, current row, lower row
            for neighbor_col in range(col - 1, col + 2):  # going through upper column, current column, lower column
                if neighbor_row == row and neighbor_col == col:  # then we are not in the cell itself
                    continue
                if 0 <= neighbor_row <= self.rows - 1 and 0 <= neighbor_col <= self.columns - 1:
                    if self.grid[neighbor_row][neighbor_col].alive:
                        neighbors_count += 1
        return neighbors_count

    def next_step(self):
        new_grid = self.empty()
        for i in range(self.rows):
            for j in range(self.columns):
                neighbors_count = self.count_alive_neighbors(i, j)
                if self.grid[i][j].alive:
                    if neighbors_count < 2 or neighbors_count > 3:
                        new_grid[i][j].alive = False
                    else:
                        new_grid[i][j].alive = True
                else:
                    if neighbors_count == 3:
                        new_grid[i][j].alive = True
                    else:
                        new_grid[i][j].alive = False

        self.grid = new_grid

    def glider(self, starting_row=10, starting_column=10):
        grid = []
        for i in range(self.rows):
            cells_list = []
            for j in range(self.columns):
                alive = (i == starting_row and j == starting_column or
                         i == starting_row + 1 and j == starting_column + 1 or
                         i == starting_row + 2 and j == starting_column - 1 or
                         i == starting_row + 2 and j == starting_column or
                         i == starting_row + 2 and j == starting_column + 1)
                cell = Cell(alive, i, j)
                cells_list.append(cell)
            grid.append(cells_list)
        return grid

    def random(self):
        grid = []
        for i in range(self.rows):
            cells_list = []
            for j in range(self.columns):
                alive = random.choice([True, False])
                cell = Cell(alive, i, j)
                cells_list.append(cell)
            grid.append(cells_list)
        return grid

    def whole(self):
        grid = []
        for i in range(self.rows):
            cells_list = []
            for j in range(self.columns):
                cell = Cell(True, i, j)
                cells_list.append(cell)
            grid.append(cells_list)
        return grid

    def empty(self):
        grid = []
        for i in range(self.rows):
            cells_list = []
            for j in range(self.columns):
                cell = Cell(False, i, j)
                cells_list.append(cell)
            grid.append(cells_list)
        return grid
