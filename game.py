import random

class Board(object):

    """Represents a tic tac toe board."""

    def __init__(self):

        """Initialize an empty board with spaces numbered 1-9."""

        # This holds the pieces. It starts with empty spaces.
        self.gameboard = { 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ",  7: " ", 8: " ", 9: " " }

        # This is a template that gets rendered with the actual positions
        self.template = """
-------------
| %s | %s | %s |
-------------
| %s | %s | %s |
-------------
| %s | %s | %s |
-------------""" 

    def __repr__(self):
        
        """A string representation of the board."""

        output = "This is the game board object..."
        return output

    def render_template(self):

        """Renders the board to the screen with the current positions."""

        # Holds values of current positions
        board = []

        # Append the current positions onto the board list
        for key, value in self.gameboard.iteritems():
            board.append(value)

        # Print the rendered template
        print self.template % (board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8], board[9])

    def print_help(self):
        
        """Draw the position numbers to help the player."""

        # Print out the keys used to place a piece on the board
        for key in self.gameboard:
            if key % 3 != 0:
                print key,
            else:
                print key

#class Piece(object):

    #"""Represents an X or O on the board along with a position. Probably don't need this."""

    #def __init__(self, shape, x, y):
        #self.shape = shape
        #self.x = x
        #self.y = y

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

    def ask_for_move(self):

        """Get player's move."""
        player_move = raw_input("Please enter a position number between 1-9: ")

        try:
            if int(player_move) not in range(1, 10):
                print "Invalid choice..."
                self.ask_for_move()
        except:
            print "Please enter a number... Try again."
            self.ask_for_move()

class Computer(Player):

    """Extends the Player class to represent a computer with AI."""

    def choose_move(self):
        pass

class Logger(object):

    """This will keep track of every game."""

    pass


