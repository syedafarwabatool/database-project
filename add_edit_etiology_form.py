import tkinter as tk
from tkinter import messagebox
from db_utils import execute_non_query, execute_query

class AddEditEtiologyForm(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.etiology_id = None
        self.create_widgets()

    def create_widgets(self):
        self.label_EID = tk.Label(self, text="Etiology ID")
        self.label_EID.grid(row=0, column=0, padx=10, pady=10)

        self.entry_EID = tk.Entry(self)
        self.entry_EID.grid(row=0, column=1, padx=10, pady=10)

        self.label_IID = tk.Label(self, text="Infection ID")
        self.label_IID.grid(row=1, column=0, padx=10, pady=10)

        self.entry_IID = tk.Entry(self)
        self.entry_IID.grid(row=1, column=1, padx=10, pady=10)

        self.label_cause_type = tk.Label(self, text="Cause Type")
        self.label_cause_type.grid(row=2, column=0, padx=10, pady=10)

        self.entry_cause_type = tk.Entry(self)
        self.entry_cause_type.grid(row=2, column=1, padx=10, pady=10)

        self.button_save = tk.Button(self, text="Save", command=self.save_etiology)
        self.button_save.grid(row=3, column=0, columnspan=2, pady=10)

        self.button_cancel = tk.Button(self, text="Cancel", command=lambda: self.controller.show_frame("EtiologyManagementForm"))
        self.button_cancel.grid(row=4, column=0, columnspan=2, pady=10)

    def load_etiology(self, etiology_id):
        self.etiology_id = etiology_id
        query = "SELECT * FROM etiology WHERE etiologyID = ?"
        etiology = execute_query(query, (etiology_id,))
        if etiology:
            self.entry_EID.delete(0, tk.END)
            self.entry_EID.insert(0, etiology[0][0])
            self.entry_IID.delete(0, tk.END)
            self.entry_IID.insert(0, etiology[0][1])
            self.entry_cause_type.delete(0, tk.END)
            self.entry_cause_type.insert(0, etiology[0][2])

    def save_etiology(self):
        EID = self.entry_EID.get()
        # IID = self.entry_IID.get()
        # cause_type = self.entry_cause_type.get()
        if self.etiology_id:
            query = "UPDATE Etiology SET etiologyID = ? WHERE etiologyID = ?"
            execute_non_query(query, (EID, self.etiology_id))
        else:
            query = "INSERT INTO Etiology (etiologyID) VALUES (?)"
            execute_non_query(query, (EID))
        self.controller.show_frame("EtiologyManagementForm")
        self.controller.frames["EtiologyManagementForm"].load_etiologies()

if __name__ == "__main__":
    root = tk.Tk()
    frame = AddEditEtiologyForm(root, None)
    frame.pack()
    root.mainloop()
