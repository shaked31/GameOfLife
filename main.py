from classes import *
import os
import time


def main():
    while True:
        try:
            user_choice = int(input("Choose grid:\n(1) Random Grid\n(2) Glider Grid\n(3) Whole Grid\n"))
            if user_choice not in (1, 2, 3):
                raise ValueError
            break

        except ValueError as e:
            print("Must Enter a valid int")

    grid = Grid(20, 20, user_choice)
    print(grid)
    while True:
        os.system("cls")
        grid.next_step()
        print(grid)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
