""" coordinate.py

Contains coordinate validation logic. Only valid for an 8 x 8 board.

"""

import re
import string

class Coordinate:
    def __init__(self, coordinate_string):
        """Create the coordinate and provide validation for valid coordinate format"""
        
        assert len(coordinate_string) == 2, "Invalid length for a coordinate."

        alpha_list = ["A", "B", "C", "D", "E", "F", "G", "H"]
        digit_list = ["1", "2", "3", "4", "5", "6", "7", "8"]

        first_part = coordinate_string[:1]
        second_part = coordinate_string[1:]

        if str(first_part) in alpha_list and str(second_part) in digit_list:
            self.row = str(second_part)
            self.col = str(first_part).upper()
        elif str(second_part) in alpha_list and str(first_part) in digit_list:
            self.row = str(first_part)
            self.col = str(second_part).upper()
        else:
            raise Exception("Invalid format for a coordinate.")

        # Create index for accessing 2D list
        self.row_idx = int(self.row) - 1
        self.col_idx = string.ascii_uppercase.find(self.col)

       
    def __str__(self):
        return f"{self.col}{self.row}"

