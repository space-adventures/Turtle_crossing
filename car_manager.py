# CAR MANAGING FILE ==> This file will deal with anything related to the cars, creating them, moving them,
# and speeding them up
# Imports of all necessary files

# Public python module that deals with randomizing numbers or letters
import random
# From the public python module turtle, imported the class Turtle that holds all the objects attributes
from turtle import Turtle

# List COLORS ==> A list that contains all the possible colors of the cars in the string format
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE ==> A variable that contains the speed amount of the level 0 cars
STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT ==> Contains the speed amount that all cars have to increment from every new level
MOVE_INCREMENT = 10


# These variables were all caps because when using variables in a class, you must capitalize all of it to differentiate
# these variables from the ones not used in classes.

# Class "CarManager" declaration statement
class CarManager:

    # Defines the initializer method
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # Method that creates the actual car
    def create(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(1, 2)
            new_car.pu()
            new_car.color(random.choice(COLORS))
            new_car.goto(260, random.randint(-250, 250))
            self.all_cars.append(new_car)

    # Method that moves the car
    def move(self):
        for car in self.all_cars:
            car.bk(self.car_speed)

    # Method that speeds up the car every new level
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
