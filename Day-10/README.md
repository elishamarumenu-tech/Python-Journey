# 🧮 Python GUI Calculator

A modern **GUI Calculator built with Python and Tkinter** that supports basic arithmetic operations along with square root, square, and percentage calculations.

The calculator provides a simple desktop interface with buttons, keyboard support, error handling, and a dark-themed design.

## 📌 Description

This project is a desktop calculator application developed using **Python's Tkinter library**.

It allows users to perform:

* Addition
* Subtraction
* Multiplication
* Division
* Percentage calculation
* Square calculation
* Square root calculation

The application also supports keyboard shortcuts for faster calculations.

## ✨ Features

* 🖥️ Graphical User Interface
* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* `%` Percentage
* `x²` Square
* `√` Square root
* 🧹 Clear button
* ⌫ Backspace support
* ⌨️ Keyboard input
* ⚠️ Error handling
* 🚫 Division-by-zero detection
* 🎨 Dark-themed interface
* 📱 Fixed-size calculator window

## 🛠️ Technologies Used

* **Python**
* **Tkinter**
* `math` module
* Object-Oriented Programming
* Classes and objects
* Event handling
* Lambda functions
* Exception handling

## 🧩 Program Structure

### `Calculator` Class

The entire calculator is organized inside a `Calculator` class.

```python
class Calculator:
```

This makes the program easier to organize and maintain.

### `__init__()`

The constructor creates the calculator window and initializes:

* Window properties
* Display
* Buttons
* Button layout
* Keyboard bindings

### `update_display()`

Updates the calculator display with the given text.

```python
def update_display(self, text):
```

### `on_button_click()`

Handles button clicks and determines which calculator operation should be performed.

```python
def on_button_click(self, char):
```

### `clear_all()`

Clears the complete calculator expression.

```python
def clear_all(self):
```

### `clear_last()`

Removes the last character from the current expression.

```python
def clear_last(self):
```

### `square_root()`

Calculates the square root of the displayed number.

Example:

```text
√25 = 5
```

The program also prevents square roots of negative numbers.

### `square()`

Calculates the square of a number.

Example:

```text
5² = 25
```

### `percentage()`

Converts a number into its percentage value.

Example:

```text
50% = 0.5
```

### `calculate()`

Evaluates arithmetic expressions and displays the result.

Example:

```text
25 + 10 * 2 = 45
```

The function also handles errors such as division by zero.

## ⌨️ Keyboard Shortcuts

The calculator supports keyboard input.

| Key         | Action                |
| ----------- | --------------------- |
| `0-9`       | Enter numbers         |
| `+`         | Addition              |
| `-`         | Subtraction           |
| `*`         | Multiplication        |
| `/`         | Division              |
| `.`         | Decimal point         |
| `Enter`     | Calculate             |
| `Backspace` | Delete last character |
| `Escape`    | Clear calculator      |

## ▶️ How to Run

Make sure Python is installed on your computer.

Save the program as:

```text
calculator.py
```

Run it using:

```bash
python calculator.py
```

A calculator window will open.

## 💻 Example Calculations

### Addition

```text
10 + 20 = 30
```

### Subtraction

```text
50 - 15 = 35
```

### Multiplication

```text
8 * 5 = 40
```

### Division

```text
100 / 4 = 25
```

### Square

```text
5² = 25
```

### Square Root

```text
√81 = 9
```

### Percentage

```text
50% = 0.5
```

## ⚠️ Error Handling

The calculator handles several common errors.

### Division by Zero

```text
10 / 0
```

Output:

```text
Error (Div by 0)
```

### Invalid Expression

If an invalid expression is entered:

```text
10 + *
```

the calculator displays:

```text
Error
```

### Negative Square Root

Trying to calculate:

```text
√-25
```

displays:

```text
Error (Negative √)
```

## 📚 What I Learned

Through this project, I practiced:

* Building GUI applications with Tkinter.
* Creating classes and objects.
* Using Object-Oriented Programming.
* Creating buttons dynamically.
* Using `grid()` for GUI layout.
* Handling button events.
* Using keyboard event bindings.
* Working with the `math` module.
* Using `lambda` functions.
* Handling exceptions.
* Working with strings and expressions.
* Creating reusable class methods.
* Designing a desktop application.

## 🚀 Future Improvements

Possible improvements:

* Add scientific calculator functions.
* Add calculation history.
* Add a light/dark theme switch.
* Add keyboard support for all calculator operations.
* Add memory buttons such as `M+`, `M-`, and `MR`.
* Add parentheses support.
* Add a more advanced expression parser.
* Add a calculation history panel.
* Package the application as a Windows `.exe`.

## ⚠️ Note

This project uses Python's `eval()` function to evaluate arithmetic expressions. Since `eval()` can execute arbitrary Python code, it should **not be used with untrusted input** in applications intended for real-world use.

## 👨‍💻 Author

**JOY ELISHA**

### 🐍 Python Journey

This project is part of my **Python Journey**, where I am learning Python through practical projects and building real-world programming skills.
