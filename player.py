from turtle import Turtle

# Constants for starting position, movement distance, and finish line
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        """
        Initialize the Player object.
        """
        super().__init__()  # Initialize the Turtle superclass
        self.penup()  # Lift the pen to prevent drawing lines
        self.color("black")  # Set the turtle's color to black
        self.shape("turtle")  # Set the turtle's shape to 'turtle'
        self.go_to_start()  # Position the turtle at the starting position
        self.setheading(90)  # Set the turtle's initial heading to north (up)

    def move_up(self):
        """
        Move the turtle forward by MOVE_DISTANCE when the 'Up' arrow key is pressed.
        """
        self.forward(MOVE_DISTANCE)

    def at_finish_line(self):
        """
        Check if the turtle has crossed the finish line (y-coordinate greater than FINISH_LINE_Y).
        Returns:
            bool: True if turtle's y-coordinate is greater than FINISH_LINE_Y, False otherwise.
        """
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def move_down(self):
        """
        Move the turtle backward by MOVE_DISTANCE when the 'Down' arrow key is pressed.
        """
        self.backward(MOVE_DISTANCE)

    def move_left(self):
        """
        Temporarily set heading to west (left) and move left by MOVE_DISTANCE.
        """
        self.setheading(180)  # Set heading to west (left)
        self.forward(MOVE_DISTANCE)  # Move the turtle forward by MOVE_DISTANCE
        self.setheading(90)  # Restore heading to north (up) after moving left

    def move_right(self):
        """
        Temporarily set heading to east (right) and move right by MOVE_DISTANCE.
        """
        self.setheading(0)  # Set heading to east (right)
        self.forward(MOVE_DISTANCE)  # Move the turtle forward by MOVE_DISTANCE
        self.setheading(90)  # Restore heading to north (up) after moving right

    def go_to_start(self):
        """
        Move the turtle to the starting position defined by STARTING_POSITION.
        """
        self.goto(STARTING_POSITION)
