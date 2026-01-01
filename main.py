from classes import *
def init_cells() -> Grid:
    cells_list = []
    grid = []
    for i in range(20):
        for j in range(20):
            if i%2==0 and j%2==0:
                cell = Cell(True, i, j)
            else:
                cell = Cell(False, i, j)
            cells_list.append(cell)
        grid.append(cells_list)
    grid = Grid(grid)
    return grid
def main():
    grid = init_cells()
    print(grid)

if __name__ == "__main__":
    main()