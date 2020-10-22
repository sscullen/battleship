import io
import unittest
import unittest.mock
import sys

from battleship.board import Board
from battleship.coordinate import Coordinate
from battleship.ship import Ship

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.empty_board_string = """
+----+-----+-----+-----+-----+-----+-----+-----+-----+
|    | A   | B   | C   | D   | E   | F   | G   | H   |
+====+=====+=====+=====+=====+=====+=====+=====+=====+
|  1 |     |     |     |     |     |     |     |     |
+----+-----+-----+-----+-----+-----+-----+-----+-----+
|  2 |     |     |     |     |     |     |     |     |
+----+-----+-----+-----+-----+-----+-----+-----+-----+
|  3 |     |     |     |     |     |     |     |     |
+----+-----+-----+-----+-----+-----+-----+-----+-----+
|  4 |     |     |     |     |     |     |     |     |
+----+-----+-----+-----+-----+-----+-----+-----+-----+
|  5 |     |     |     |     |     |     |     |     |
+----+-----+-----+-----+-----+-----+-----+-----+-----+
|  6 |     |     |     |     |     |     |     |     |
+----+-----+-----+-----+-----+-----+-----+-----+-----+
|  7 |     |     |     |     |     |     |     |     |
+----+-----+-----+-----+-----+-----+-----+-----+-----+
|  8 |     |     |     |     |     |     |     |     |
+----+-----+-----+-----+-----+-----+-----+-----+-----+"""

    def test_board_update_board(self):
        board = Board()
        target_coord = Coordinate("A1")

        board.update_board(target_coord, True)

        self.assertEqual("H", board.board_state[target_coord.row_idx][target_coord.col_idx])

    def test_board_update_board_miss(self):
        board = Board()
        target_coord = Coordinate("A1")

        board.update_board(target_coord, False)

        self.assertEqual("M", board.board_state[target_coord.row_idx][target_coord.col_idx])

    def test_board_print(self):
        board = Board()
    
        # Redirect stdout to enable testing the board visualization
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print(board)
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue().strip(), self.empty_board_string.strip())

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()