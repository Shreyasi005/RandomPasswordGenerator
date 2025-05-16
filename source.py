import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # pip install pyperclip


class PasswordGeneratorApp: 
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("400x400")

        # Widgets
        tk.Label(root, text="Password Length:").pack()
        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        # Checkboxes for character types
        self.include_upper = tk.BooleanVar(value=True)
        self.include_lower = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Include Uppercase", variable=self.include_upper).pack()
        tk.Checkbutton(root, text="Include Lowercase", variable=self.include_lower).pack()
        tk.Checkbutton(root, text="Include Digits", variable=self.include_digits).pack()
        tk.Checkbutton(root, text="Include Symbols", variable=self.include_symbols).pack()

        tk.Label(root, text="Exclude Characters:").pack()
        self.exclude_entry = tk.Entry(root)
        self.exclude_entry.pack()

        self.password_display = tk.Entry(root, width=50)
        self.password_display.pack(pady=10)

        tk.Button(root, text="Generate Password", command=self.generate_password).pack()
        tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard).pack()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            exclude_chars = set(self.exclude_entry.get())

            if length <= 0:
                raise ValueError("Length must be positive")

            char_pool = ""
            if self.include_upper.get():
                char_pool += string.ascii_uppercase
            if self.include_lower.get():
                char_pool += string.ascii_lowercase
            if self.include_digits.get():
                char_pool += string.digits
            if self.include_symbols.get():
                char_pool += string.punctuation

            # Remove excluded characters
            char_pool = ''.join(c for c in char_pool if c not in exclude_chars)

            if not char_pool:
                raise ValueError("No valid characters available for password generation.")

            password = ''.join(random.choice(char_pool) for _ in range(length))
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def copy_to_clipboard(self):
        password = self.password_display.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy!")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
