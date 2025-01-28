import tkinter as tk
from tkinter import messagebox
from db_utils import execute_query, execute_non_query

class PhysicianManagementForm(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.physician_listbox = tk.Listbox(self)
        self.physician_listbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.button_add = tk.Button(self, text="Add Physician", command=lambda: self.controller.show_frame("AddEditPhysicianForm"))
        self.button_add.grid(row=1, column=0, padx=10, pady=10)

        self.button_edit = tk.Button(self, text="Edit Physician", command=self.edit_physician)
        self.button_edit.grid(row=1, column=1, padx=10, pady=10)

        self.button_delete = tk.Button(self, text="Delete Physician", command=self.delete_physician)
        self.button_delete.grid(row=1, column=2, padx=10, pady=10)

        self.load_physicians()

    def load_physicians(self):
        self.physician_listbox.delete(0, tk.END)
        query = "SELECT physicianID, name FROM physician"
        physicians = execute_query(query)
        for physician in physicians:
            self.physician_listbox.insert(tk.END, f"{physician[0]} - {physician[1]}")

    def edit_physician(self):
        selected = self.physician_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No physician selected")
            return
        physician_id = self.physician_listbox.get(selected).split(" - ")[0]
        self.controller.frames["AddEditPhysicianForm"].load_physician(physician_id)
        self.controller.show_frame("AddEditPhysicianForm")

    def delete_physician(self):
        selected = self.physician_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No physician selected")
            return
        physician_id = self.physician_listbox.get(selected).split(" - ")[0]
        query = "DELETE FROM physicians WHERE physician_id = :1"
        execute_non_query(query, (physician_id,))
        self.load_physicians()

if __name__ == "__main__":
    root = tk.Tk()
    frame = PhysicianManagementForm(root, None)
    frame.pack()
    root.mainloop()
