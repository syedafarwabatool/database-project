import tkinter as tk
from tkinter import messagebox
from db_utils import execute_non_query, execute_query

class AddEditInfectionForm(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.infection_id = None
        self.create_widgets()

    def create_widgets(self):
        self.label_name = tk.Label(self, text="Infection Name")
        self.label_name.grid(row=0, column=0, padx=10, pady=10)

        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.button_save = tk.Button(self, text="Save", command=self.save_infection)
        self.button_save.grid(row=1, column=0, columnspan=2, pady=10)

        self.button_cancel = tk.Button(self, text="Cancel", command=lambda: self.controller.show_frame("InfectionManagementForm"))
        self.button_cancel.grid(row=2, column=0, columnspan=2, pady=10)

    def load_infection(self, infection_id):
        self.infection_id = infection_id
        query = "SELECT infection_name FROM infections WHERE infection_id = :1"
        infection = execute_query(query, (infection_id,))
        if infection:
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, infection[0][0])

    def save_infection(self):
        name = self.entry_name.get()
        if self.infection_id:
            query = "UPDATE infections SET infection_name = :1 WHERE infection_id = :2"
            execute_non_query(query, (name, self.infection_id))
        else:
            query = "INSERT INTO infections (infection_name) VALUES (:1)"
            execute_non_query(query, (name,))
        self.controller.show_frame("InfectionManagementForm")
        self.controller.frames["InfectionManagementForm"].load_infections()

if __name__ == "__main__":
    root = tk.Tk()
    frame = AddEditInfectionForm(root, None)
    frame.pack()
    root.mainloop()
