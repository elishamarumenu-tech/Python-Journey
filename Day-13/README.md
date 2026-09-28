# ✅ Python To-Do List App

A simple and interactive desktop To-Do List application built using Python and Tkinter. This application helps users organize daily tasks, track completion status, and save tasks locally using JSON file storage.

## 📌 Project Description

The Python To-Do List is a GUI-based task management application designed to help users manage their daily activities efficiently.

Users can add new tasks, mark them as completed, delete individual tasks, and clear all tasks. The application automatically saves tasks in a local JSON file, allowing tasks to remain available even after closing and reopening the program.

## ✨ Features

* User-friendly graphical interface.
* Add new tasks using an input field.
* Mark tasks as completed or active.
* Delete selected tasks.
* Clear all tasks with confirmation.
* Automatically save tasks using JSON.
* Load previously saved tasks on startup.
* Scrollable task list.
* Keyboard support using the Enter key.
* Dark-themed interface.
* Warning messages for invalid actions.

## 🛠️ Technologies Used

| Technology | Purpose                                 |
| ---------- | --------------------------------------- |
| Python     | Core programming language               |
| Tkinter    | Graphical user interface                |
| JSON       | Local task data storage                 |
| OS module  | Checks whether the task file exists     |
| OOP        | Organizes the application using a class |

## 📂 Project Structure

```text
Python-To-Do-List/
│
├── todo.py
├── tasks.json
└── README.md
```

**Note:** `tasks.json` is automatically created when tasks are saved. It stores the task descriptions and their completion status.

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Tkinter, JSON, and OS are included with standard Python installations.

### Step 2: Run the application

Open a terminal in the project folder and execute:

```bash
python todo.py
```

The To-Do List application window will open.

## 🎮 How to Use

1. Enter a task description in the input box.
2. Click **Add** or press Enter to add the task.
3. Select a task from the list.
4. Click **Toggle Complete** to mark it completed or active.
5. Click **Delete** to remove the selected task.
6. Click **Clear All** to remove every task after confirmation.

Completed tasks are displayed with a check mark (✓), while active tasks are displayed with a bullet (•).

## 💾 Data Storage

The application stores tasks in a local JSON file named `tasks.json`.

Example:

```json
[
    {
        "text": "Learn Python",
        "completed": true
    },
    {
        "text": "Practice Tkinter",
        "completed": false
    }
]
```

Each task contains two properties:

* `text`: The description of the task.
* `completed`: A Boolean value indicating whether the task is completed.

When the application starts, it loads previously saved tasks from the JSON file.

## 🧩 Main Functions

| Function            | Purpose                               |
| ------------------- | ------------------------------------- |
| `setup_ui()`        | Creates the application interface.    |
| `refresh_listbox()` | Updates the task list display.        |
| `add_task()`        | Adds a new task.                      |
| `toggle_complete()` | Changes the completion status.        |
| `delete_task()`     | Deletes the selected task.            |
| `clear_all()`       | Removes all tasks after confirmation. |
| `save_tasks()`      | Saves tasks to the JSON file.         |
| `load_tasks()`      | Loads saved tasks on startup.         |

## 🧠 Concepts Learned

Through this project, I practiced:

* Python classes, objects, and methods.
* Tkinter widgets, buttons, frames, and listboxes.
* Event handling and callback functions.
* Lists and dictionaries.
* File handling with `open()`.
* JSON serialization and deserialization.
* Exception handling using `try-except`.
* Conditional statements and loops.
* Persistent local data storage.
* GUI-based user interaction.

## 🚀 Future Improvements

* Add due dates and reminders.
* Introduce task priority levels.
* Add categories for organizing tasks.
* Include a search and filter feature.
* Display task completion statistics.
* Add dark and light theme options.
* Export tasks to CSV or Excel.

## 👨‍💻 Author

**JOY ELISHA**

Python Journey – Learning Python through practical projects.

---

⭐ If you like this project, consider giving the repository a star!
