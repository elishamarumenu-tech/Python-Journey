# Python Currency Converter

A simple and interactive **Currency Converter desktop application** built using Python and Tkinter. It allows users to convert amounts between different international currencies using predefined exchange rates, with USD (US Dollar) as the base currency.

## Features

- **9 Supported Currencies:**
  - USD – US Dollar
  - EUR – Euro
  - GBP – British Pound
  - INR – Indian Rupee
  - JPY – Japanese Yen
  - CAD – Canadian Dollar
  - AUD – Australian Dollar
  - CHF – Swiss Franc
  - CNY – Chinese Yuan
- **Currency Selection:** Choose source and target currencies using dropdown menus.
- **Amount Validation:** Handles empty, invalid, and negative inputs.
- **Instant Conversion:** Displays the converted amount immediately.
- **Keyboard Support:** Press Enter to convert.
- **Formatted Results:** Displays amounts with commas and two decimal places.
- **Modern GUI:** Simple dark-themed interface.

## Technologies Used

- **Python 3**
- **Tkinter** – GUI development
- **ttk (Themed Tkinter)** – Currency dropdown menus
- **Messagebox** – Input validation messages
- **Dictionary** – Stores exchange rates

## Project Structure

```text
Python-Currency-Converter/
│
├── currency_converter.py
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
python currency_converter.py
```

**Note:** Python 3 must be installed. Tkinter is included with most standard Python installations.

## How to Use

1. Open the Currency Converter application.
2. Enter the amount you want to convert.
3. Select the source currency in the **From** dropdown.
4. Select the target currency in the **To** dropdown.
5. Click the **Convert Currency** button or press Enter.
6. View the converted amount on the screen.

## Conversion Formula

The application uses USD as the standard intermediate base currency.

**Step 1: Convert the source amount into USD**

```text
Amount in USD = Amount / Source Currency Rate
```

**Step 2: Convert USD into the target currency**

```text
Final Amount = Amount in USD × Target Currency Rate
```

### Example

Suppose you want to convert 100 USD into INR.

Using the predefined exchange rates:

```text
USD = 1.00
INR = 83.12

100 USD = 8,312 INR
```

## Main Components

| Component | Description |
|---|---|
| `EXCHANGE_RATES` | Stores predefined currency exchange rates relative to USD. |
| `CurrencyConverterApp` | Main application class. |
| `setup_ui()` | Creates the graphical user interface. |
| `convert()` | Validates the amount and performs currency conversion. |

## Concepts Learned

- Python Object-Oriented Programming (OOP)
- Tkinter GUI development
- Labels, buttons, entry fields, and dropdown menus
- Python dictionaries and key-value pairs
- Currency conversion formulas
- Mathematical calculations
- Input validation
- Exception handling using `try-except`
- Event handling and keyboard bindings
- Number formatting

## Important Note

The exchange rates used in this project are **predefined sample rates** stored in the `EXCHANGE_RATES` dictionary. They are not fetched from a live financial API and may not reflect current market rates. This application is intended for learning and demonstration purposes, not financial transactions.

## Future Improvements

- Integrate a live currency exchange rate API.
- Add more international currencies.
- Add a Swap Currencies button.
- Display conversion history.
- Add date and time of conversion.
- Support offline conversion using saved exchange rates.
- Improve the interface with additional themes.

## Author

**JOY ELISHA**

GitHub: [elishamarumenu-tech](https://github.com/elishamarumenu-tech)

---

If you find this project useful, consider giving the repository a ⭐!

