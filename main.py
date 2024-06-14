"""
# TODO 1: Move the turtle with key press
# TODO 2: Create and move the cars
# TODO 3: Detect collision with car
# TODO 4: Detect when turtle reaches the other side
# TODO 5: Create a scoreboard
"""
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from point_manager import PointManager


def screen_setup(scrn, plr):
    """
    Set up the screen with given dimensions and title.
    Register key listeners for player movement.

    Args:
        scrn (Screen): The turtle Screen object.
        plr (Player): The player object to register key presses for.
    """
    scrn.setup(width=600, height=600)
    scrn.tracer(0)  # Turn off animation to manually update screen
    scrn.title("Turtle Crossing")
    scrn.listen()
    scrn.onkey(plr.move_up, "Up")
    scrn.onkey(plr.move_down, "Down")
    scrn.onkey(plr.move_left, "Left")
    scrn.onkey(plr.move_right, "Right")


if __name__ == '__main__':
    # Initialize objects of all classes
    screen = Screen()
    player = Player()
    scoreboard = Scoreboard()
    car_manager = CarManager()
    point_manager = PointManager(player)  # Pass player object to PointManager

    screen_setup(screen, player)  # Set up the screen and key bindings

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)  # Delay to control game speed
        screen.update()  # Update the screen manually

        car_manager.create_car()  # Create new cars at random intervals
        car_manager.move_cars()  # Move all cars to the left

        point_manager.create_point()  # Create points randomly for player to collect

        # Detect collision with cars
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False  # End game if player collides with a car
                scoreboard.game_over()  # Display game over message

        # Detect if player has crossed to the other side
        if player.at_finish_line():
            player.go_to_start()  # Reset player position to starting point
            car_manager.level_up()  # Increase car speed for the next level
            scoreboard.increase_level()  # Increase level on the scoreboard

        # Check if player has collected any points
        if isinstance(point_manager.all_points, list):
            for point in point_manager.all_points:
                if player.distance(point) < 20:
                    point_manager.collect_point(point)  # Remove collected point
                    scoreboard.increase_score()  # Increase score on the scoreboard

    screen.exitonclick()  # Close the screen when clicked
