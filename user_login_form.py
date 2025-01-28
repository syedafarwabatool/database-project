import tkinter as tk
from tkinter import messagebox
from db_utils import execute_query

class UserLoginForm(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
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

        self.button_login = tk.Button(self, text="Login", command=self.login)
        self.button_login.grid(row=2, column=0, columnspan=2, pady=10)

        self.button_register = tk.Button(self, text="Register", command=lambda: self.controller.show_frame("RegistrationForm"))
        self.button_register.grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        query = "SELECT * FROM Userlogin WHERE username = ? AND password = ?"
        result = execute_query(query, (username, password))
        if result:
            self.controller.show_frame("PatientManagementForm")
        else:
            messagebox.showerror("Error", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    frame = UserLoginForm(root, None)
    frame.pack()
    root.mainloop()
