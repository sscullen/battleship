""" battleship_game.py

This is a basic implementation of the Battleship boardgame. There are 
2 players, each with 1 ship. Players place their ships using coordinate tuples 
on a 8 x 8 grid (A-H x 1-8). The ships are 3 spaces long, so a valid placement 
would be (B2,D2). Once the ships are placed, players take turns shooting at 
coordinates. Once a player destroys the enemy ship, they win!

Structure of the objects involved. 

Player class
    holds the Board for that player
    additional metadata about the player
Board class
    keeps track of the hits and misses for each player
Ship class
    keeps track of the location of the ships for each player
    logic for hit or miss
    logic for destroyed check

Shaun Cullen, 2020-10-21

"""

from board import Board


if __name__ == "__main__":
    print("""
  ____       _______ _______ _      ______  _____ _    _ _____ _____  
 |  _ \   /\|__   __|__   __| |    |  ____|/ ____| |  | |_   _|  __ \ 
 | |_) | /  \  | |     | |  | |    | |__  | (___ | |__| | | | | |__) |
 |  _ < / /\ \ | |     | |  | |    |  __|  \___ \|  __  | | | |  ___/ 
 | |_) / ____ \| |     | |  | |____| |____ ____) | |  | |_| |_| |     
 |____/_/    \_\_|     |_|  |______|______|_____/|_|  |_|_____|_|     
                                                                      """)

    print("""
Welcome! 
This is a 2 player game. Each player will place one ship.
The length of the ship is 3. After the ships are placed, you will 
take turns shooting. The first player to destroy the enemy ship wins!""")

    print("The battlefield looks like this:")

    board = Board()

    print(board)

    print("""
Place your ship by selecting coordinates that are 3 horizontal or 3 vertical 
spaces apart. Coordinates are in the form A2 or D7. 

So a valid ship placement would be A7, C7 or E1, E4.""")

    print("Player 1, place your ship!")
    coord_1 = input("Ship coordinate 1: ")