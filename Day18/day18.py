import tkinter as tk
from tkinter import ttk, messagebox

# Standard exchange rates relative to USD (Base Currency)
EXCHANGE_RATES = {
    "USD": 1.00,
    "EUR": 0.92,
    "GBP": 0.79,
    "INR": 83.12,
    "JPY": 155.45,
    "CAD": 1.36,
    "AUD": 1.52,
    "CHF": 0.91,
    "CNY": 7.23
}

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Currency Converter")
        self.root.geometry("420x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.setup_ui()

    def setup_ui(self):
        # Header Title
        title_label = tk.Label(
            self.root,
            text="Currency Converter",
            font=("Arial", 18, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        )
        title_label.pack(pady=(20, 15))

        # Amount Input Frame
        input_frame = tk.Frame(self.root, bg="#1e1e2e")
        input_frame.pack(fill="x", padx=30, pady=10)

        tk.Label(
            input_frame, 
            text="Amount to Convert:", 
            font=("Arial", 11), 
            bg="#1e1e2e", 
            fg="#cdd6f4"
        ).pack(anchor="w", pady=(0, 5))
        
        self.amount_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            bg="#313244",
            fg="#f5e0dc",
            insertbackground="white",
            relief="flat"
        )
        self.amount_entry.pack(fill="x", ipady=6)
        self.amount_entry.bind("<Return>", lambda e: self.convert())

        # From / To Currency Dropdown Frame
        dropdowns_frame = tk.Frame(self.root, bg="#1e1e2e")
        dropdowns_frame.pack(fill="x", padx=30, pady=10)

        currencies = list(EXCHANGE_RATES.keys())

        # From Currency
        from_frame = tk.Frame(dropdowns_frame, bg="#1e1e2e")
        from_frame.pack(side="left", fill="x", expand=True, padx=(0, 10))
        tk.Label(from_frame, text="From:", font=("Arial", 10), bg="#1e1e2e", fg="#cdd6f4").pack(anchor="w", pady=(0, 2))
        
        self.from_var = tk.StringVar(value="USD")
        self.from_dropdown = ttk.Combobox(from_frame, textvariable=self.from_var, values=currencies, state="readonly", font=("Arial", 10))
        self.from_dropdown.pack(fill="x", ipady=3)

        # To Currency
        to_frame = tk.Frame(dropdowns_frame, bg="#1e1e2e")
        to_frame.pack(side="right", fill="x", expand=True, padx=(10, 0))
        tk.Label(to_frame, text="To:", font=("Arial", 10), bg="#1e1e2e", fg="#cdd6f4").pack(anchor="w", pady=(0, 2))
        
        self.to_var = tk.StringVar(value="EUR")
        self.to_dropdown = ttk.Combobox(to_frame, textvariable=self.to_var, values=currencies, state="readonly", font=("Arial", 10))
        self.to_dropdown.pack(fill="x", ipady=3)

        # Convert Button
        convert_btn = tk.Button(
            self.root,
            text="Convert Currency",
            font=("Arial", 12, "bold"),
            bg="#89b4fa",
            fg="#11111b",
            activebackground="#74c7ec",
            bd=0,
            pady=8,
            cursor="hand2",
            command=self.convert
        )
        convert_btn.pack(fill="x", padx=30, pady=20)

        # Result Display Label
        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 14, "bold"),
            bg="#1e1e2e",
            fg="#a6e3a1"
        )
        self.result_label.pack(pady=5)

    def convert(self):
        """Calculates and displays the converted currency amount."""
        amount_str = self.amount_entry.get().strip()
        if not amount_str:
            messagebox.showwarning("Input Required", "Please enter an amount to convert!")
            return

        try:
            amount = float(amount_str)
            if amount < 0:
                messagebox.showwarning("Invalid Amount", "Amount cannot be negative.")
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")
            return

        from_curr = self.from_var.get()
        to_curr = self.to_var.get()

        # Conversion formula using USD as standard intermediary base
        # amount_in_usd = amount / rate_from
        # final_amount = amount_in_usd * rate_to
        amount_in_usd = amount / EXCHANGE_RATES[from_curr]
        result = amount_in_usd * EXCHANGE_RATES[to_curr]

        # Format output neatly with 2 decimal places
        self.result_label.config(text=f"{amount:,.2f} {from_curr} = {result:,.2f} {to_curr}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()