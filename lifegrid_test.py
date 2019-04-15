# Program for playing the game of Life.
import time
from lifegrid import LifeGrid

# Define the initial configuration of live cells.
INIT_CONFIG = [(1, 1), (1, 2), (2, 2), (3, 2)]


def main():
    '''
     Constructs the game grid and configure it.
    '''
    grid_width = int(input("Enter the width:"))
    grid_height = int(input("Enter the height:"))
    num_gens = int(input("Enter the number of generations"))
    grid = LifeGrid(grid_width, grid_height)
    try:
        grid.configure(INIT_CONFIG)
        # Plays the game.
        print(draw(grid))
        # print("neighbour:",grid.num_live_neighbors(0, 0))
        # print("neighbours:",grid.num_live_neighbors(1, 1))
        for i in range(num_gens):
            evolve(grid)
            time.sleep(1)
            print(draw(grid))
    except IndexError:
        print("Please change INIT_CONFIG in correspondance to the chosen width and height")


def evolve(grid):
    '''
    Generates the next generation of organisms.
    :param grid:LifeGrid
    :return:None
    '''
    # List for storing the live cells of the next generation.
    live_cells = []
    # Iterate over the elements of the grid.
    for i in range(grid.num_rows()):
        for j in range(grid.num_cols()):
            # Determine the number of live neighbors for this cell.
            neighbors = grid.num_live_neighbors(i, j)
            # Add the (i,j) tuple to liveCells if this cell contains
            # a live organism in the next generation.
            if (neighbors == 2 and grid.is_live_cell(i, j)) or (neighbors == 3):
                live_cells.append((i, j))
    print("live_cells", live_cells)
    # Reconfigure the grid using the liveCells coord list.
    for i in range(grid.num_rows()):
        for j in range(grid.num_cols()):
            grid.clear_cell(i, j)
    grid.configure(live_cells)


def draw(grid):
    '''
    Prints a text based representation of the game grid.
    :param grid:list
    :return: str
    '''
    cells = ""
    for i in range(grid.num_rows()):
        for j in range(grid.num_cols()):
            if grid._grid.__getitem__((i, j)):
                cells += grid._grid.__getitem__((i, j))
            else:
                cells += " "
        cells += "\n"
    return cells


# Executes the main routine.
main()
