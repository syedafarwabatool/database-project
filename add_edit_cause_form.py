import tkinter as tk
from tkinter import messagebox
from db_utils import execute_non_query, execute_query

class AddEditCauseForm(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.cause_id = None
        self.create_widgets()

    def create_widgets(self):
        self.label_cause_type = tk.Label(self, text="Cause Type")
        self.label_cause_type.grid(row=0, column=0, padx=10, pady=10)

        self.entry_cause_type = tk.Entry(self)
        self.entry_cause_type.grid(row=0, column=1, padx=10, pady=10)

        self.button_save = tk.Button(self, text="Save", command=self.save_cause)
        self.button_save.grid(row=1, column=0, columnspan=2, pady=10)

        self.button_cancel = tk.Button(self, text="Cancel", command=lambda: self.controller.show_frame("CauseManagementForm"))
        self.button_cancel.grid(row=2, column=0, columnspan=2, pady=10)

    def load_cause(self, cause_id):
        self.cause_id = cause_id
        query = "SELECT causeType FROM causes WHERE causeType = ?"
        cause = execute_query(query, (cause_id,))
        if cause:
            self.entry_cause_type.delete(0, tk.END)
            self.entry_cause_type.insert(0, cause[0][0])

    def save_cause(self):
        cause_name = self.entry_cause_type.get()
        if self.cause_id:
            query = "UPDATE cause SET causeType = ? WHERE causeType = ?"
            execute_non_query(query, (cause_name, self.cause_id))
        else:
            query = "INSERT INTO cause (causeType) VALUES (?)"
            execute_non_query(query, (cause_name,))
        self.controller.show_frame("CauseManagementForm")
        self.controller.frames["CauseManagementForm"].load_causes()

if __name__ == "__main__":
    root = tk.Tk()
    frame = AddEditCauseForm(root, None)
    frame.pack()
    root.mainloop()
