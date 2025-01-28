import tkinter as tk
from tkinter import messagebox
from db_utils import execute_query, execute_non_query

class InfectionManagementForm(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.infection_listbox = tk.Listbox(self)
        self.infection_listbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.button_add = tk.Button(self, text="Add Infection", command=lambda: self.controller.show_frame("AddEditInfectionForm"))
        self.button_add.grid(row=1, column=0, padx=10, pady=10)

        self.button_edit = tk.Button(self, text="Edit Infection", command=self.edit_infection)
        self.button_edit.grid(row=1, column=1, padx=10, pady=10)

        self.button_delete = tk.Button(self, text="Delete Infection", command=self.delete_infection)
        self.button_delete.grid(row=1, column=2, padx=10, pady=10)

        self.load_infections()

    def load_infections(self):
        self.infection_listbox.delete(0, tk.END)
        query = "SELECT infectionID, Symptoms FROM pinkeyeinfection"
        infections = execute_query(query)
        for infection in infections:
            self.infection_listbox.insert(tk.END, f"{infection[0]} - {infection[1]}")

    def edit_infection(self):
        selected = self.infection_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No infection selected")
            return
        infection_id = self.infection_listbox.get(selected).split(" - ")[0]
        self.controller.frames["AddEditInfectionForm"].load_infection(infection_id)
        self.controller.show_frame("AddEditInfectionForm")

    def delete_infection(self):
        selected = self.infection_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No infection selected")
            return
        infection_id = self.infection_listbox.get(selected).split(" - ")[0]
        query = "DELETE FROM infections WHERE infection_id = :1"
        execute_non_query(query, (infection_id,))
        self.load_infections()

if __name__ == "__main__":
    root = tk.Tk()
    frame = InfectionManagementForm(root, None)
    frame.pack()
    root.mainloop()
