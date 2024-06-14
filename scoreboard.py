from turtle import Turtle
import winsound

# Constants for font properties
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle superclass
        self.hideturtle()  # Hide the turtle cursor
        self.penup()  # Lift the pen to prevent drawing lines
        self.level = 1  # Initialize the current level
        self.score = 0  # Initialize the current score
        self.high_score = 0  # Initialize the high score
        self.highest_level = 0  # Initialize the highest level
        with open("data.txt") as data:
            data.read()  # Read data from a file (not used effectively here, can be improved)
        self.goto(x=-280, y=260)  # Position the scoreboard
        self.update_scoreboard()  # Update the scoreboard with initial values

    def update_scoreboard(self):
        """
        Clears the previous scoreboard and writes the current level and score.
        """
        self.clear()
        self.write(f"Level: {self.level} Score: {self.score}", align="left", font=FONT)

    def increase_level(self):
        """
        Increases the current level by 1, updates the scoreboard, and plays a sound effect.
        """
        self.level += 1
        self.update_scoreboard()
        winsound.PlaySound("level_up.wav", winsound.SND_ASYNC)

    def increase_score(self):
        """
        Increases the current score by 1, updates the scoreboard, and plays a sound effect.
        """
        self.score += 1
        self.update_scoreboard()
        winsound.PlaySound("coin_collected.wav", winsound.SND_ASYNC)

    def game_over(self):
        """
        Displays "GAME OVER" at the center of the screen and plays a game over sound effect.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
        winsound.PlaySound("game_end.wav", winsound.SND_ASYNC)

    def reset(self):
        """
        Resets the game state:
        - Updates the high score and highest level if necessary.
        - Writes the updated high score and highest level to a file.
        - Resets the current score and level to zero and one respectively.
        - Updates the scoreboard to reflect the reset scores.
        """
        # Check if both the current score and level are higher than the recorded high score and highest level
        if self.score > self.high_score and self.level > self.highest_level:
            self.high_score = self.score
            self.highest_level = self.level
        # Check if only the current score is higher than the recorded high score
        elif self.score > self.high_score:
            self.high_score = self.score
        # Check if only the current level is higher than the recorded highest level
        elif self.level > self.highest_level:
            self.highest_level = self.level

        # Write the updated high score and highest level to the file
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}, {self.highest_level}")

        # Reset the current score and level
        self.score = 0
        self.level = 1

        # Update the scoreboard to reflect the reset scores
        self.update_scoreboard()
