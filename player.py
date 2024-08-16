# PLAYER FILE ==> The file that contains all the attr's and md's of the player.
# Imports of all necessary files

# From the public python module turtle imported the Class Turtle
from turtle import Turtle

# Variable that holds the starting position x-y coordinates
STARTING_POSITION = (0, -280)
# Variable that holds the amount of pixels jumped each move
MOVE_DISTANCE = 10
# Variable that holds the y-coordinates of the finish line
FINISH_LINE_Y = 280


# Class "Player" declaration statement
class Player(Turtle):

    # Creating the initializer method
    def __init__(self):
        # super class inheritance method to inherit all methods of the turtle class
        super().__init__()
        # self. statements to create the player
        self.shape('turtle')
        self.color('green')
        self.lt(90)
        self.pu()

    # The set function will set the starting position as the home and will make the player go there every time they hit
    # the finish line
    def set(self):
        self.goto(STARTING_POSITION)

    # The forwards function moves the player by the move distance amount
    def forwards(self):
        self.fd(MOVE_DISTANCE)

    # The is at finish line method checks if the player has reached the other side.
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
