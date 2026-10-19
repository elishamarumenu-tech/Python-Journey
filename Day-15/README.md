# 🕒 Python Digital Clock

A simple and stylish digital clock application built using **Python and Tkinter**. It displays the current system time in 12-hour format with AM/PM, along with the current date and day. The clock updates automatically every second.

## 📌 Project Description

The Python Digital Clock is a desktop GUI application designed to display real-time information in a clean and user-friendly interface.

Using Python's built-in `time` module, the application retrieves the current system time and date. Tkinter provides the graphical interface, while its `after()` method refreshes the display every second without blocking the application.

## ✨ Features

- Displays the current time in 12-hour format.
- Shows hours, minutes, seconds, and AM/PM.
- Displays the current day, month, date, and year.
- Automatically updates every second.
- Simple and attractive dark-themed interface.
- Large, easy-to-read time display.
- Fixed-size application window.
- Lightweight application with no external libraries required.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Tkinter | Graphical user interface |
| Time module | Retrieves and formats system time and date |
| `after()` method | Schedules updates every second |
| OOP | Organizes the application using a class |

## 📂 Project Structure

```text
Python-Digital-Clock/
│
├── digital_clock.py
└── README.md
```

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Tkinter and the `time` module are included with standard Python installations.

### Step 2: Run the application

Open a terminal in the project folder and execute:

```bash
python digital_clock.py
```

The digital clock window will open and start displaying the current time and date.

## 🖥️ Application Display

The application displays information in the following format:

```text
        DIGITAL CLOCK

         01:45:30 PM

   Monday, October 19, 2026
```

*The displayed time and date will reflect your computer's current system settings.*

## ⚙️ How It Works

1. The `DigitalClockApp` class initializes the application window.
2. The `setup_ui()` method creates the title, time display, and date display.
3. The `update_clock()` method retrieves the current time using `time.strftime()`.
4. The time and date labels are updated with the latest values.
5. The `root.after(1000, self.update_clock)` statement schedules the next update after 1,000 milliseconds.
6. The process repeats every second while the application remains open.

## 🧩 Main Methods

| Method | Purpose |
|---|---|
| `__init__()` | Initializes the window and starts the clock. |
| `setup_ui()` | Creates the graphical interface. |
| `update_clock()` | Updates the time and date every second. |

## 🧠 Concepts Learned

Through this project, I practiced:

- Python classes and objects.
- Tkinter labels and window configuration.
- The Python `time` module.
- Formatting dates and times using `strftime()`.
- GUI updates and event scheduling.
- The Tkinter `after()` method.
- Object-oriented programming.
- Creating a continuously updating desktop application.

## 🚀 Future Improvements

- Add a 24-hour time format option.
- Add a light and dark theme switch.
- Display the current timezone.
- Add an alarm clock feature.
- Add a stopwatch and countdown timer.
- Display a digital calendar.
- Add customizable fonts and colors.

## 👨‍💻 Author

**JOY ELISHA**

Python Journey — Learning Python through practical projects.

---

⭐ If you like this project, consider giving the repository a star!