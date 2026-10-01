# 📇 Contact Management System

A desktop-based Contact Management System built using **Python and Tkinter**. The application allows users to add, update, search, and delete contacts while automatically storing contact information in a local JSON file.

## 📌 Project Description

The Python Contact Management System provides a simple graphical interface for managing personal contact information.

Users can store a contact's **name, phone number, and email address**, search contacts dynamically, update existing information, and delete unwanted contacts. All contact data is saved locally in a JSON file so that it can be loaded again when the application starts.

## ✨ Features

* Add new contacts.
* Update existing contacts.
* Delete selected contacts.
* Search contacts dynamically.
* Store name, phone number, and email.
* Select a contact to automatically load its details into the form.
* Save contacts using JSON.
* Automatically load saved contacts when the application starts.
* Input validation for required fields.
* Delete confirmation dialog.
* Success and warning message boxes.
* Table-based contact display using Tkinter Treeview.
* Clean dark-themed GUI.

## 🛠️ Technologies Used

| Technology | Purpose                                 |
| ---------- | --------------------------------------- |
| Python     | Core programming language               |
| Tkinter    | GUI development                         |
| ttk        | Treeview table and scrollbar            |
| JSON       | Local contact storage                   |
| OS         | Checks whether the JSON file exists     |
| OOP        | Organizes the application using a class |

## 📂 Project Structure

```text
Contact-Management-System/
│
├── contact_manager.py
├── contacts.json
└── README.md
```

**Note:** `contacts.json` is automatically created when contacts are saved.

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Tkinter, JSON, and OS are available with standard Python installations.

### 2. Run the application

Open a terminal in the project folder and execute:

```bash
python contact_manager.py
```

The Contact Management System window will open.

## 🎮 How to Use

### ➕ Add Contact

1. Enter the contact's name.
2. Enter the phone number.
3. Enter the email address.
4. Click **Add Contact**.

Name and phone number are required fields.

### ✏️ Update Contact

1. Select a contact from the table.
2. The contact details will automatically appear in the form.
3. Edit the required information.
4. Click **Update Selected**.

### 🔍 Search Contact

Type a name, phone number, or email address into the search box.

The table automatically filters the contacts as you type.

### 🗑️ Delete Contact

1. Select a contact.
2. Click **Delete Selected Contact**.
3. Confirm the deletion.

### 🧹 Clear Form

Click **Clear Form** to remove the current information from the input fields.

## 💾 Data Storage

Contact information is stored locally in:

```text
contacts.json
```

Example:

```json
[
    {
        "name": "John",
        "phone": "9876543210",
        "email": "john@example.com"
    },
    {
        "name": "Sarah",
        "phone": "9123456780",
        "email": "sarah@example.com"
    }
]
```

Each contact contains:

* `name` – Contact name.
* `phone` – Phone number.
* `email` – Email address.

## 🧩 Main Functions

| Function            | Purpose                                       |
| ------------------- | --------------------------------------------- |
| `setup_ui()`        | Creates the graphical user interface.         |
| `refresh_table()`   | Displays contact data in the table.           |
| `add_contact()`     | Adds a new contact.                           |
| `update_contact()`  | Updates an existing contact.                  |
| `delete_contact()`  | Deletes a selected contact.                   |
| `on_row_select()`   | Loads selected contact details into the form. |
| `search_contacts()` | Filters contacts while typing.                |
| `clear_form()`      | Clears all input fields.                      |
| `save_contacts()`   | Saves contacts to the JSON file.              |
| `load_contacts()`   | Loads saved contacts when the program starts. |

## 🧠 Concepts Learned

Through this project, I practiced:

* Python classes and objects.
* Object-oriented programming.
* Tkinter GUI development.
* `Entry`, `Button`, `Label`, `Frame`, and `Treeview` widgets.
* Event handling and callback functions.
* Lists and dictionaries.
* JSON file handling.
* Reading and writing files.
* Searching and filtering data.
* Input validation.
* Exception handling.
* CRUD operations:

  * **Create** – Add contacts.
  * **Read** – View and search contacts.
  * **Update** – Modify contacts.
  * **Delete** – Remove contacts.

## 🔄 Application Workflow

```text
Start Application
       ↓
Load contacts.json
       ↓
Display Contacts
       ↓
┌─────────────────────────┐
│ Add / Search / Update   │
│ Delete / Clear Form     │
└─────────────────────────┘
       ↓
Save Changes
       ↓
Update contacts.json
```

## 🚀 Future Improvements

* Add phone number validation.
* Add email format validation.
* Prevent duplicate contacts.
* Add contact categories.
* Add profile pictures.
* Add sorting by name or phone number.
* Add import/export functionality.
* Add CSV and Excel support.
* Add dark/light theme switching.
* Add database support using SQLite.
* Add contact backup and restore.

## 👨‍💻 Author

**JOY ELISHA**

Python Journey – Learning Python through practical projects.

---

⭐ If you like this project, consider giving the repository a star!
