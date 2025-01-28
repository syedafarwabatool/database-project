import tkinter as tk
from tkinter import messagebox
from db_utils import execute_non_query

class RegistrationForm(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.label_username = tk.Label(self, text="Username")
        self.label_username.grid(row=0, column=0, padx=10, pady=10)

        self.entry_username = tk.Entry(self)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        self.label_password = tk.Label(self, text="Password")
        self.label_password.grid(row=1, column=0, padx=10, pady=10)

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.label_confirm_password = tk.Label(self, text="Confirm Password")
        self.label_confirm_password.grid(row=2, column=0, padx=10, pady=10)

        self.entry_confirm_password = tk.Entry(self, show="*")
        self.entry_confirm_password.grid(row=2, column=1, padx=10, pady=10)

        self.button_register = tk.Button(self, text="Register", command=self.register)
        self.button_register.grid(row=3, column=0, columnspan=2, pady=10)

        self.button_cancel = tk.Button(self, text="Cancel", command=lambda: self.controller.show_frame("UserLoginForm"))
        self.button_cancel.grid(row=4, column=0, columnspan=2, pady=10)

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return
        query = "INSERT INTO users (username, password) VALUES (:1, :2)"
        try:
            execute_non_query(query, (username, password))
            messagebox.showinfo("Success", "User registered successfully")
            self.controller.show_frame("UserLoginForm")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    frame = RegistrationForm(root, None)
    frame.pack()
    root.mainloop()
