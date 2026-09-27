# 🧠 Python Knowledge Quiz

A simple and interactive desktop quiz application built using Python and Tkinter. This project tests programming knowledge through multiple-choice questions, provides instant feedback, and displays the final score with accuracy.

## 📌 Project Description

Python Knowledge Quiz is a GUI-based quiz application designed to help users practice basic programming concepts in an interactive way.

The application presents multiple-choice questions, allows users to select answers, checks their responses, and calculates their final score. Users can restart the quiz and attempt the questions again.

## ✨ Features

* User-friendly graphical interface.
* Multiple-choice questions with four options.
* Instant feedback for correct and incorrect answers.
* Displays the correct answer when a response is incorrect.
* Question progress counter.
* Automatic score calculation.
* Accuracy percentage display.
* Performance-based feedback.
* Restart quiz functionality.
* Warning message when no option is selected.
* Dark-themed interface.

## 🛠️ Technologies Used

* **Python** – Core programming language.
* **Tkinter** – GUI development.
* **Messagebox** – Displays warnings and quiz results.
* **Object-Oriented Programming** – Uses classes and methods.
* **Lists and Dictionaries** – Stores questions, options, and answers.

## 📂 Project Structure

```text
Python-Knowledge-Quiz/
│
├── quiz_app.py
└── README.md
```

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Tkinter is included with most standard Python installations.

### Step 2: Run the program

Open the terminal in the project folder and execute:

```bash
python quiz_app.py
```

The quiz application window will open.

## 🎮 How to Play

1. Read the question displayed on the screen.
2. Select one of the four available options.
3. Click **Submit Answer** to check your response.
4. View the feedback and correct answer if you answered incorrectly.
5. Click **Next Question** to continue.
6. After answering all questions, view your score and accuracy.
7. Choose whether to restart the quiz or exit.

## 📚 Topics Covered

The current question bank includes:

| Topic                 | Example               |
| --------------------- | --------------------- |
| Programming languages | JavaScript            |
| Python functions      | `def` keyword         |
| Data structures       | Queue and FIFO        |
| Python operations     | String multiplication |
| Python syntax         | Single-line comments  |

## 🧩 Program Structure

| Function / Method | Purpose                                              |
| ----------------- | ---------------------------------------------------- |
| `QuizApp`         | Main class that manages the quiz application.        |
| `setup_ui()`      | Creates the quiz interface and buttons.              |
| `load_question()` | Displays the current question and options.           |
| `check_answer()`  | Validates the selected answer and updates the score. |
| `next_question()` | Moves to the next question.                          |
| `show_results()`  | Displays the final score and accuracy.               |
| `restart_quiz()`  | Resets the quiz for another attempt.                 |

## 🧮 Score Calculation

The application calculates the percentage of correct answers using:

```python
percentage = round((score / total) * 100)
```

Performance feedback is based on the final accuracy:

* 80% or above: Outstanding performance.
* 50% to 79%: Good effort.
* Below 50%: Encouragement to review and practice.

## 🧠 Concepts Learned

Through this project, I practiced:

* Python classes, objects, and methods.
* Tkinter widgets such as Label, Button, Frame, and Radiobutton.
* Event handling and callback functions.
* Lists and dictionaries.
* Conditional statements and loops.
* String formatting and percentage calculations.
* GUI state management.
* Message boxes and user interaction.

## 🚀 Future Improvements

* Add more questions and difficulty levels.
* Include a timer for each question.
* Randomize question and answer order.
* Add a leaderboard and high-score tracking.
* Add different quiz categories such as Python, C++, DBMS, and DSA.
* Store scores using a file or database.
* Add a review screen showing all incorrect answers.

## 👨‍💻 Author

**JOY ELISHA**

Python Journey – Learning Python through practical projects.

---

⭐ If you like this project, consider giving the repository a star!
