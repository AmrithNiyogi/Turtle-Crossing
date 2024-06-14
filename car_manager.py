from turtle import Turtle
import random as r

# Constants for car properties and movement
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []  # List to store all car instances
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial speed of cars

    def create_car(self):
        """
        Creates a new car instance with a probability of 1/6 each time this method is called.
        The car is positioned at the right edge of the screen with a random y-coordinate.
        """
        random_chance = r.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")  # Create a new turtle instance for the car
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Adjust the car's shape
            new_car.penup()  # Lift the pen to prevent drawing lines
            new_car.color(r.choice(COLORS))  # Randomly select a color for the car
            random_y = r.randint(-250, 250)  # Randomly position the car along the y-axis
            new_car.goto(300, random_y)  # Position the car at the right edge of the screen
            self.all_cars.append(new_car)  # Add the new car to the list of cars

    def move_cars(self):
        """
        Move each car instance stored in all_cars backwards by the current car_speed.
        """
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """
        Increase the speed of the cars by MOVE_INCREMENT when the player levels up.
        """
        self.car_speed += MOVE_INCREMENT
