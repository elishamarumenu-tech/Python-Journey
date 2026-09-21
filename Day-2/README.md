# 🔢 Number Guessing Game

A simple **Number Guessing Game built with Python**. The computer randomly selects a number between **1 and 100**, and the player has to guess it.

The program provides hints after each guess to help the player find the correct number.

## 📌 Description

The game works by:

* Generating a random number between 1 and 100.
* Asking the user to enter a guess.
* Checking whether the guess is too low or too high.
* Displaying a congratulations message when the correct number is guessed.
* Handling invalid input using exception handling.
* Continuing until the correct number is found.

## 🛠️ Technologies Used

* **Python**
* `random` module
* `while` loop         
* `try-except`
* `if-elif-else`
* `input()`
* `random.randint()`
* Type conversion using `int()`

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python number_guessing_game.py
```

## 💻 Example Output

```text
Guess the number between 1 and 100: 40
Too low

Guess the number between 1 and 100: 75
Too high

Guess the number between 1 and 100: 62
Congratulations! You guessed the number
```

### Invalid Input Example

```text
Guess the number between 1 and 100: abc
Please enter a valid number
```

## 📚 What I Learned

Through this project, I practiced:

* Generating random numbers using Python.
* Taking input from the user.
* Using `while` loops.
* Using conditional statements.
* Handling invalid input with `try-except`.
* Converting strings into integers.
* Building an interactive command-line game.

## 🚀 Future Improvements

Possible improvements:

* Add a maximum number of attempts.
* Display the number of attempts taken.
* Add difficulty levels.
* Give hints such as "Very close!".
* Allow the player to restart the game.
* Add a score system.

## 👨‍💻 Author

**JOY ELISHA**

### 🐍 Python Journey

This project is part of my **Python Journey**, where I am learning Python concepts by building small practical projects.
