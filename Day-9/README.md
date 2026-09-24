# 🏆 Silent Auction

A command-line **Silent Auction program built with Python** where multiple bidders can secretly enter their bids. The program determines the bidder with the highest bid and announces the winner at the end.

This project demonstrates dictionaries, functions, loops, input validation, exception handling, and terminal screen clearing.

## 📌 Description

The Silent Auction program allows multiple users to participate in an auction.

The program:

1. Asks each bidder for their name.
2. Collects their bid amount.
3. Validates the bid.
4. Stores each bidder and their bid in a dictionary.
5. Clears the screen between bidders to keep bids private.
6. Determines the highest bidder.
7. Displays the winner and their bid amount.

## ✨ Features

* 👤 Multiple bidders.
* 💰 Custom bid amounts.
* 🔒 Clears the terminal between bidders.
* 🏆 Automatically finds the highest bidder.
* 💵 Displays bids with currency formatting.
* ❌ Validates invalid bid input.
* ✅ Prevents empty bidder names.
* 🔄 Allows the auction to continue until all bidders are finished.
* 🖥️ Works on Windows, macOS, and Linux.

## 🧩 Program Structure

### `clear_screen()`

```python
def clear_screen():
```

Clears the terminal screen so the next bidder cannot easily see previous bids.

The program detects the operating system using:

```python
os.name
```

and uses:

```text
Windows → cls
macOS/Linux → clear
```

### `find_highest_bidder()`

```python
def find_highest_bidder(bids_dict: dict):
```

Loops through the dictionary of bidders and finds the person with the highest bid.

It stores:

* Highest bid amount
* Winner's name

The result is then displayed in a formatted message.

### `main()`

```python
def main():
```

Controls the complete auction process.

It handles:

* Bidder registration.
* Bid collection.
* Input validation.
* Storing bids.
* Checking for additional bidders.
* Ending the auction.

## 📚 Data Structure Used

The program uses a **dictionary** to store bidder information.

Example:

```python
bids = {
    "Alice": 500,
    "Bob": 750,
    "Charlie": 600
}
```

Here:

```text
Key   → Bidder name
Value → Bid amount
```

This makes it easy to compare all bids.

## 🛠️ Technologies Used

* **Python**
* `os` module
* Dictionary
* Functions
* `while` loops
* `for` loops
* `if-elif-else`
* `try-except`
* String methods
* f-strings
* Type hints

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program:

```bash
python silent_auction.py
```

## 💻 Example Output

```text
========================================
       WELCOME TO THE SILENT AUCTION
========================================

What is your name? Alice
What is your bid? $500

Are there any other bidders? (yes/no): yes
```

The screen is cleared for the next bidder.

```text
What is your name? Bob
What is your bid? $750

Are there any other bidders? (yes/no): yes
```

Another bidder:

```text
What is your name? Charlie
What is your bid? $600

Are there any other bidders? (yes/no): no
```

Finally:

```text
========================================
  🏆 THE WINNER IS BOB WITH A BID OF $750.00! 🏆
========================================
```

## ❌ Input Validation

### Empty Name

If the bidder doesn't enter a name:

```text
Name cannot be empty. Please enter your name:
```

### Invalid Bid

If the bidder enters text instead of a number:

```text
What is your bid? $abc
Invalid input. Please enter a numerical amount (e.g., 50 or 12.50).
```

### Zero or Negative Bid

```text
What is your bid? $-50
Bid amount must be greater than $0.
```

### Invalid Continue Option

```text
Are there any other bidders? (yes/no): maybe
Please answer 'yes' or 'no'.
```

## 📚 What I Learned

Through this project, I practiced:

* Creating and using dictionaries.
* Storing key-value pairs.
* Creating reusable functions.
* Using `for` and `while` loops.
* Finding the maximum value manually.
* Handling invalid user input.
* Using `try-except` for error handling.
* Working with the `os` module.
* Clearing the terminal screen.
* Formatting currency using f-strings.
* Using type hints.
* Building a complete interactive command-line application.

## 🚀 Future Improvements

Possible improvements:

* Add a minimum bid increment.
* Prevent duplicate bidder names from overwriting previous bids.
* Display the complete auction results after the winner is selected.
* Add a timer for bidding.
* Save auction results to a file.
* Add a graphical user interface.
* Support multiple auction rounds.
* Add an option to export results as CSV.

## ⚠️ Note

The terminal-clearing feature helps keep bids private during normal use, but it should not be considered a secure method for protecting sensitive information.

## 👨‍💻 Author

**JOY ELISHA**

### 🐍 Python Journey

This project is part of my **Python Journey**, where I am learning Python through practical projects and progressively improving my programming skills.
