# 🎮 Rock Paper Scissors Game

A simple **Rock Paper Scissors game built with Python** using functions, user input, random computer choices, and conditional logic.

This version improves the previous project by organizing the program into separate functions, making the code easier to understand, maintain, and reuse.

## 📌 Description

In this game:

1. The player chooses Rock, Paper, or Scissors.
2. The computer randomly selects a choice.
3. The choices are displayed using emojis.
4. The winner is determined using the game rules.
5. The player can continue playing or exit the game.

## 🕹️ Game Rules

| Player Choice      | Computer Choice | Result   |
| ------------------ | --------------- | -------- |
| Rock 🪨            | Scissors ✂️     | You Win  |
| Scissors ✂️        | Paper 📄        | You Win  |
| Paper 📄           | Rock 🪨         | You Win  |
| Same Choice        | Same Choice     | Tie      |
| Other combinations | —               | You Lose |

## 🧩 Functions Used

### `get_user_choice()`

Gets the player's choice and validates the input.

```python
def get_user_choice():
```

If the user enters an invalid choice, the program asks again.

### `display_choices()`

Displays the choices made by the player and computer.

```python
def display_choices(user_choice, computer_choice):
```

### `determine_winner()`

Compares the two choices and determines whether the result is:

* Tie
* You Win
* You Lose

```python
def determine_winner(user_choice, computer_choice):
```

### `play_game()`

Controls the main game loop and allows the player to continue playing.

```python
def play_game():
```

## 🛠️ Technologies Used

* **Python**
* `random` module
* Functions
* Dictionary
* Tuple
* `while` loop
* `if-elif-else`
* `random.choice()`
* User input
* String methods

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python rock_paper_scissors.py
```

## 💻 Example Output

```text
Rock, paper, or scissors? (r/p/s): r

You chose ♣️
Computer chose ✂️

You win!

Continue? (y/n): y

Rock, paper, or scissors? (r/p/s): p

You chose ✂️
Computer chose ✂️

Tie!

Continue? (y/n): n
```

## ❌ Invalid Input

If the user enters an invalid choice:

```text
Rock, paper, or scissors? (r/p/s): x
Invalid choice!

Rock, paper, or scissors? (r/p/s):
```

The program continues asking until a valid choice is entered.

## 📚 What I Learned

Through this project, I practiced:

* Creating and calling functions.
* Passing arguments to functions.
* Returning values from functions.
* Using dictionaries.
* Using tuples.
* Generating random choices.
* Validating user input.
* Using loops.
* Applying conditional statements.
* Breaking a large program into smaller functions.
* Building a reusable and organized Python program.

## 🚀 Future Improvements

Possible improvements include:

* Add a score counter.
* Track wins, losses, and ties.
* Add multiple-round gameplay.
* Add a best-of-3 or best-of-5 mode.
* Add a restart option.
* Improve the user interface.
* Add more detailed game statistics.

## 👨‍💻 Author

**JOY ELISHA**

### 🐍 Python Journey

This project is part of my **Python Journey**, where I am learning Python concepts by building practical projects and improving my programming skills.
