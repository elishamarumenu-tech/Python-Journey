import tkinter as tk
from tkinter import messagebox
import json
import os

FILENAME = "tasks.json"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python To-Do List")
        self.root.geometry("420x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.tasks = []

        self.setup_ui()
        self.load_tasks()

    def setup_ui(self):
        # Header Title
        title_label = tk.Label(
            self.root,
            text="My To-Do List",
            font=("Arial", 18, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        )
        title_label.pack(pady=(20, 10))

        # Input Frame (Entry + Add Button)
        input_frame = tk.Frame(self.root, bg="#1e1e2e")
        input_frame.pack(fill="x", padx=25, pady=10)

        self.task_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            bg="#313244",
            fg="#f5e0dc",
            insertbackground="white",
            relief="flat"
        )
        self.task_entry.pack(side="left", expand=True, fill="both", ipady=6, padx=(0, 10))
        self.task_entry.bind("<Return>", lambda e: self.add_task())

        add_btn = tk.Button(
            input_frame,
            text="Add",
            font=("Arial", 11, "bold"),
            bg="#a6e3a1",
            fg="#11111b",
            activebackground="#94e2d5",
            activeforeground="#11111b",
            bd=0,
            padx=15,
            cursor="hand2",
            command=self.add_task
        )
        add_btn.pack(side="right", fill="both")

        # Task Listbox with Scrollbar
        list_frame = tk.Frame(self.root, bg="#1e1e2e")
        list_frame.pack(expand=True, fill="both", padx=25, pady=10)

        self.task_listbox = tk.Listbox(
            list_frame,
            font=("Arial", 12),
            bg="#313244",
            fg="#cdd6f4",
            selectbackground="#45475a",
            selectforeground="#f5e0dc",
            bd=0,
            highlightthickness=0,
            activestyle="none"
        )
        self.task_listbox.pack(side="left", expand=True, fill="both")

        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.task_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.task_listbox.config(yscrollcommand=scrollbar.set)

        # Action Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#1e1e2e")
        btn_frame.pack(fill="x", padx=25, pady=(10, 20))

        complete_btn = tk.Button(
            btn_frame,
            text="Toggle Complete",
            font=("Arial", 10, "bold"),
            bg="#89b4fa",
            fg="#11111b",
            activebackground="#74c7ec",
            bd=0,
            pady=6,
            cursor="hand2",
            command=self.toggle_complete
        )
        complete_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))

        delete_btn = tk.Button(
            btn_frame,
            text="Delete",
            font=("Arial", 10, "bold"),
            bg="#f38ba8",
            fg="#11111b",
            activebackground="#eba0ac",
            bd=0,
            pady=6,
            cursor="hand2",
            command=self.delete_task
        )
        delete_btn.pack(side="left", expand=True, fill="x", padx=5)

        clear_btn = tk.Button(
            btn_frame,
            text="Clear All",
            font=("Arial", 10, "bold"),
            bg="#f9e2af",
            fg="#11111b",
            activebackground="#fab387",
            bd=0,
            pady=6,
            cursor="hand2",
            command=self.clear_all
        )
        clear_btn.pack(side="right", expand=True, fill="x", padx=(5, 0))

    def refresh_listbox(self):
        """Refreshes the Listbox visual contents based on local task data."""
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = f"✓ {task['text']}" if task["completed"] else f"• {task['text']}"
            self.task_listbox.insert(tk.END, display_text)

    def add_task(self):
        """Adds a new task to the list."""
        text = self.task_entry.get().strip()
        if not text:
            messagebox.showwarning("Empty Input", "Please enter a task description!")
            return

        self.tasks.append({"text": text, "completed": False})
        self.task_entry.delete(0, tk.END)
        self.save_tasks()
        self.refresh_listbox()

    def toggle_complete(self):
        """Marks the selected task as completed or active."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["completed"] = not self.tasks[selected_index]["completed"]
            self.save_tasks()
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Selection Required", "Please select a task to update!")

    def delete_task(self):
        """Deletes the selected task."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.save_tasks()
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Selection Required", "Please select a task to delete!")

    def clear_all(self):
        """Removes all tasks after user confirmation."""
        if self.tasks and messagebox.askyesno("Confirm Clear", "Are you sure you want to delete all tasks?"):
            self.tasks = []
            self.save_tasks()
            self.refresh_listbox()

    def save_tasks(self):
        """Saves current task items to a local JSON file."""
        try:
            with open(FILENAME, "w") as file:
                json.dump(self.tasks, file)
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self):
        """Loads saved tasks from the local JSON file on startup."""
        if os.path.exists(FILENAME):
            try:
                with open(FILENAME, "r") as file:
                    self.tasks = json.load(file)
                self.refresh_listbox()
            except Exception as e:
                print(f"Error loading tasks: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()