""" board.py

Data class for storing board state for a battleship game.

"""

from tabulate import tabulate
import string

class Board:

    def __init__(self, width=8, height=8):
        self.width = width
        self.height = height

        # create an empty board
        self.board_state = [[" "] * width for i in range(height)]
        
    def update_board(self, coordinate, hit):
        """Update the board using the coordinate numeric indexes.

        If hit is true, an "H" is stored in that location, else an "M" is.
        """
        
        if hit:
            self.board_state[coordinate.row_idx][coordinate.col_idx] = "H"
        else:
            self.board_state[coordinate.row_idx][coordinate.col_idx] = "M"


    def __str__(self):
        """Utilizes tabulate to provide a visual representation of the board state."""

        # Create grid headers for the table
        headers = [letter for letter in string.ascii_uppercase[:self.width]]

        board_state = []
        board_state.extend([[value for value in row] for i, row in enumerate(self.board_state)])

        for idx, row in enumerate(board_state):
            row.insert(0, idx + 1)

        return tabulate(board_state, headers, tablefmt="grid")
