import tkinter as tk
from tkinter import messagebox
from db_utils import execute_non_query, execute_query

class AddEditPhysicianForm(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.physician_id = None
        self.create_widgets()

    def create_widgets(self):
        self.label_name = tk.Label(self, text="Physician Name")
        self.label_name.grid(row=0, column=0, padx=10, pady=10)

        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.button_save = tk.Button(self, text="Save", command=self.save_physician)
        self.button_save.grid(row=1, column=0, columnspan=2, pady=10)

        self.button_cancel = tk.Button(self, text="Cancel", command=lambda: self.controller.show_frame("PhysicianManagementForm"))
        self.button_cancel.grid(row=2, column=0, columnspan=2, pady=10)

    def load_physician(self, physician_id):
        self.physician_id = physician_id
        query = "SELECT physician_name FROM physicians WHERE physician_id = :1"
        physician = execute_query(query, (physician_id,))
        if physician:
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, physician[0][0])

    def save_physician(self):
        name = self.entry_name.get()
        if self.physician_id:
            query = "UPDATE physicians SET physician_name = :1 WHERE physician_id = :2"
            execute_non_query(query, (name, self.physician_id))
        else:
            query = "INSERT INTO physicians (physician_name) VALUES (:1)"
            execute_non_query(query, (name,))
        self.controller.show_frame("PhysicianManagementForm")
        self.controller.frames["PhysicianManagementForm"].load_physicians()

if __name__ == "__main__":
    root = tk.Tk()
    frame = AddEditPhysicianForm(root, None)
    frame.pack()
    root.mainloop()
