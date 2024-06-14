from turtle import Turtle
import random as r

# Constants for point properties
POINT_COLOR = "black"
POINT_SHAPE = "circle"
POINT_SIZE = 0.75


class PointManager:
    all_points = None

    def __init__(self, player):
        self.all_points = []  # List to store all point instances
        self.player = player  # Reference to the player object to access its position

    def create_point(self):
        # Randomly decide when to create a new point (approximately 1 in 30 chance)
        if r.randint(1, 30) == 1:
            # Create a new point with specified shape and size
            new_point = Turtle(shape=POINT_SHAPE)
            new_point.shapesize(stretch_wid=POINT_SIZE, stretch_len=POINT_SIZE)
            new_point.penup()
            new_point.color(POINT_COLOR)

            # Ensure the point is not created below the player's current y-coordinate
            while True:
                random_x = r.randint(-280, 280)
                random_y = r.randint(self.player.ycor(), 280)
                if random_y > self.player.ycor():
                    break

            # Place the new point at the calculated random position
            new_point.goto(random_x, random_y)
            # Add the new point to the list of points
            self.all_points.append(new_point)

    def collect_point(self, point):
        # Hide the point and remove it from the list of points
        point.hideturtle()
        if point in self.all_points:
            self.all_points.remove(point)
