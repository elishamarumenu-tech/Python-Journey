import tkinter as tk
from tkinter import messagebox

class GradeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grade Calculator")
        self.root.geometry("450x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.scores = []

        self.setup_ui()

    def setup_ui(self):
        # Header Title
        title_label = tk.Label(
            self.root,
            text="Student Grade Calculator",
            font=("Arial", 18, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        )
        title_label.pack(pady=(20, 10))

        # Input Frame
        input_frame = tk.Frame(self.root, bg="#1e1e2e")
        input_frame.pack(fill="x", padx=25, pady=10)

        tk.Label(
            input_frame, 
            text="Enter Score (0-100):", 
            font=("Arial", 11), 
            bg="#1e1e2e", 
            fg="#cdd6f4"
        ).pack(anchor="w", pady=(0, 5))
        
        entry_box_frame = tk.Frame(input_frame, bg="#1e1e2e")
        entry_box_frame.pack(fill="x")

        self.score_entry = tk.Entry(
            entry_box_frame,
            font=("Arial", 14),
            bg="#313244",
            fg="#f5e0dc",
            insertbackground="white",
            relief="flat"
        )
        self.score_entry.pack(side="left", expand=True, fill="both", ipady=6, padx=(0, 10))
        self.score_entry.bind("<Return>", lambda e: self.add_score())

        add_btn = tk.Button(
            entry_box_frame,
            text="Add Score",
            font=("Arial", 10, "bold"),
            bg="#a6e3a1",
            fg="#11111b",
            activebackground="#94e2d5",
            bd=0,
            padx=15,
            cursor="hand2",
            command=self.add_score
        )
        add_btn.pack(side="right", fill="both")

        # Scores Listbox
        list_frame = tk.Frame(self.root, bg="#1e1e2e")
        list_frame.pack(fill="both", padx=25, pady=10, expand=True)

        tk.Label(
            list_frame, 
            text="Recorded Scores:", 
            font=("Arial", 10, "bold"), 
            bg="#1e1e2e", 
            fg="#a6adc8"
        ).pack(anchor="w", pady=(0, 2))

        self.score_listbox = tk.Listbox(
            list_frame,
            font=("Arial", 12),
            bg="#313244",
            fg="#cdd6f4",
            selectbackground="#45475a",
            selectforeground="#f5e0dc",
            bd=0,
            highlightthickness=0
        )
        self.score_listbox.pack(side="left", expand=True, fill="both")

        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.score_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.score_listbox.config(yscrollcommand=scrollbar.set)

        # Action Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#1e1e2e")
        btn_frame.pack(fill="x", padx=25, pady=10)

        calc_btn = tk.Button(
            btn_frame,
            text="Calculate Grade",
            font=("Arial", 11, "bold"),
            bg="#89b4fa",
            fg="#11111b",
            activebackground="#74c7ec",
            bd=0,
            pady=8,
            cursor="hand2",
            command=self.calculate_grade
        )
        calc_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))

        clear_btn = tk.Button(
            btn_frame,
            text="Clear All",
            font=("Arial", 11, "bold"),
            bg="#f38ba8",
            fg="#11111b",
            activebackground="#eba0ac",
            bd=0,
            pady=8,
            cursor="hand2",
            command=self.clear_scores
        )
        clear_btn.pack(side="right", expand=True, fill="x", padx=(5, 0))

    def add_score(self):
        """Validates and adds a score to the tracking list."""
        val_str = self.score_entry.get().strip()
        if not val_str:
            messagebox.showwarning("Empty Input", "Please enter a score value!")
            return
        try:
            score = float(val_str)
            if not (0 <= score <= 100):
                messagebox.showwarning("Invalid Range", "Score must be between 0 and 100.")
                return
            self.scores.append(score)
            self.score_listbox.insert(tk.END, f"Score Entry: {score}")
            self.score_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric score.")

    def calculate_grade(self):
        """Computes the final average and assigns a standard letter grade."""
        if not self.scores:
            messagebox.showwarning("No Scores", "Please add at least one score before calculating!")
            return

        avg = sum(self.scores) / len(self.scores)

        if avg >= 90:
            grade = "A (Excellent)"
        elif avg >= 80:
            grade = "B (Good)"
        elif avg >= 70:
            grade = "C (Satisfactory)"
        elif avg >= 60:
            grade = "D (Passing)"
        else:
            grade = "F (Needs Improvement)"

        result_msg = (
            f"Total Scores Logged: {len(self.scores)}\n"
            f"Average Score: {avg:.2f}%\n"
            f"Final Letter Grade: {grade}"
        )
        messagebox.showinfo("Grade Calculation Results", result_msg)

    def clear_scores(self):
        """Clears all logged scores after user confirmation."""
        if self.scores and messagebox.askyesno("Confirm Clear", "Are you sure you want to clear all scores?"):
            self.scores = []
            self.score_listbox.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = GradeCalculatorApp(root)
    root.mainloop()