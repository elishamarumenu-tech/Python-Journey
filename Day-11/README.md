# 🐢 Python Turtle Race

A fun and interactive turtle racing game built using Python's built-in `turtle` graphics module. Players predict which colored turtle will win the race, and six turtles compete with randomly generated movement speeds.

## 📌 Project Description

Python Turtle Race is a graphical racing game where six colorful turtles race toward a finish line. The player selects a turtle color before the race begins. Each turtle moves a random distance, making every race different.

At the end of the race, the program displays the winning turtle and tells the player whether their prediction was correct.

## ✨ Features

* Six colorful turtle racers.
* Interactive betting using a popup dialog.
* Random movement for each turtle.
* Graphical race track with a finish line.
* Automatic winner detection.
* Displays win or lose messages.
* Dark-themed racing screen.
* Click the screen to close the game.

## 🛠️ Technologies Used

* **Python** – Programming language.
* **Turtle** – Graphics and animation.
* **Random** – Generates random movement distances.

## 📂 Project Structure

```text
Python-Turtle-Race/
│
├── turtle_race.py
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

The `turtle` and `random` modules are included with standard Python installations.

### 2. Run the program

Open the terminal in the project folder and execute:

```bash
python turtle_race.py
```

A race window will open.

### 3. Play the game

1. Enter your predicted winning turtle color in the popup.
2. Watch all six turtles race toward the finish line.
3. The first turtle to cross the finish line wins.
4. Check whether your selected color matches the winner.
5. Click the screen to close the game.

## 🎮 Available Turtle Colors

| Turtle | Color  |
| ------ | ------ |
| 1      | Red    |
| 2      | Orange |
| 3      | Yellow |
| 4      | Green  |
| 5      | Blue   |
| 6      | Purple |

## 🧠 Concepts Learned

This project helped me practice:

* Python functions and modular programming.
* Lists and list indexing.
* For loops and while loops.
* Conditional statements.
* Random number generation using `random.randint()`.
* Object-oriented programming with Turtle objects.
* User input using graphical popup dialogs.
* Turtle positioning and screen coordinates.
* Collision and finish-line detection.
* Basic animation and graphical user interfaces.

## 🔍 How the Race Works

1. The `setup_race_track()` function creates the screen and draws the finish line.
2. Six turtle objects are created and positioned at the starting line.
3. The player selects a color using a popup dialog.
4. Each turtle moves forward by a random distance between 1 and 10 pixels.
5. The race continues until a turtle crosses the finish line.
6. The program displays the winner and the player's result.

## 🚀 Future Improvements

* Add a scoreboard to track wins and losses.
* Allow players to restart the race without closing the window.
* Add background music and racing sound effects.
* Display a countdown before the race starts.
* Add more racers and customizable race tracks.
* Improve the betting system with input validation.

## 👨‍💻 Author

**JOY ELISHA**

Python Journey – Learning Python through practical projects.

---

⭐ If you like this project, consider giving the repository a star!
