import random

class Board(object):

    """Represents a tic tac toe board."""

    def __init__(self):

        """Initialize an empty board with spaces numbered 1-9."""

        # This holds the pieces
        self.gameboard = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]

        # This is just the layout to display as keyboard shortcuts
        self.layout = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]

        # This is a template that gets rendered with the actual positions
        self.template = """
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------""" 

    def __repr__(self):
        
        """A string representation of the board."""

        output = "This is the game board object..."
        return output

    def render_template(self):
        pass

    def draw_help(self):
        
        """Draw the position numbers to help the player."""

        for row in self.layout:
            print ""
            for space in row:
                print space,

class Piece(object):

    """Represents an X or O on the board along with a position."""

    def __init__(self, shape, x, y):
        self.shape = shape
        self.x = x
        self.y = y

class Player(object):

    """Represents a player, either real or computer."""

    def __init__(self):
        pass

    def __repr__(self):

        """A string representation of a Player object."""

        output = "This is a Player object..."
        return output

    def move(self, position):

        """Place a piece on the game board."""

        if position not in range(1,10):
            print "Please choose a number between 1 and 9."

class GameMaster(object):

    """Represents the game administrator who runs the game."""

    def __init__(self):
        pass

class Computer(Player):

    """Extends the Player class to represent a computer with AI."""

class Log(object):
    pass


