import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

FILENAME = "contacts.json"

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.geometry("680x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.contacts = []

        self.setup_ui()
        self.load_contacts()

    def setup_ui(self):
        # Header Title
        title_label = tk.Label(
            self.root,
            text="Contact Management System",
            font=("Arial", 18, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        )
        title_label.pack(pady=(15, 10))

        # Main Container Frame
        main_frame = tk.Frame(self.root, bg="#1e1e2e")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Left Frame: Input Form
        form_frame = tk.LabelFrame(
            main_frame,
            text=" Contact Details ",
            font=("Arial", 11, "bold"),
            bg="#1e1e2e",
            fg="#a6adc8",
            padx=10,
            pady=10
        )
        form_frame.pack(side="left", fill="y", padx=(0, 15))

        # Name Field
        tk.Label(form_frame, text="Name:", font=("Arial", 10), bg="#1e1e2e", fg="#cdd6f4").pack(anchor="w", pady=(5, 0))
        self.name_entry = tk.Entry(form_frame, font=("Arial", 11), bg="#313244", fg="#f5e0dc", insertbackground="white", relief="flat")
        self.name_entry.pack(fill="x", ipady=4, pady=(2, 10))

        # Phone Field
        tk.Label(form_frame, text="Phone Number:", font=("Arial", 10), bg="#1e1e2e", fg="#cdd6f4").pack(anchor="w")
        self.phone_entry = tk.Entry(form_frame, font=("Arial", 11), bg="#313244", fg="#f5e0dc", insertbackground="white", relief="flat")
        self.phone_entry.pack(fill="x", ipady=4, pady=(2, 10))

        # Email Field
        tk.Label(form_frame, text="Email Address:", font=("Arial", 10), bg="#1e1e2e", fg="#cdd6f4").pack(anchor="w")
        self.email_entry = tk.Entry(form_frame, font=("Arial", 11), bg="#313244", fg="#f5e0dc", insertbackground="white", relief="flat")
        self.email_entry.pack(fill="x", ipady=4, pady=(2, 15))

        # Form Buttons
        btn_add = tk.Button(form_frame, text="Add Contact", font=("Arial", 10, "bold"), bg="#a6e3a1", fg="#11111b", bd=0, pady=6, cursor="hand2", command=self.add_contact)
        btn_add.pack(fill="x", pady=4)

        btn_update = tk.Button(form_frame, text="Update Selected", font=("Arial", 10, "bold"), bg="#89b4fa", fg="#11111b", bd=0, pady=6, cursor="hand2", command=self.update_contact)
        btn_update.pack(fill="x", pady=4)

        btn_clear = tk.Button(form_frame, text="Clear Form", font=("Arial", 10, "bold"), bg="#f9e2af", fg="#11111b", bd=0, pady=6, cursor="hand2", command=self.clear_form)
        btn_clear.pack(fill="x", pady=4)

        # Right Frame: Search & Treeview List
        right_frame = tk.Frame(main_frame, bg="#1e1e2e")
        right_frame.pack(side="right", fill="both", expand=True)

        # Search Bar
        search_frame = tk.Frame(right_frame, bg="#1e1e2e")
        search_frame.pack(fill="x", pady=(0, 10))

        tk.Label(search_frame, text="Search:", font=("Arial", 10), bg="#1e1e2e", fg="#cdd6f4").pack(side="left", padx=(0, 5))
        self.search_entry = tk.Entry(search_frame, font=("Arial", 11), bg="#313244", fg="#f5e0dc", insertbackground="white", relief="flat")
        self.search_entry.pack(side="left", fill="x", expand=True, ipady=3, padx=(0, 5))
        self.search_entry.bind("<KeyRelease>", self.search_contacts)

        # Treeview (Table) for Contacts
        columns = ("Name", "Phone", "Email")
        self.tree = ttk.Treeview(right_frame, columns=columns, show="headings", selectmode="browse")
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=110, anchor="w")

        self.tree.pack(side="top", fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

        # Scrollbar for Treeview
        scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=self.tree.yview)
        # Place scrollbar cleanly or let tree handle it packing side-by-side if preferred.

        # Bottom Action Bar (Delete)
        bottom_frame = tk.Frame(self.root, bg="#1e1e2e")
        bottom_frame.pack(fill="x", padx=20, pady=(0, 15))

        btn_delete = tk.Button(bottom_frame, text="Delete Selected Contact", font=("Arial", 10, "bold"), bg="#f38ba8", fg="#11111b", bd=0, pady=6, cursor="hand2", command=self.delete_contact)
        btn_delete.pack(fill="x")

    def refresh_table(self, data=None):
        """Refreshes the table display with contact data."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        contacts_to_show = data if data is not None else self.contacts
        for contact in contacts_to_show:
            self.tree.insert("", "end", values=(contact["name"], contact["phone"], contact["email"]))

    def add_contact(self):
        """Adds a new contact to the database."""
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()

        if not name or not phone:
            messagebox.showwarning("Validation Error", "Name and Phone Number are required fields!")
            return

        self.contacts.append({"name": name, "phone": phone, "email": email})
        self.save_contacts()
        self.refresh_table()
        self.clear_form()
        messagebox.showinfo("Success", f"Contact '{name}' added successfully!")

    def update_contact(self):
        """Updates the details of the selected contact."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Required", "Please select a contact from the list to update!")
            return

        # Find original index based on tree values
        item_values = self.tree.item(selected_item, "values")
        
        for index, contact in enumerate(self.contacts):
            if contact["name"] == item_values[0] and contact["phone"] == item_values[1]:
                new_name = self.name_entry.get().strip()
                new_phone = self.phone_entry.get().strip()
                new_email = self.email_entry.get().strip()

                if not new_name or not new_phone:
                    messagebox.showwarning("Validation Error", "Name and Phone Number cannot be empty!")
                    return

                self.contacts[index] = {"name": new_name, "phone": new_phone, "email": new_email}
                self.save_contacts()
                self.refresh_table()
                self.clear_form()
                messagebox.showinfo("Success", "Contact updated successfully!")
                break

    def delete_contact(self):
        """Deletes the selected contact."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Required", "Please select a contact to delete!")
            return

        item_values = self.tree.item(selected_item, "values")
        
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {item_values[0]}?"):
            self.contacts = [c for c in self.contacts if not (c["name"] == item_values[0] and c["phone"] == item_values[1])]
            self.save_contacts()
            self.refresh_table()
            self.clear_form()

    def on_row_select(self, event):
        """Loads selected table row data into form inputs for easy editing."""
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item, "values")
            self.clear_form()
            self.name_entry.insert(0, item_values[0])
            self.phone_entry.insert(0, item_values[1])
            self.email_entry.insert(0, item_values[2])

    def search_contacts(self, event):
        """Filters contacts dynamically as you type in the search bar."""
        query = self.search_entry.get().strip().lower()
        if not query:
            self.refresh_table()
            return

        filtered = [
            c for c in self.contacts 
            if query in c["name"].lower() or query in c["phone"] or query in c["email"].lower()
        ]
        self.refresh_table(filtered)

    def clear_form(self):
        """Clears all text entry fields."""
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def save_contacts(self):
        """Saves current contact entries to a local JSON file."""
        try:
            with open(FILENAME, "w") as file:
                json.dump(self.contacts, file, indent=4)
        except Exception as e:
            print(f"Error saving contacts: {e}")

    def load_contacts(self):
        """Loads saved contacts from the local JSON file on startup."""
        if os.path.exists(FILENAME):
            try:
                with open(FILENAME, "r") as file:
                    self.contacts = json.load(file)
                self.refresh_table()
            except Exception as e:
                print(f"Error loading contacts: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()