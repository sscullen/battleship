import io
import sys
import unittest

from ..ship import Ship
from ..coordinate import Coordinate

class TestShip(unittest.TestCase):
    def setUp(self):
        pass

    def test_ship_valid_column(self):
        coordinate_string_1 = "A1"
        coordinate_1 = Coordinate(coordinate_string_1)

        coordinate_string_2 = "A3"
        coordinate_2 = Coordinate(coordinate_string_2)

        ship = Ship(coordinate_1, coordinate_2)

        self.assertEqual([str(coord) for coord in ship.coordinate_list], ["A1", "A2", "A3"])

    def test_ship_valid_row(self):
        coordinate_string_1 = "A1"
        coordinate_1 = Coordinate(coordinate_string_1)

        coordinate_string_2 = "C1"
        coordinate_2 = Coordinate(coordinate_string_2)

        ship = Ship(coordinate_1, coordinate_2)

        self.assertEqual([str(coord) for coord in ship.coordinate_list], ["A1", "B1", "C1"])
        
    def test_ship_invalid_shape(self):
        coordinate_string_1 = "A1"
        coordinate_1 = Coordinate(coordinate_string_1)

        coordinate_string_2 = "B3"
        coordinate_2 = Coordinate(coordinate_string_2)

        with self.assertRaises(Exception):
            Ship(coordinate_1, coordinate_2)

    def test_ship_invalid_length(self):
        coordinate_string_1 = "A1"
        coordinate_1 = Coordinate(coordinate_string_1)

        coordinate_string_2 = "A4"
        coordinate_2 = Coordinate(coordinate_string_2)

        with self.assertRaises(Exception):
            Ship(coordinate_1, coordinate_2, length=3)

    def test_ship_check_if_hit(self):
        coordinate_string_1 = "A1"
        coordinate_1 = Coordinate(coordinate_string_1)

        coordinate_string_2 = "A3"
        coordinate_2 = Coordinate(coordinate_string_2)

        ship = Ship(coordinate_1, coordinate_2, length=3)

        target_coord = Coordinate("A1")

        shot_result = ship.check_if_hit(target_coord)

        self.assertTrue(shot_result[0])

    def test_ship_check_if_miss(self):
        coordinate_string_1 = "A1"
        coordinate_1 = Coordinate(coordinate_string_1)

        coordinate_string_2 = "A3"
        coordinate_2 = Coordinate(coordinate_string_2)

        ship = Ship(coordinate_1, coordinate_2, length=3)

        target_coord = Coordinate("D1")

        shot_result = ship.check_if_hit(target_coord)

        self.assertFalse(shot_result[0])

    def test_ship_check_ship_destroyed(self):
        coordinate_string_1 = "A1"
        coordinate_1 = Coordinate(coordinate_string_1)

        coordinate_string_2 = "A3"
        coordinate_2 = Coordinate(coordinate_string_2)

        ship = Ship(coordinate_1, coordinate_2, length=3)

        target_coord1 = Coordinate("A1")
        target_coord2 = Coordinate("A2")
        target_coord3 = Coordinate("A3")

        shot_result = ship.check_if_hit(target_coord1)

        self.assertTrue(shot_result[0])
        self.assertFalse(shot_result[1])

        shot_result = ship.check_if_hit(target_coord2)

        self.assertTrue(shot_result[0])
        self.assertFalse(shot_result[1])

        shot_result = ship.check_if_hit(target_coord3)

        self.assertTrue(shot_result[0])
        self.assertTrue(shot_result[1])

    def test_ship_test_print(self):
        coordinate_string_1 = "A1"
        coordinate_1 = Coordinate(coordinate_string_1)

        coordinate_string_2 = "A3"
        coordinate_2 = Coordinate(coordinate_string_2)

        ship = Ship(coordinate_1, coordinate_2, length=3)
    
        # Redirect stdout to enable testing the ship visualization
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print(ship)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "['A1', 'A2', 'A3']")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()