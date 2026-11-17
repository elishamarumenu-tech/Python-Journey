# Python Countdown Timer

A simple and interactive **Countdown Timer desktop application** developed using Python and Tkinter. It allows users to set a custom time in minutes and seconds, start the countdown, pause it, resume it, and reset the timer through a user-friendly graphical interface.

## Features

- **Custom Time Input:** Set countdown time using minutes and seconds.
- **Start Timer:** Begin the countdown.
- **Pause Timer:** Pause the countdown at any moment.
- **Resume Timer:** Continue from the remaining time.
- **Reset Timer:** Reset the timer and clear the input fields.
- **Live Display:** Shows the remaining time in `MM:SS` format.
- **Completion Alert:** Displays a message when the countdown reaches zero.
- **Input Validation:** Handles invalid and zero or negative time values.
- **Modern GUI:** Attractive dark-themed interface.
- **Simple Controls:** Easy-to-use Start, Pause, and Reset buttons.

## Technologies Used

- **Python 3**
- **Tkinter** – GUI development
- **Messagebox** – Warning, error, and completion messages
- **`root.after()`** – Updates the countdown every second
- **Object-Oriented Programming (OOP)** – Organizes application functionality using a class

## Project Structure

```text
Python-Countdown-Timer/
│
├── countdown_timer.py
└── README.md
```

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/elishamarumenu-tech/Python-Journey.git
```

### 2. Navigate to the Project Folder

```bash
cd Python-Journey
```

### 3. Run the Program

```bash
python countdown_timer.py
```

**Note:** Python 3 must be installed. Tkinter is included with most standard Python installations.

## How to Use

1. Open the Countdown Timer application.
2. Enter the required minutes.
3. Enter the required seconds.
4. Click **Start** to begin the countdown.
5. Click **Pause** to temporarily stop the timer.
6. Click **Start** again to resume.
7. Click **Reset** to clear the timer and enter a new time.
8. When the timer reaches zero, a completion alert appears.

## Example

Suppose you enter:

| Input | Value |
|---|---:|
| Minutes | 1 |
| Seconds | 30 |
| Total Time | 90 seconds |

The timer displays:

```text
01:30
01:29
01:28
...
00:01
00:00
```

When the countdown finishes, the application displays a **"Time's Up!"** message.

## Main Functions

| Function | Description |
|---|---|
| `setup_ui()` | Creates the graphical user interface. |
| `start_timer()` | Starts or resumes the countdown. |
| `run_countdown()` | Updates the remaining time every second. |
| `pause_timer()` | Pauses the countdown and cancels the scheduled callback. |
| `reset_timer()` | Resets the timer and clears the input fields. |

## Concepts Learned

- Python Object-Oriented Programming (OOP)
- Tkinter GUI development
- Labels, buttons, frames, and entry fields
- Class methods and instance variables
- Conditional statements
- Exception handling using `try-except`
- Time calculation using `divmod()`
- Event-driven programming
- Scheduling callbacks using `root.after()`
- Managing timer states using Boolean variables

## Future Improvements

- Add alarm sound when the timer finishes.
- Add multiple countdown timers.
- Add a stopwatch feature.
- Add preset