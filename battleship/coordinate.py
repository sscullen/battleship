""" coordinate.py

Contains coordinate validation logic. Only valid for an 8 x 8 board.

"""

import re
import string

class Coordinate:
    def __init__(self, coordinate_string):
        assert(len(coordinate_string) == 2)

        first_part = coordinate_string[:1]
        second_part = coordinate_string[1:]

        if str(first_part).isalpha():
            assert(str(second_part).isdigit())
            self.row = str(second_part)
            self.col = str(first_part).upper()
        elif str(first_part).isdigit():
            assert(str(second_part).isalpha())
            self.row = str(first_part)
            self.col = str(second_part).upper()
        else:
            raise Exception("Invalid input for a coordinate.")

        # Create index for accessing 2D list
        self.row_idx = int(self.row) - 1
        self.col_idx = string.ascii_uppercase.find(self.col)

       
    def __str__(self):
        return f"{self.col}{self.row}"

