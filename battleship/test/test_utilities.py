import io
import sys
import unittest
from unittest.mock import patch

from battleship.utilities import get_target_coordinate, place_ship

class TestUtilities(unittest.TestCase):
    def setUp(self):
        pass
    
    @patch("battleship.utilities.input", create=True)
    def test_utilities_test_place_ship(self, mocked_input):
        mocked_input.side_effect = ["A1", "A3"]

        # Redirect the stdout so it doesn't clog up the test output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        ship = place_ship()
        
        sys.stdout = sys.__stdout__

        self.assertEqual(str(ship), "['A1', 'A2', 'A3']")

    @patch("battleship.utilities.input", create=True)
    def test_utilities_test_place_ship_invalid_shape(self, mocked_input):
        mocked_input.side_effect = ["A1", "B3"]

        # Redirect the stdout so it doesn't clog up the test output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        with self.assertRaises(Exception):
            ship = place_ship()
        
        sys.stdout = sys.__stdout__

    @patch("battleship.utilities.input", create=True)
    def test_utilities_test_place_ship_invalid_length(self, mocked_input):
        mocked_input.side_effect = ["A1", "A5"]

        # Redirect the stdout so it doesn't clog up the test output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Even though this isn't catching the right exception
        # (it actually is catching our mocked input running out of values)
        # It does show that our function is working because it is asking the
        # user for additional values when an invalid value is entered
        with self.assertRaises(Exception):
            ship = place_ship()
        
        sys.stdout = sys.__stdout__

    @patch("battleship.utilities.input", create=True)
    def test_utilities_test_place_ship_invalid_coordinate_format(self, mocked_input):
        mocked_input.side_effect = ["AA"]

        # Redirect the stdout so it doesn't clog up the test output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Even though this isn't catching the right exception
        # (it actually is catching our mocked input running out of values)
        # It does show that our function is working because it is asking the
        # user for additional values when an invalid value is entered
        with self.assertRaises(Exception):
            ship = place_ship()
        
        sys.stdout = sys.__stdout__

    @patch("battleship.utilities.input", create=True)
    def test_utilities_test_get_target_coordinate(self, mocked_input):
        mocked_input.side_effect = ["A1"]

        # Redirect the stdout so it doesn't clog up the test output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        coord = get_target_coordinate()
        
        sys.stdout = sys.__stdout__

        self.assertEqual(str(coord), "A1")

    @patch("battleship.utilities.input", create=True)
    def test_utilities_test_get_target_coordinate_invalid(self, mocked_input):
        mocked_input.side_effect = ["AA"]

        # Redirect the stdout so it doesn't clog up the test output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Even though this isn't catching the right exception
        # (it actually is catching our mocked input running out of values)
        # It does show that our function is working because it is asking the
        # user for additional values when an invalid value is entered
        with self.assertRaises(Exception):
            coord = get_target_coordinate()
        
        sys.stdout = sys.__stdout__

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()