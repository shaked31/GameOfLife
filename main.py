from classes import *
import os
import time


def main():
    grid = Grid(20, 20, 2)
    print(grid)
    while True:
        os.system("cls")
        grid.next_step()
        print(grid)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
