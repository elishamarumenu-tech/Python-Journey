# Python Unit Converter

A simple and user-friendly **Unit Converter desktop application** built using Python and Tkinter. It allows users to convert values between different units of length, weight, and temperature through an interactive graphical interface.

## Features

- **Three Conversion Categories**
  - Length
  - Weight
  - Temperature
- **Length Conversion:** Meters, Kilometers, Centimeters, Millimeters, Miles, Feet, and Inches.
- **Weight Conversion:** Grams, Kilograms, Milligrams, Pounds, and Ounces.
- **Temperature Conversion:** Celsius, Fahrenheit, and Kelvin.
- **Dynamic Unit Selection:** Unit dropdowns update automatically when the category changes.
- **Input Validation:** Handles empty and invalid numeric inputs.
- **Instant Conversion:** Displays the converted result in the application.
- **Keyboard Support:** Press Enter to convert.
- **Modern GUI:** Dark-themed interface with simple controls.

## Technologies Used

- **Python 3**
- **Tkinter** – GUI development
- **ttk (Themed Tkinter)** – Dropdown menus
- **Messagebox** – Input error and warning messages

## Project Structure

```text
Python-Unit-Converter/
│
├── unit_converter.py
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
python unit_converter.py
```

**Note:** Python 3 must be installed. Tkinter is included with most standard Python installations.

## How to Use

1. Open the Unit Converter application.
2. Select a category: Length, Weight, or Temperature.
3. Enter the value you want to convert.
4. Select the source unit in the **From** dropdown.
5. Select the target unit in the **To** dropdown.
6. Click the **Convert** button or press Enter.
7. View the converted result on the screen.

## Conversion Examples

| Category | From | To | Example |
|---|---|---|---|
| Length | Kilometers | Meters | 2 km = 2000 m |
| Length | Meters | Feet | 1 m ≈ 3.2808 ft |
| Weight | Kilograms | Grams | 5 kg = 5000 g |
| Weight | Pounds | Kilograms | 2 lb ≈ 0.9072 kg |
| Temperature | Celsius | Fahrenheit | 0°C = 32°F |
| Temperature | Celsius | Kelvin | 25°C = 298.15 K |

## Main Functions

| Function | Description |
|---|---|
| `setup_ui()` | Creates the graphical user interface. |
| `update_units()` | Updates available units based on the selected category. |
| `convert()` | Performs the selected unit conversion and displays the result. |

## Concepts Learned

- Python Object-Oriented Programming (OOP)
- Tkinter GUI development
- Labels, buttons, entry fields, and dropdown menus
- Event handling and keyboard bindings
- Functions and conditional statements
- Dictionaries for conversion factors
- Mathematical calculations and formulas
- Exception handling using `try-except`
- Input validation and output formatting

## Future Improvements

- Add area, volume, speed, and time conversions.
- Add a conversion history feature.
- Add a Swap Units button.
- Improve the interface with additional themes.
- Add copy-result functionality.
- Support more measurement units.

## Author

**JOY ELISHA**

GitHub: [elishamarumenu-tech](https://github.com/elishamarumenu-tech)

---

If you find this project useful, consider giving the repository a ⭐!

