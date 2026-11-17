import tkinter as tk
from tkinter import messagebox

class CountdownTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Countdown Timer")
        self.root.geometry("420x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.remaining_time = 0
        self.is_running = False
        self.timer_id = None

        self.setup_ui()

    def setup_ui(self):
        # Header Title
        title_label = tk.Label(
            self.root,
            text="Countdown Timer",
            font=("Arial", 18, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        )
        title_label.pack(pady=(20, 15))

        # Timer Display (Large Font)
        self.time_display_label = tk.Label(
            self.root,
            text="00:30",
            font=("Arial", 54, "bold"),
            bg="#1e1e2e",
            fg="#89b4fa"
        )
        self.time_display_label.pack(pady=10)

        # Input Frame (Minutes & Seconds)
        input_frame = tk.Frame(self.root, bg="#1e1e2e")
        input_frame.pack(fill="x", padx=40, pady=10)

        # Minutes Input
        min_frame = tk.Frame(input_frame, bg="#1e1e2e")
        min_frame.pack(side="left", expand=True, fill="x", padx=(0, 10))
        tk.Label(min_frame, text="Minutes:", font=("Arial", 10), bg="#1e1e2e", fg="#cdd6f4").pack(anchor="w", pady=(0, 2))
        
        self.min_entry = tk.Entry(min_frame, font=("Arial", 14), bg="#313244", fg="#f5e0dc", insertbackground="white", relief="flat", justify="center")
        self.min_entry.pack(fill="x", ipady=6)
        self.min_entry.insert(0, "0")

        # Seconds Input
        sec_frame = tk.Frame(input_frame, bg="#1e1e2e")
        sec_frame.pack(side="right", expand=True, fill="x", padx=(10, 0))
        tk.Label(sec_frame, text="Seconds:", font=("Arial", 10), bg="#1e1e2e", fg="#cdd6f4").pack(anchor="w", pady=(0, 2))
        
        self.sec_entry = tk.Entry(sec_frame, font=("Arial", 14), bg="#313244", fg="#f5e0dc", insertbackground="white", relief="flat", justify="center")
        self.sec_entry.pack(fill="x", ipady=6)
        self.sec_entry.insert(0, "30")

        # Control Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#1e1e2e")
        btn_frame.pack(fill="x", padx=40, pady=20)

        self.start_btn = tk.Button(
            btn_frame,
            text="Start",
            font=("Arial", 11, "bold"),
            bg="#a6e3a1",
            fg="#11111b",
            activebackground="#94e2d5",
            bd=0,
            pady=8,
            cursor="hand2",
            command=self.start_timer
        )
        self.start_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))

        self.pause_btn = tk.Button(
            btn_frame,
            text="Pause",
            font=("Arial", 11, "bold"),
            bg="#f9e2af",
            fg="#11111b",
            activebackground="#fab387",
            bd=0,
            pady=8,
            cursor="hand2",
            command=self.pause_timer
        )
        self.pause_btn.pack(side="left", expand=True, fill="x", padx=5)

        self.reset_btn = tk.Button(
            btn_frame,
            text="Reset",
            font=("Arial", 11, "bold"),
            bg="#f38ba8",
            fg="#11111b",
            activebackground="#eba0ac",
            bd=0,
            pady=8,
            cursor="hand2",
            command=self.reset_timer
        )
        self.reset_btn.pack(side="right", expand=True, fill="x", padx=(5, 0))

    def start_timer(self):
        """Starts or resumes the countdown timer."""
        if self.is_running:
            return

        if self.remaining_time == 0:
            try:
                mins = int(self.min_entry.get().strip() or 0)
                secs = int(self.sec_entry.get().strip() or 0)
                self.remaining_time = (mins * 60) + secs
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid integer numbers for minutes and seconds.")
                return

        if self.remaining_time <= 0:
            messagebox.showwarning("Time Required", "Please enter a time greater than 0.")
            return

        self.is_running = True
        self.run_countdown()

    def run_countdown(self):
        """Recursively updates the timer every second using root.after."""
        if self.is_running and self.remaining_time >= 0:
            mins, secs = divmod(self.remaining_time, 60)
            self.time_display_label.config(text=f"{mins:02d}:{secs:02d}")
            
            if self.remaining_time == 0:
                self.is_running = False
                messagebox.showinfo("Time's Up!", "Countdown timer has finished!")
                return

            self.remaining_time -= 1
            self.timer_id = self.root.after(1000, self.run_countdown)

    def pause_timer(self):
        """Pauses the countdown loop."""
        if self.is_running:
            self.is_running = False
            if self.timer_id:
                self.root.after_cancel(self.timer_id)

    def reset_timer(self):
        """Resets the timer back to zero and clears states."""
        self.pause_timer()
        self.remaining_time = 0
        self.time_display_label.config(text="00:00")
        self.min_entry.delete(0, tk.END)
        self.min_entry.insert(0, "0")
        self.sec_entry.delete(0, tk.END)
        self.sec_entry.insert(0, "0")


if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimerApp(root)
    root.mainloop()             