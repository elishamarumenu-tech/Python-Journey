import tkinter as tk
import time

class DigitalClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Digital Clock")
        self.root.geometry("450x220")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.setup_ui()
        self.update_clock()

    def setup_ui(self):
        # App Header
        title_label = tk.Label(
            self.root,
            text="DIGITAL CLOCK",
            font=("Arial", 11, "bold"),
            bg="#1e1e2e",
            fg="#a6adc8"
        )
        title_label.pack(pady=(20, 5))

        # Time Display Label (Large Font)
        self.time_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 42, "bold"),
            bg="#1e1e2e",
            fg="#89b4fa"
        )
        self.time_label.pack(pady=10)

        # Date & Day Display Label
        self.date_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 14),
            bg="#1e1e2e",
            fg="#f5e0dc"
        )
        self.date_label.pack(pady=(0, 20))

    def update_clock(self):
        """Fetches current system time and updates the UI labels every second."""
        # Format time as 12-hour format with AM/PM (e.g., 02:45:30 PM)
        current_time = time.strftime("%I:%M:%S %p")
        
        # Format date (e.g., Monday, October 19, 2026)
        current_date = time.strftime("%A, %B %d, %Y")

        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)

        # Schedule update_clock to run again after 1000 milliseconds (1 second)
        self.root.after(1000, self.update_clock)


if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClockApp(root)
    root.mainloop()