from arrays import Array2D


class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.
        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._grid = Array2D(num_rows, num_cols)
        # Clears the grid and set all cells to dead.
        self.configure(list())

    def num_rows(self):
        """
        Returns the number of rows in the grid.
        :return: the number rows in the grid.
        """
        return self._grid.num_rows()

    def num_cols(self):
        """
        Returns the number of columns in the grid.
        :return:Returns the number of columns in the grid. 
        """
        return self._grid.num_cols()

    def configure(self, coord_list):
        """
        Configures the grid to contain the given live cells.
        :param coord_list: list
        :return: 
        """
        for tup in coord_list:
            self._grid.__setitem__(tup, "🌼")

    def is_live_cell(self, col, row):
        """
        Does the indicated cell contain a live organism?
        :param row: row of the cell.
        :param col: column of the cell.
        :return: the result of check.
        """
        if self._grid.__getitem__((col, row)) == "🌼":
            return True
        else:
            return False

    def check(self, tup):
        '''
        Checks whether the elements are bigger than 0 and less than number of cols(rows).
        :param tup: tuple
        :return: bool
        '''
        return 0 <= tup[0] <= self.num_cols() - 1 and 0 <= tup[1] <= self.num_rows() - 1

    def clear_cell(self, col, row):
        """
        Clears the indicated cell by setting it to dead.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        if self._grid.__getitem__((col, row)) == "🌼":
            self._grid.__setitem__((col, row), " ")

    def set_cell(self, col, row):
        """
        Sets the indicated cell to be alive.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self.__setitem__((col, row), "🌼")

    def num_live_neighbors(self, col, row):
        """
        Returns the number of live neighbors for the given cell
        :param row: row of the cell.
        :param col: column of the cell.
        :return: int
        """
        lst_indexes = [(col, row + 1), (col + 1, row + 1), (col - 1, row + 1), (col - 1, row), (col - 1, row - 1),
                       (col + 1, row), (col, row - 1), (col + 1, row - 1)]
        live_counter = 0
        # print("lst_indexes",lst_indexes)
        for tup in lst_indexes:
            # print(tup)
            if self.check(tup):
                if self._grid.__getitem__(tup) == "🌼":
                    live_counter += 1
        return live_counter
