# 🔐 Caesar Cipher

A simple and interactive **Caesar Cipher program built with Python** that allows users to **encrypt and decrypt messages** using a customizable shift value.

This project demonstrates string manipulation, functions, loops, conditional statements, ASCII operations, modulo arithmetic, and exception handling.

## 📌 Description

The Caesar Cipher is a basic encryption technique where each letter in a message is shifted by a fixed number of positions in the alphabet.

For example, with a shift of `3`:

```text
A → D
B → E
C → F
```

Therefore:

```text
HELLO
```

becomes:

```text
KHOOR
```

The same program can reverse the process to decrypt the message.

## ✨ Features

* 🔒 Encrypt text.
* 🔓 Decrypt text.
* 🔢 Accept custom shift values.
* 🔠 Preserve uppercase and lowercase letters.
* 🔤 Leave spaces and punctuation unchanged.
* 🔄 Support positive and negative shifts.
* ❌ Validate user input.
* 🔁 Perform multiple operations without restarting.
* 🚪 Quit the program at any time.

## 🧩 How It Works

### 1. Choose an Operation

The program asks:

```text
Do you want to (E)ncrypt or (D)ecrypt?
```

The user can enter:

* `E` or `Encrypt`
* `D` or `Decrypt`
* `Q` or `Quit`

### 2. Enter the Message

The user enters the text they want to encrypt or decrypt.

Example:

```text
Hello World
```

### 3. Enter the Shift

The user provides an integer shift value.

Example:

```text
Enter shift value (integer): 3
```

### 4. Apply the Caesar Cipher

Each alphabetic character is shifted according to the selected shift value.

With a shift of `3`:

```text
Hello World
```

becomes:

```text
Khoor Zruog
```

## 🔄 Encryption and Decryption

### Encryption

Encryption moves letters forward through the alphabet.

```text
HELLO
```

with shift `3`:

```text
KHOOR
```

### Decryption

Decryption moves letters backward.

```text
KHOOR
```

with shift `3`:

```text
HELLO
```

The program reverses the shift when the selected mode is `decode`.

## 🔤 Uppercase and Lowercase

The program preserves the original case of letters.

Example:

```text
Hello World
```

with a shift of `3` becomes:

```text
Khoor Zruog
```

Uppercase letters remain uppercase and lowercase letters remain lowercase.

## 🔣 Special Characters

Non-alphabetic characters remain unchanged.

For example:

```text
Hello, World! 123
```

with a shift of `3` becomes:

```text
Khoor, Zruog! 123
```

## 🧮 Modulo 26

The program uses:

```python
shift = shift % 26
```

This keeps the shift within the 26-letter alphabet.

It also allows the alphabet to wrap around.

For example, with a shift of `3`:

```text
X → A
Y → B
Z → C
```

## 🛠️ Technologies Used

* **Python**
* Functions
* Loops
* Conditional statements
* String manipulation
* Lists
* `ord()`
* `chr()`
* Modulo arithmetic
* Exception handling
* Type hints
* Docstrings

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program:

```bash
python caesar_cipher.py
```

## 💻 Example Output

```text
===================================
      CAESAR CIPHER PROGRAM
===================================

Do you want to (E)ncrypt or (D)ecrypt? (Or type 'Q' to quit): e

Enter your message: Hello World
Enter shift value (integer): 3

Result (ENCODED): Khoor Zruog
```

### 🔓 Decryption Example

```text
Do you want to (E)ncrypt or (D)ecrypt? (Or type 'Q' to quit): d

Enter your message: Khoor Zruog
Enter shift value (integer): 3

Result (DECODED): Hello World
```

## ❌ Input Validation

The program checks whether the user entered a valid operation.

```text
Invalid choice. Please enter 'E', 'D', or 'Q'.
```

It also validates the shift value:

```text
Enter shift value (integer): abc
Please enter a valid integer for the shift value.
```

## 📚 What I Learned

Through this project, I practiced:

* Creating reusable functions.
* Using parameters and default arguments.
* Working with strings and characters.
* Using `ord()` and `chr()`.
* Applying modulo arithmetic.
* Working with positive and negative values.
* Using `while` loops.
* Using conditional statements.
* Handling errors with `try-except`.
* Using type hints.
* Writing docstrings.
* Building an interactive command-line application.

## 🚀 Future Improvements

Possible improvements include:

* Add brute-force decryption.
* Add a graphical user interface.
* Add file encryption and decryption.
* Support custom alphabets.
* Add encryption history.
* Add a menu-based interface.
* Add more advanced encryption algorithms.

## ⚠️ Security Note

The Caesar Cipher is mainly useful for **learning programming and basic cryptography concepts**. It should not be used to protect sensitive or confidential information because it is very easy to break.

## 👨‍💻 Author

**JOY ELISHA**

### 🐍 Python Journey

This project is part of my **Python Journey**, where I am learning Python through practical projects and continuously improving my programming skills.
