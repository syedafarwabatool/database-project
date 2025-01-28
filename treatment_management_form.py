import tkinter as tk
from tkinter import messagebox
from db_utils import execute_query, execute_non_query

class TreatmentManagementForm(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the heading
        heading_frame = tk.Frame(self)
        heading_frame.grid(row=0, column=0, columnspan=1, padx=5, pady=(5, 0))
        
        # Add headings as labels
        headings = ["TreatmentID", "InfectionID","PhysicianID","Medication","Outcome","OtherTherapy"]
        for col_num, heading in enumerate(headings):
            label = tk.Label(heading_frame, text=heading, borderwidth=2, relief="groove", width=11)
            label.grid(row=0, column=col_num, padx=1, pady=1)

        self.treatment_listbox = tk.Listbox(self, width=70)
        self.treatment_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

          # Configure the Listbox frame grid
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.button_add = tk.Button(self, text="Add Treatment", command=lambda: self.controller.show_frame("AddEditTreatmentForm"))
        self.button_add.grid(row=2, column=0, padx=10, pady=10)

        self.button_edit = tk.Button(self, text="Edit Treatment", command=self.edit_treatment)
        self.button_edit.grid(row=3, column=0, padx=10, pady=10)

        self.button_delete = tk.Button(self, text="Delete Treatment", command=self.delete_treatment)
        self.button_delete.grid(row=4, column=0, padx=10, pady=10)

        self.button_delete = tk.Button(self, text="Manage Etiology", command=lambda: self.controller.show_frame("EtiologyManagementForm"))
        self.button_delete.grid(row=5, column=0, padx=10, pady=10)

        self.load_treatments()

    def load_treatments(self):
        self.treatment_listbox.delete(0, tk.END)
        query = "SELECT * FROM treatment"
        treatments = execute_query(query)
        for treatment in treatments:
            self.treatment_listbox.insert(tk.END, f"{treatment[0]} - {treatment[1]} - {treatment[2]} - {treatment[3]} - {treatment[4]} - {treatment[5]}")

    def edit_treatment(self):
        selected = self.treatment_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No treatment selected")
            return
        treatment_id = self.treatment_listbox.get(selected).split(" - ")[0]
        self.controller.frames["AddEditTreatmentForm"].load_treatment(treatment_id)
        self.controller.show_frame("AddEditTreatmentForm")

    def delete_treatment(self):
        selected = self.treatment_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No treatment selected")
            return
        treatment_id = self.treatment_listbox.get(selected).split(" - ")[0]
        query = "DELETE FROM treatment WHERE treatmentID = ?"
        execute_non_query(query, (treatment_id,))
        self.load_treatments()

if __name__ == "__main__":
    root = tk.Tk()
    frame = TreatmentManagementForm(root, None)
    frame.pack()
    root.mainloop()
