import tkinter as tk
from tkinter import messagebox

# Question Bank: List of dictionaries containing questions, choices, and correct answers
QUESTION_BANK = [
    {
        "question": "Which programming language is known as the 'Language of the Web'?",
        "options": ["Python", "JavaScript", "C++", "Java"],
        "answer": "JavaScript"
    },
    {
        "question": "What is the keyword used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "Which data structure operates on a First-In, First-Out (FIFO) basis?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "Queue"
    },
    {
        "question": "What is the output of 3 * '2' in Python?",
        "options": ["6", "222", "Error", "33"],
        "answer": "222"
    },
    {
        "question": "Which symbol is used for single-line comments in Python?",
        "options": ["//", "/*", "#", "--"],
        "answer": "#"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Knowledge Quiz")
        self.root.geometry("500x480")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.questions = QUESTION_BANK
        self.current_index = 0
        self.score = 0
        self.selected_option = tk.StringVar()

        self.setup_ui()
        self.load_question()

    def setup_ui(self):
        # Header / Title
        self.title_label = tk.Label(
            self.root,
            text="Python Knowledge Quiz",
            font=("Arial", 18, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        )
        self.title_label.pack(pady=(20, 10))

        # Progress / Question Counter
        self.progress_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 11),
            bg="#1e1e2e",
            fg="#a6adc8"
        )
        self.progress_label.pack(pady=(0, 15))

        # Question Frame
        self.question_frame = tk.Frame(self.root, bg="#313244", padx=15, pady=15)
        self.question_frame.pack(fill="x", padx=20)

        self.question_label = tk.Label(
            self.question_frame,
            text="",
            font=("Arial", 13, "bold"),
            bg="#313244",
            fg="#f5e0dc",
            wraplength=420,
            justify="center"
        )
        self.question_label.pack()

        # Options Container
        self.options_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.options_frame.pack(fill="x", padx=40, pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(
                self.options_frame,
                text="",
                value="",
                variable=self.selected_option,
                font=("Arial", 12),
                bg="#1e1e2e",
                fg="#cdd6f4",
                selectcolor="#45475a",
                activebackground="#1e1e2e",
                activeforeground="#cdd6f4",
                anchor="w",
                padx=10,
                pady=5
            )
            btn.pack(fill="x", pady=4)
            self.option_buttons.append(btn)

        # Feedback Label
        self.feedback_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 11, "italic"),
            bg="#1e1e2e",
            fg="#a6e3a1"
        )
        self.feedback_label.pack(pady=5)

        # Submit / Next Button
        self.submit_btn = tk.Button(
            self.root,
            text="Submit Answer",
            font=("Arial", 12, "bold"),
            bg="#89b4fa",
            fg="#11111b",
            activebackground="#74c7ec",
            activeforeground="#11111b",
            bd=0,
            padx=20,
            pady=8,
            cursor="hand2",
            command=self.check_answer
        )
        self.submit_btn.pack(pady=10)

    def load_question(self):
        """Loads the current question and options into the UI."""
        q_data = self.questions[self.current_index]

        self.progress_label.config(
            text=f"Question {self.current_index + 1} of {len(self.questions)}"
        )
        self.question_label.config(text=q_data["question"])
        self.selected_option.set("")  # Clear previous selection
        self.feedback_label.config(text="")

        for i, option in enumerate(q_data["options"]):
            self.option_buttons[i].config(text=f"  {option}", value=option, state="normal")

        self.submit_btn.config(text="Submit Answer", command=self.check_answer)

    def check_answer(self):
        """Validates the selected answer and gives immediate visual feedback."""
        chosen = self.selected_option.get()

        if not chosen:
            messagebox.showwarning("Selection Required", "Please select an option before submitting!")
            return

        correct_answer = self.questions[self.current_index]["answer"]

        # Disable radio buttons after submitting
        for btn in self.option_buttons:
            btn.config(state="disabled")

        if chosen == correct_answer:
            self.score += 1
            self.feedback_label.config(text="✓ Correct!", fg="#a6e3a1")  # Green accent
        else:
            self.feedback_label.config(
                text=f"✗ Incorrect! Correct answer: {correct_answer}", 
                fg="#f38ba8"  # Red accent
            )

        # Prepare button for the next step
        if self.current_index < len(self.questions) - 1:
            self.submit_btn.config(text="Next Question ➔", command=self.next_question)
        else:
            self.submit_btn.config(text="View Results 🏁", command=self.show_results)

    def next_question(self):
        """Advances to the next question."""
        self.current_index += 1
        self.load_question()

    def show_results(self):
        """Displays final score summary screen with options to restart."""
        total = len(self.questions)
        percentage = round((self.score / total) * 100)

        result_message = (
            f"Quiz Finished!\n\n"
            f"Your Score: {self.score} / {total}\n"
            f"Accuracy: {percentage}%\n\n"
        )
        
        if percentage >= 80:
            result_message += "🎉 Great job! Outstanding performance!"
        elif percentage >= 50:
            result_message += "👍 Good effort! Keep practicing."
        else:
            result_message += "📚 Don't worry! Review the concepts and try again."

        play_again = messagebox.askyesno("Results", result_message + "\n\nWould you like to restart?")
        
        if play_again:
            self.restart_quiz()
        else:
            self.root.destroy()

    def restart_quiz(self):
        """Resets the state to play again."""
        self.current_index = 0
        self.score = 0
        self.load_question()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()