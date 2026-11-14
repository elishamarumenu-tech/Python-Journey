import tkinter as tk
from tkinter import ttk, messagebox

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Unit Converter")
        self.root.geometry("450x460")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.setup_ui()

    def setup_ui(self):
        # Header Title
        title_label = tk.Label(
            self.root,
            text="Unit Converter",
            font=("Arial", 18, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        )
        title_label.pack(pady=(20, 15))

        # Category Selection Frame
        cat_frame = tk.Frame(self.root, bg="#1e1e2e")
        cat_frame.pack(fill="x", padx=30, pady=5)

        tk.Label(cat_frame, text="Category:", font=("Arial", 11), bg="#1e1e2e", fg="#cdd6f4").pack(side="left")
        
        self.category_var = tk.StringVar(value="Length")
        self.category_dropdown = ttk.Combobox(
            cat_frame, 
            textvariable=self.category_var, 
            values=["Length", "Weight", "Temperature"],
            state="readonly",
            font=("Arial", 11)
        )
        self.category_dropdown.pack(side="right", fill="x", expand=True, padx=(10, 0))
        self.category_dropdown.bind("<<ComboboxSelected>>", self.update_units)

        # Input Value Frame
        input_frame = tk.Frame(self.root, bg="#1e1e2e")
        input_frame.pack(fill="x", padx=30, pady=10)

        tk.Label(input_frame, text="Value to Convert:", font=("Arial", 11), bg="#1e1e2e", fg="#cdd6f4").pack(anchor="w", pady=(0, 5))
        self.value_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            bg="#313244",
            fg="#f5e0dc",
            insertbackground="white",
            relief="flat"
        )
        self.value_entry.pack(fill="x", ipady=6)
        self.value_entry.bind("<Return>", lambda e: self.convert())

        # From / To Units Selection Frame
        units_frame = tk.Frame(self.root, bg="#1e1e2e")
        units_frame.pack(fill="x", padx=30, pady=10)

        # From Unit Dropdown
        from_frame = tk.Frame(units_frame, bg="#1e1e2e")
        from_frame.pack(side="left", fill="x", expand=True, padx=(0, 10))
        tk.Label(from_frame, text="From:", font=("Arial", 10), bg="#1e1e2e", fg="#cdd6f4").pack(anchor="w", pady=(0, 2))
        self.from_var = tk.StringVar()
        self.from_dropdown = ttk.Combobox(from_frame, textvariable=self.from_var, state="readonly", font=("Arial", 10))
        self.from_dropdown.pack(fill="x", ipady=3)

        # To Unit Dropdown
        to_frame = tk.Frame(units_frame, bg="#1e1e2e")
        to_frame.pack(side="right", fill="x", expand=True, padx=(10, 0))
        tk.Label(to_frame, text="To:", font=("Arial", 10), bg="#1e1e2e", fg="#cdd6f4").pack(anchor="w", pady=(0, 2))
        self.to_var = tk.StringVar()
        self.to_dropdown = ttk.Combobox(to_frame, textvariable=self.to_var, state="readonly", font=("Arial", 10))
        self.to_dropdown.pack(fill="x", ipady=3)

        # Populate initial dropdown lists
        self.update_units()

        # Convert Button
        convert_btn = tk.Button(
            self.root,
            text="Convert",
            font=("Arial", 12, "bold"),
            bg="#89b4fa",
            fg="#11111b",
            activebackground="#74c7ec",
            bd=0,
            pady=8,
            cursor="hand2",
            command=self.convert
        )
        convert_btn.pack(fill="x", padx=30, pady=15)

        # Result Display Label
        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 14, "bold"),
            bg="#1e1e2e",
            fg="#a6e3a1"
        )
        self.result_label.pack(pady=5)

    def update_units(self, event=None):
        """Updates unit options dynamically based on the selected category."""
        category = self.category_var.get()
        if category == "Length":
            units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Feet", "Inches"]
        elif category == "Weight":
            units = ["Grams", "Kilograms", "Milligrams", "Pounds", "Ounces"]
        elif category == "Temperature":
            units = ["Celsius", "Fahrenheit", "Kelvin"]
        else:
            units = []

        self.from_dropdown['values'] = units
        self.to_dropdown['values'] = units
        if units:
            self.from_dropdown.current(0)
            self.to_dropdown.current(1 if len(units) > 1 else 0)

    def convert(self):
        """Calculates and displays the converted unit value."""
        val_str = self.value_entry.get().strip()
        if not val_str:
            messagebox.showwarning("Input Required", "Please enter a value to convert!")
            return

        try:
            val = float(val_str)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric value.")
            return

        category = self.category_var.get()
        from_unit = self.from_var.get()
        to_unit = self.to_var.get()

        if from_unit == to_unit:
            self.result_label.config(text=f"Result: {val} {to_unit}")
            return

        result = 0.0

        if category == "Length":
            # Conversion base factor relative to meters
            meters_lookup = {
                "Meters": 1.0,
                "Kilometers": 1000.0,
                "Centimeters": 0.01,
                "Millimeters": 0.001,
                "Miles": 1609.344,
                "Feet": 0.3048,
                "Inches": 0.0254
            }
            val_in_meters = val * meters_lookup[from_unit]
            result = val_in_meters / meters_lookup[to_unit]

        elif category == "Weight":
            # Conversion base factor relative to grams
            grams_lookup = {
                "Grams": 1.0,
                "Kilograms": 1000.0,
                "Milligrams": 0.001,
                "Pounds": 453.59237,
                "Ounces": 28.34952
            }
            val_in_grams = val * grams_lookup[from_unit]
            result = val_in_grams / grams_lookup[to_unit]

        elif category == "Temperature":
            # Convert from_unit to Celsius intermediate step
            if from_unit == "Celsius":
                c = val
            elif from_unit == "Fahrenheit":
                c = (val - 32) * 5/9
            elif from_unit == "Kelvin":
                c = val - 273.15
            
            # Convert Celsius intermediate to target to_unit
            if to_unit == "Celsius":
                result = c
            elif to_unit == "Fahrenheit":
                result = (c * 9/5) + 32
            elif to_unit == "Kelvin":
                result = c + 273.15

        # Format output neatly, stripping redundant trailing decimal zeros
        formatted_result = f"{result:.4f}".rstrip('0').rstrip('.')
        self.result_label.config(text=f"Result: {formatted_result} {to_unit}")


if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()