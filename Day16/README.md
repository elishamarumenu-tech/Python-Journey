# 🎓 Student Grade Calculator

A simple and interactive desktop application built using **Python and Tkinter**. It allows users to enter multiple student scores, calculate the average percentage, and determine the final letter grade automatically.

## 📌 Project Description

The Student Grade Calculator is a GUI-based application designed to make score calculation easy and efficient.

Users can enter multiple scores between 0 and 100. The application stores the entered scores, calculates their average, and assigns a letter grade based on predefined grading criteria.

It also provides options to clear all recorded scores and displays results through interactive message boxes.

## ✨ Features

- User-friendly graphical interface.
- Enter multiple student scores.
- Accepts scores between 0 and 100.
- Validates numeric input.
- Displays all recorded scores.
- Calculates the average score automatically.
- Assigns letter grades based on average percentage.
- Displays total number of recorded scores.
- Clear all scores with confirmation.
- Press Enter to add a score.
- Dark-themed interface.
- Warning and error messages for invalid inputs.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Tkinter | Graphical user interface |
| Messagebox | Displays results, warnings, and errors |
| OOP | Organizes the application using a class |
| Lists | Stores multiple student scores |

## 📂 Project Structure

```text
Student-Grade-Calculator/
│
├── grade_calculator.py
└── README.md
```

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Tkinter is included with most standard Python installations.

### Step 2: Run the application

Open a terminal in the project folder and execute:

```bash
python grade_calculator.py
```

The Student Grade Calculator window will open.

## 🎮 How to Use

1. Enter a score between 0 and 100.
2. Click **Add Score** or press Enter.
3. Repeat to add multiple scores.
4. Click **Calculate Grade** to calculate the average and final grade.
5. View the results in the message box.
6. Click **Clear All** to remove all recorded scores after confirmation.

## 📊 Grading System

The application assigns grades based on the average score.

| Average Score | Grade | Description |
|---|---|---|
| 90–100 | A | Excellent |
| 80–89.99 | B | Good |
| 70–79.99 | C | Satisfactory |
| 60–69.99 | D | Passing |
| Below 60 | F | Needs Improvement |

## 🧮 Average Calculation

The application calculates the average using:

\[
\text{Average} = \frac{\text{Sum of all scores}}{\text{Number of scores}}
\]

**Example:**

Suppose the entered scores are:

- 85
- 90
- 75
- 80

\[
\text{Average} = \frac{85+90+75+80}{4}=82.5
\]

<badge color="success">Final Grade: B (Good)</badge>

## 🧩 Main Functions

| Function | Purpose |
|---|---|
| `setup_ui()` | Creates the graphical interface. |
| `add_score()` | Validates and adds scores to the list. |
| `calculate_grade()` | Calculates the average and assigns a letter grade. |
| `clear_scores()` | Removes all recorded scores after confirmation. |

## 🧠 Concepts Learned

Through this project, I practiced:

- Python classes and objects.
- Object-oriented programming.
- Tkinter GUI development.
- Labels, buttons, frames, and entry widgets.
- Lists and list operations.
- User input validation.
- Type conversion using `float()`.
- Conditional statements (`if`, `elif`, `else`).
- Exception handling using `try-except`.
- Mathematical calculations.
- Event handling and callback functions.
- Message boxes for user interaction.

## 🚀 Future Improvements

- Add individual student names.
- Support subject-wise marks.
- Add weighted grade calculation.
- Display individual subject grades.
- Generate downloadable report cards.
- Save scores using JSON or SQLite.
- Add graphical performance charts.
- Include customizable grading criteria.

## 👨‍💻 Author

**JOY ELISHA**

Python Journey — Learning Python through practical projects.

---

⭐ If you like this project, consider giving the repository a star!