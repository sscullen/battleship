# Battleship Game

## Dependencies

* python 3.7
* python packages tabulate, coverage

## Install 

```
pip install -r requirements.txt
```

## Run Tests

```
python -m unittest discover
```

## Run Code Coverage Check

```
coverage run -m unittest discover
```

View results:

```
coverage report
```

## Playing the Game

Launch the game with `python game.py` from your favorite terminal application.

The game is played with 2 players, with an 8 x 8 board. 

Each player places a single ship of length 3, using the coordinate system LETTERNUMBER, for example A7, or B3.

```
+----+-----+-----+-----+-----+-----+-----+-----+-----+
|    | A   | B   | C   | D   | E   | F   | G   | H   |
+====+=====+=====+=====+=====+=====+=====+=====+=====+
|  1 |     |     |     |     |     |     |     |     |
+----+-----+-----+-----+-----+-----+-----+-----+-----+
|  2 |     |     |     |     |     |     |     |     |
+----+-----+-----+-----+-----+-----+-----+-----+-----+
|  3 |     |     | H   |     |     |     |     |     |
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
+----+-----+-----+-----+-----+-----+-----+-----+-----+
```
So the "H" above would be at C3.

Once the players place their ships, they take turns targeting each others ship.

The first player to destroy their opponent's ship by hitting all three sections of the ship wins.

