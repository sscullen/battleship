import unittest
from pathlib import Path

TEST_DIR = Path(__file__).absolute().parent

from battleship.coordinate import Coordinate

class TestCoordinate(unittest.TestCase):
    def setUp(self):
        pass

    def test_coordinate_valid(self):
        coordinate_string = "A2"

        coordinate = Coordinate(coordinate_string)

        self.assertEqual(coordinate.col, 'A')
        self.assertEqual(coordinate.row, '2')
        self.assertEqual(coordinate.col_idx, 0)
        self.assertEqual(coordinate.row_idx, 1)

        coordinate_string = "5B"

        coordinate = Coordinate(coordinate_string)

        self.assertEqual(coordinate.col, 'B')
        self.assertEqual(coordinate.row, '5')
        self.assertEqual(coordinate.col_idx, 1)
        self.assertEqual(coordinate.row_idx, 4)

    def test_coordinate_invalid_length(self):
        coordinate_string = "AA2"

        with self.assertRaises(Exception):
            Coordinate(coordinate_string)
        
    def test_coordinate_invalid_format(self):
        coordinate_string = "AA"

        with self.assertRaises(Exception):
            Coordinate(coordinate_string)

    def test_coordinate_invalid_out_of_range(self):
        coordinate_string = "I8"

        with self.assertRaises(Exception):
            Coordinate(coordinate_string)

        coordinate_string = "9A"

        with self.assertRaises(Exception):
            Coordinate(coordinate_string)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()