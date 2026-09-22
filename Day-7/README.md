# 🔐 PyPassword Generator

A simple **Password Generator built with Python** that creates random passwords using a combination of **letters, numbers, and symbols**.

The user can choose how many letters, numbers, and symbols should be included in the password. The characters are then shuffled to create a more random password.

## 📌 Description

The program asks the user:

* How many letters they want.
* How many numbers they want.
* How many symbols they want.

It then:

1. Selects random letters.
2. Selects random numbers.
3. Selects random symbols.
4. Stores them in a password list.
5. Shuffles the characters randomly.
6. Combines the characters into a final password.
7. Displays the generated password.

## 🔑 Password Generation

The program uses three character categories:

### 🔤 Letters

Both lowercase and uppercase letters are available:

```text
a-z
A-Z
```

### 🔢 Numbers

Numbers from:

```text
0-9
```

### 🔣 Symbols

The program uses:

```text
! # $ % & ( ) * +
```

## 🧩 Two Password Generation Levels

### Easy Level

The commented-out Easy Level generates the password in this order:

```text
Letters → Numbers → Symbols
```

For example:

```text
abcXYZ123!@#
```

### Hard Level

The current program uses the Hard Level.

After generating the required characters, it uses:

```python
random.shuffle(password_list)
```

This randomly changes the order of the characters.

Example:

```text
a7#B2!xZ9
```

This makes the password less predictable.

## 🛠️ Technologies Used

* **Python**
* `random` module
* Lists
* `for` loops
* `random.choice()`
* `random.shuffle()`
* `input()`
* Type conversion using `int()`

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python password_generator.py
```

## 💻 Example Output

```text
Welcome to the PyPassword Generator!

How many letters Would you like in your password? 5
How many numbers Would you like? 3
H
```
