""" player.py

Basic class to hold the player's board, ships, and any other player data.

Could be extended in the future to persist player scores and other info.

"""

class Player:
    def __init__(self, board):

        self.board = board
        self.ships = []
    
    def add_ship(self, ship):

        self.ships.append(ship)