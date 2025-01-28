import tkinter as tk
from tkinter import messagebox
from db_utils import execute_query, execute_non_query

class AssignedManagementForm(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):

        # Create a frame for the heading
        heading_frame = tk.Frame(self)
        heading_frame.grid(row=0, column=0, columnspan=1, padx=5, pady=(5, 0))
        
        # Add headings as labels
        headings = ["InfectionID","Cause Type"]
        for col_num, heading in enumerate(headings):
            label = tk.Label(heading_frame, text=heading, borderwidth=2, relief="groove", width=10)
            label.grid(row=0, column=col_num, padx=1, pady=1)

        self.assigned_listbox = tk.Listbox(self)
        self.assigned_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

          # Configure the Listbox frame grid
        # self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)


        # self.button_add = tk.Button(self, text="Add Assignment", command=lambda: self.controller.show_frame("AddEditAssignedForm"))
        # self.button_add.grid(row=1, column=0, padx=10, pady=10)

        # self.button_edit = tk.Button(self, text="Edit Assignment", command=self.edit_assignment)
        # self.button_edit.grid(row=1, column=1, padx=10, pady=10)

        # self.button_delete = tk.Button(self, text="Delete Assignment", command=self.delete_assignment)
        # self.button_delete.grid(row=1, column=2, padx=10, pady=10)

        self.button_delete = tk.Button(self, text="Back to Patient Data", command=lambda: self.controller.show_frame("PatientManagementForm"))
        self.button_delete.grid(row=2, column=0, padx=10, pady=10)

        self.load_assignments()

    def load_assignments(self):
        self.assigned_listbox.delete(0, tk.END)
        query = "SELECT infectionID, causeType FROM Assigned"
        assignments = execute_query(query)
        for assignment in assignments:
            self.assigned_listbox.insert(tk.END, f"{assignment[0]} - {assignment[1]}")

    def edit_assignment(self):
        selected = self.assigned_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No assignment selected")
            return
        assigned_id = self.assigned_listbox.get(selected).split(" - ")[0]
        self.controller.frames["AddEditAssignedForm"].load_assignment(assigned_id)
        self.controller.show_frame("AddEditAssignedForm")

    def delete_assignment(self):
        selected = self.assigned_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No assignment selected")
            return
        assigned_id = self.assigned_listbox.get(selected).split(" - ")[0]
        query = "DELETE FROM assigned WHERE infectionID = :1"
        execute_non_query(query, (assigned_id,))
        self.load_assignments()

if __name__ == "__main__":
    root = tk.Tk()
    frame = AssignedManagementForm(root, None)
    frame.pack()
    root.mainloop()
