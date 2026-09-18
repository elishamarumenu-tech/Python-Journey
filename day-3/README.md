# 🎮 Rock Paper Scissors Game

A simple **Rock Paper Scissors game built with Python** where the player competes against the computer.

The computer randomly selects Rock, Paper, or Scissors, and the program determines the winner based on the game rules.

## 📌 Description

This project is a beginner-friendly Python game that demonstrates:

* Taking user input.
* Generating random choices.
* Using dictionaries.
* Using tuples.
* Applying conditional statements.
* Creating a continuous game loop.
* Validating user input.

## 🕹️ Game Rules

The rules are:

| Player             | Computer    | Result   |
| ------------------ | ----------- | -------- |
| Rock 🪨            | Scissors ✂️ | You Win  |
| Scissors ✂️        | Paper 📄    | You Win  |
| Paper 📄           | Rock 🪨     | You Win  |
| Same Choice        | Same Choice | Tie      |
| Other combinations | —           | You Lose |

## 🛠️ Technologies Used

* **Python**
* `random` module
* Dictionary
* Tuple
* `while` loop
* `if-elif-else`
* `random.choice()`
* User input

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program:

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

If the user enters something other than `r`, `p`, or `s`:

```text
Rock, paper, or scissors? (r/p/s): x
Invalid choice
```

The program asks the user to enter a valid choice again.

## 📚 What I Learned

Through this project, I practiced:

* Importing Python modules.
* Using `random.choice()`.
* Creating and accessing dictionaries.
* Using tuples to store choices.
* Validating user input.
* Using `while` loops.
* Applying logical operators.
* Using `if-elif-else` conditions.
* Building an interactive command-line game.

## 🚀 Future Improvements

Possible improvements include:

* Add a score counter.
* Add multiple rounds.
* Display the final score.
* Add a best-of-3 or best-of-5 mode.
* Improve the emoji representation.
* Add difficulty levels.
* Allow the player to restart automatically.

## 👨‍💻 Author

**JOY ELISHA**

### 🐍 Python Journey

This project is part of my **Python Journey**, where I am learning Python by creating small practical projects and improving my programming skills.
          