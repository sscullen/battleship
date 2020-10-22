import unittest
from pathlib import Path

TEST_DIR = Path(__file__).absolute().parent

from battleship.board import Board
from battleship.coordinate import Coordinate
from battleship.player import Player
from battleship.ship import Ship

class TestPlayer(unittest.TestCase):
    def setUp(self):
        pass

    def test_player_create_player(self):
        board = Board()
        player = Player(board)

    def test_player_add_ship(self):
        board = Board()
        player = Player(board)

        ship = Ship(Coordinate("A1"), Coordinate("A3"))

        player.add_ship(ship)

        self.assertEqual(str(player.ships[0]), "['A1', 'A2', 'A3']")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()