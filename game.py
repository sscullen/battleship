""" game.py

This is a basic implementation of the Battleship boardgame. There are 
2 players, each with 1 ship. Players place their ships using coordinate tuples 
on a 8 x 8 grid (A-H x 1-8). The ships are 3 spaces long, so a valid placement 
would be (B2,D2). Once the ships are placed, players take turns shooting at 
coordinates. Once a player destroys the enemy ship, they win!

Structure of the objects involved. 

Player class
    holds the Board for that player
    holds the Ship(s) for that player
    additional metadata about the player
Board class
    keeps track of the hits and misses for each player
Ship class
    keeps track of the location of the ships for each player
    logic for hit or miss
    logic for ship destroyed

Shaun Cullen, 2020-10-21

"""

import os

from battleship.board import Board
from battleship.coordinate import Coordinate
from battleship.player import Player
from battleship.ship import Ship

from battleship.utilities import place_ship, get_target_coordinate

if __name__ == "__main__":
    board_1 = Board()
    board_2 = Board()

    player_1 = Player(board_1)
    player_2 = Player(board_2)

    player_list = [player_1, player_2]
    
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
take turns shooting. The first player to destroy the enemy ship wins!
    """)

    print("The battlefield looks like this:")

    print(board_1)

    print("""
Place your ship by selecting coordinates that are 3 horizontal or 3 vertical 
spaces apart. Coordinates are in the form [letter][number], for example A2 or D7. 

So a valid ship placement would be A7 to C7 or E1 to E3.
    """)

    for idx, player in enumerate(player_list):
        # To clear the screen (to prevent cheating!) os.system("cls") for Windows
        # os.system("clear") on Linux
        print(f"Player {idx + 1}, place your ship!")
        ship = place_ship()
        player.ships.append(ship)
    
    game_over = False
    idx_of_winner = None

    print("The ships are placed! Get ready to fire!")

    while not game_over:
        for idx, player in enumerate(player_list):
            if game_over:
                break

            print(f"Player {idx + 1}, take aim!")
            target_coord = get_target_coordinate()

            # Check for hit or miss
            opposing_player_idx = (idx + 1) % 2
            opponent = player_list[opposing_player_idx]
            
            for ship in opponent.ships:
                shot_result = ship.check_if_hit(target_coord)

                if shot_result[0]:
                    print("HIT!")
                    player.board.update_board(target_coord, True)
                    if shot_result[1]:
                        print("Ship destroyed!")

                        game_over = True
                        idx_of_winner = idx
                    break
            else:
                print("MISS!")
                player.board.update_board(target_coord, False)
                
            print(player.board)

    print(f"Congratulations Player {idx_of_winner + 1}, you win!")
    print("Please play again soon! Bye!")