# Turtle Crossing

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Rules](#rules)
- [Controls](#controls)
- [Files and Structure](#files-and-structure)
- [Credits](#credits)
- [Contributing](contributing)
- [License](#license)

## Overview
The Turtle Crossing Game is a simple interactive game implemented in Python using the Turtle graphics library. In this game, the player controls a turtle character and navigates it across a busy road while avoiding collisions with moving cars. The objective is to safely cross to the other side of the road while collecting points for a higher score.

## Features

- Player-controlled turtle movement (up, down, left, right).
- Randomly generated cars that move horizontally across the screen.
- Points (objects) randomly appearing for the player to collect.
- Score and level tracking with a scoreboard display.
- Game over detection upon collision with a car.
- Level increases with higher speeds for cars as the game progresses.


## Installation
1. **Clone the Repository:**
```
git clone https://github.com/AmrithNiyogi/turtle-crossing.git
```

2. **Navigate to the project directory:**
```
cd turtle-crossing
```

3. **Install Dependencies:**

    - Ensure you have Python installed on your system.
    - Dependencies like `turtle` and `winsound` are standard with Python installations.


4. Ensure you have Python installed (preferably version 3.6 or above).

## Usage

- Start the Game:
```
python main.py
```

## Rules 

- Navigate the turtle across the road without colliding with any cars.
- Collect points `(displayed as small circles)` for increasing your score.
- Reach the top of the screen to advance to the next level.
- Game Over:
  - The game ends if the turtle collides with any car.
  - The scoreboard will display the final score and highest level achieved.
  - Click anywhere on the game screen to close the window and exit.

## Controls

- **Up Arrow**: Move up
- **Down Arrow**: Move down
- **Left Arrow**: Move left
- **Right Arrow**: Move right


## Files and Structure

- **`main.py`:** Main entry point of the game, initializes game components and manages game loop.
- **`player.py`:** Defines the `Player` class for controlling the turtle.
- **`car_manager.py`:** Manages cars, including creation, movement, and speed control.
- **`scoreboard.py`:** Handles score and level tracking, displays the scoreboard, and manages game over conditions.
- **`point_manager.py`:** Manages the creation and collection of points for increasing score.


## Credits
- This game is inspired by classic arcade-style crossing games.

- Sound effects obtained from `pixbay.com` and `mixit.co`.
  - Original audio name: `Cute Level Up`
  - Original audio name: `mixkit-cartoon-whistle-game-over-606`


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
