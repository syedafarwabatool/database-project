import tkinter as tk
from tkinter import messagebox
from db_utils import execute_query, execute_non_query

class EtiologyManagementForm(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the heading
        heading_frame = tk.Frame(self)
        heading_frame.grid(row=0, column=0, columnspan=1, padx=5, pady=(5, 0))
        
        # Add headings as labels
        headings = ["EtiologyID", "InfectionID","Cause Type"]
        for col_num, heading in enumerate(headings):
            label = tk.Label(heading_frame, text=heading, borderwidth=2, relief="groove", width=10)
            label.grid(row=0, column=col_num, padx=1, pady=1)

        self.etiology_listbox = tk.Listbox(self, width= 30)
        self.etiology_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

          # Configure the Listbox frame grid
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)


        self.button_add = tk.Button(self, text="Add Etiology", command=lambda: self.controller.show_frame("AddEditEtiologyForm"))
        self.button_add.grid(row=2, column=0, padx=10, pady=10)

        self.button_edit = tk.Button(self, text="Edit Etiology", command=self.edit_etiology)
        self.button_edit.grid(row=3, column=0, padx=10, pady=10)

        self.button_delete = tk.Button(self, text="Delete Etiology", command=self.delete_etiology)
        self.button_delete.grid(row=4, column=0, padx=10, pady=10)

        self.button_delete = tk.Button(self, text="Manage Cause", command=lambda: self.controller.show_frame("CauseManagementForm"))
        self.button_delete.grid(row=5, column=0, padx=10, pady=10)

        self.load_etiologies()

    def load_etiologies(self):
        self.etiology_listbox.delete(0, tk.END)
        query = "SELECT * FROM Etiology"
        etiologies = execute_query(query)
        for etiology in etiologies:
            self.etiology_listbox.insert(tk.END, f"{etiology[0]} - {etiology[1]} - {etiology[2]}")

    def edit_etiology(self):
        selected = self.etiology_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No etiology selected")
            return
        etiology_id = self.etiology_listbox.get(selected).split(" - ")[0]
        self.controller.frames["AddEditEtiologyForm"].load_etiology(etiology_id)
        self.controller.show_frame("AddEditEtiologyForm")

    def delete_etiology(self):
        selected = self.etiology_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No etiology selected")
            return
        etiology_id = self.etiology_listbox.get(selected).split(" - ")[0]
        query = "DELETE FROM Etiology WHERE etiologyID = ?"
        execute_non_query(query, (etiology_id,))
        self.load_etiologies()

if __name__ == "__main__":
    root = tk.Tk()
    frame = EtiologyManagementForm(root, None)
    frame.pack()
    root.mainloop()
