import tkinter as tk
from tkinter import messagebox
from db_utils import execute_query, execute_non_query

class CauseManagementForm(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the heading
        heading_frame = tk.Frame(self)
        heading_frame.grid(row=0, column=0, columnspan=1, padx=5, pady=(5, 0))
        
        # Add headings as labels
        headings = ["CauseType"]
        for col_num, heading in enumerate(headings):
            label = tk.Label(heading_frame, text=heading, borderwidth=2, relief="groove", width=10)
            label.grid(row=0, column=col_num, padx=1, pady=1)

        self.cause_listbox = tk.Listbox(self)
        self.cause_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

          # Configure the Listbox frame grid
        # self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)


        # self.button_add = tk.Button(self, text="Add Cause", command=lambda: self.controller.show_frame("AddEditCauseForm"))
        # self.button_add.grid(row=1, column=0, padx=10, pady=10)

        # self.button_edit = tk.Button(self, text="Edit Cause", command=self.edit_cause)
        # self.button_edit.grid(row=1, column=1, padx=10, pady=10)

        # self.button_delete = tk.Button(self, text="Delete Cause", command=self.delete_cause)
        # self.button_delete.grid(row=1, column=2, padx=10, pady=10)

        self.button_delete = tk.Button(self, text="Manage Assignment", command=lambda: self.controller.show_frame("AssignedManagementForm"))
        self.button_delete.grid(row=2, column=0, padx=10, pady=10)

        self.load_causes()

    def load_causes(self):
        self.cause_listbox.delete(0, tk.END)
        query = "SELECT causeType FROM Cause"
        causes = execute_query(query)
        for cause in causes:
            self.cause_listbox.insert(tk.END, f"{cause[0]}")

    def edit_cause(self):
        selected = self.cause_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No cause selected")
            return
        cause_id = self.cause_listbox.get(selected).split(" - ")[0]
        self.controller.frames["AddEditCauseForm"].load_cause(cause_id)
        self.controller.show_frame("AddEditCauseForm")

    def delete_cause(self):
        selected = self.cause_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No cause selected")
            return
        cause_id = self.cause_listbox.get(selected).split(" - ")[0]
        query = "DELETE FROM cause WHERE causeType = ?"
        execute_non_query(query, (cause_id,))
        self.load_causes()

if __name__ == "__main__":
    root = tk.Tk()
    frame = CauseManagementForm(root, None)
    frame.pack()
    root.mainloop()
