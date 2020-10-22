""" ship.py

Contains logic for ship validation, hit detection, ship destruction.

Only valid for an 8 x 8 board.

"""

from .coordinate import Coordinate

class Ship:
    def __init__(self, coord_1, coord_2, length=None):
        """Create the ship and perform validation on a ship position"""
        
        alpha_list = ["A", "B", "C", "D", "E", "F", "G", "H"]
        digit_list = ["1", "2", "3", "4", "5", "6", "7", "8"]

        row, col = False, False

        # Check if on a row
        if coord_1.row == coord_2.row:
            # On a row
            calculated_length = abs(coord_1.col_idx - coord_2.col_idx) + 1
            row = True
        elif coord_1.col == coord_2.col:
            # On a column
            calculated_length = abs(coord_1.row_idx - coord_2.row_idx) + 1
            col = True
        else:
            raise Exception("Invalid coordinate placement, ship is not linear!")
        
        if length and calculated_length != length:
            # In addition for checking linearity, we need to check length as well
            raise Exception("Invalid coordinate placement, length is incorrect!")

        self.length = calculated_length
        
        # Populate the ship coordinate list for easy hit detection
        self.coordinate_list = []
        self.hits_list = [None for x in range(0, self.length)]

        if row:
            left_most = min(coord_1.col_idx, coord_2.col_idx)
            right_most = max(coord_1.col_idx, coord_2.col_idx)
            
            for idx in range(left_most, right_most + 1):
                col_str = alpha_list[idx]
                self.coordinate_list.append(Coordinate(col_str + coord_1.row))

        elif col:
            top_most = min(coord_1.row_idx, coord_2.row_idx)
            bottom_most = max(coord_1.row_idx, coord_2.row_idx)
            
            for idx in range(top_most, bottom_most + 1):
                row_str = digit_list[idx]
                self.coordinate_list.append(Coordinate(coord_1.col + row_str))

    def check_if_hit(self, coordinate):
        """Check for a hit by comparing coordinates to input coordinate.

        If a coordinate matches, a hit is registered. The ship will store 
        hits, and if the hits_list is all True, then the ship is destroyed.

        Returns a tuple, with the first a bool for hit or miss, and the second 
        value a bool for ship destroyed.
        """

        hit = False
        destroyed = False

        for idx, coord in enumerate(self.coordinate_list):
            if str(coord) == str(coordinate):
                hit = True
                self.hits_list[idx] = True

        if all(self.hits_list):
            destroyed = True

        return (hit, destroyed)
                

    def __str__(self):
        return str([str(coord) for coord in self.coordinate_list])