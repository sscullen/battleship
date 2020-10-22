from .coordinate import Coordinate
from .ship import Ship
from .board import Board


def place_ship():
    """Get input from the user to place their ship
    
    This function checks for valid input from the user and will continue to 
    loop until valid inputs are provided
    """

    coord_1 = None
    coord_2 = None
    ship_valid = False
    while not coord_1 or not coord_2 or not ship_valid:

        if not coord_1:
            coord_1_string = input("Ship coordinate 1: ")
            try:
                coord_1 = Coordinate(coord_1_string)
            except Exception as e:
                print(f"Sorry, that's not a valid coordinate ({str(e)})")
                print(f"Try again!")
                coord_1 = None
                continue
        
        coord_2_string = input("Ship coordinate 2: ")
        try:
            coord_2 = Coordinate(coord_2_string)
        except Exception as e:
            print(f"Sorry, that's not a valid coordinate ({str(e)})")
            print(f"Try again!")
            coord_2 = None
            continue

        print("Checking if ship placement is valid (linear with length 3)...")

        try:
            ship = Ship(coord_1, coord_2, length=3)
        except Exception as e:
            print(f"Whoops! Your ship placement isn't correct. ({str(e)})")
            print("Try again!")
            coord_1 = None
            coord_2 = None
            continue
        else:
            print(f"Great! Your ship is deployed!")
            ship_valid = True

    return ship

    
def get_target_coordinate():
    """Get input from the user for their selected target"""

    coord_valid = False

    while not coord_valid:
        coord_string = input("Enter the coordinate you want to fire at: ")

        try:
            target_coord = Coordinate(coord_string)
        except Exception as e:
            print(f"Your target coordinate was invalid! ({str(e)})")
            print("Try again!")
        else:
            coord_valid = True

    return target_coord