# MAIN FILE ==> Connects and triggers all other modules
# Import all necessary modules

# Python public module: Time ==> allows for using any method related to time, duration, counting, or dates
import time
# Python public module: Turtle ==> Module that contains methods that can draw, move, write, etc; on a screen
import turtle

# Private, personal module imported from the car_manager file ==> Deals with all the properties of the created cars
from car_manager import CarManager
# Private, personal module imported from the player file ==> Deals with all the movements and properties of the player
from player import Player, STARTING_POSITION
# Private, personal module imported from the scoretext file ==> Deals with all the text and gameover stuff
from scoretext import Scoreboard
# Private, personal module imported from teh background file ==> Creates the road
from background import white_line, yellow_line

# Set up of Turtle Screen Environment
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
yellow_line()
white_line(75)
white_line(150)
white_line(225)
white_line(-75)
white_line(-150)
white_line(-225)
# Set up of the scoreboard and game over sequence, triggering the Scoreboard class to create an object: board
board = Scoreboard()


# Set up of user object, and user controls
user = Player()
user.set()
# Prompts user to choose a key for moving the player up
control = screen.textinput("This game uses only one key to move\nThe only direction is forwards", "Press a key in the "
                                                                                                  "bar to choose your direction key.")
# Function from turtle module that allows for motion controls
screen.listen()
screen.onkey(fun=user.forwards, key=control)

# Set up of cars in the road, creating object "cars" with CarManager class
cars = CarManager()

# game_is_on ==> A boolean value used to check if the game has ended or not, made to end the while loop that runs
#                the game
game_is_on = True

# Method from the Scoreboard class to create the scoreboard text and score
board.renew()

# The while loop that connects everything and runs the game
while game_is_on:
    # time.sleep slows down the creation, motion, and controls of the whole environment
    time.sleep(0.1)
    # screen.update ==> Updates the screen every 0.1 (or specified sec amt in time.sleep) seconds
    screen.update()
    # Creates the cars.
    cars.create()
    # Moves the cars
    cars.move()

    # Checks for a collision with the turtle and a car, squish!
    for car in cars.all_cars:
        # if the distance between the car and the player is less than 20 pixels, the game ends and initiates the
        # game_over sequence
        if car.distance(user) < 20:
            game_is_on = False
            board.game_over()
    # Checks if the user has crossed the road
    if user.is_at_finish_line():
        # user.goto ==> Sends the player (turtle) back to the start
        user.goto(STARTING_POSITION)
        # Increases the score amount
        board.num += 1
        # Puts the score amount in the actual text
        board.renew()
        # Speeds up the cars
        cars.level_up()
# main

# Allows the user to end the game by click on the screen without triggering an error
screen.exitonclick()
