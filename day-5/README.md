# 🎮 Rock Paper Scissors Game

A simple **Rock Paper Scissors game built with Python** using functions, constants, dictionaries, random choices, and conditional statements.

This version improves the program structure by defining **ROCK, PAPER, and SCISSORS as constants**, making the code easier to read, maintain, and modify.

## 📌 Description

The game allows the player to compete against the computer.

The program:

1. Asks the player to choose Rock, Paper, or Scissors.
2. Validates the player's input.
3. Randomly generates the computer's choice.
4. Displays both choices using emojis.
5. Determines the winner.
6. Asks whether the player wants to continue.
7. Repeats until the player chooses `n`.

## 🕹️ Game Rules

| Player             | Computer    | Result   |
| ------------------ | ----------- | -------- |
| Rock 🪨            | Scissors ✂️ | You Win  |
| Scissors ✂️        | Paper 📄    | You Win  |
| Paper 📄           | Rock 🪨     | You Win  |
| Same Choice        | Same Choice | Tie      |
| Other combinations | —           | You Lose |

## 🧩 Program Structure

### 1. Constants

The game choices are stored as constants:

```python
ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
```

Using constants makes the game logic easier to understand.

### 2. Dictionary

The `emojis` dictionary connects each choice with an emoji:

```python
emojis = {
    ROCK: '♣️',
    SCISSORS: '🗑️',
    PAPER: '✂️'
}
```

The available choices are then created automatically:

```python
choices = tuple(emojis.keys())
```

### 3. `get_user_choice()`

This function asks the player for a choice and validates the input.

```python
def get_user_choice():
```

If the user enters an invalid option, the program displays:

```text
Invalid choice!
```

and asks again.

### 4. `display_choices()`

This function displays the choices made by the player and computer.

```python
def display_choices(user_choice, computer_choice):
```

### 5. `determine_winner()`

This function compares the player and computer choices and determines the result.

Possible results:

* **Tie!**
* **You win!**
* **You lose**

```python
def determine_winner(user_choice, computer_choice):
```

### 6. `play_game()`

This is the main function that controls the game.

```python
def play_game():
```

It repeatedly:

* Gets the user's choice.
* Generates the computer's choice.
* Displays both choices.
* Determines the winner.
* Asks whether to continue.

## 🛠️ Technologies Used

* **Python**
* `random` module
* Functions
* Constants
* Dictionary
* Tuple
* `while` loop
* `if-elif-else`
* `random.choice()`
* User input

## ▶️ How to Run

Make sure Python is installed.

Run the program using:

```bash
python rock_paper_scissors.py
```

## 💻 Example Output

```text
Rock, paper, or scissors? (r/p/s): r

You chose ♣️
Computer chose 🗑️

You win!

Continue? (y/n): y

Rock, paper, or scissors? (r/p/s): p

You chose ✂️
Computer chose ✂️

Tie!

Continue? (y/n): n
```

## ❌ Invalid Input

Example:

```text
Rock, paper, or scissors? (r/p/s): x
Invalid choice!

Rock, paper, or scissors? (r/p/s):
```

The program continues until the player enters a valid choice.

## 📚 What I Learned

Through this project, I practiced:

* Creating constants.
* Using dictionaries.
* Creating tuples from dictionary keys.
* Creating and calling functions.
* Passing arguments to functions.
* Returning values from functions.
* Using `random.choice()`.
* Validating user input.
* Using `while` loops.
* Using conditional statements.
* Organizing a program into separate functions.
* Building an interactive command-line game.

## 🚀 Future Improvements

Possible improvements:

* Add a score counter.
* Track wins, losses, and ties.
* Add multiple rounds.
* Add Best of 3 / Best of 5 mode.
* Add game statistics.
* Add a restart option.
* Improve the user interface.

## 👨‍💻 Author

**JOY ELISHA**

### 🐍 Python Journey

This project is part of my **Python Journey**, where I am learning Python by building practical projects and improving my programming skills.
