import tkinter as tk
from tkinter import messagebox
from db_utils import execute_query, execute_non_query

class DiagnosisManagementForm(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):

        # Create a frame for the heading
        heading_frame = tk.Frame(self)
        heading_frame.grid(row=0, column=0, columnspan=1, padx=5, pady=(5, 0))
        
        # Add headings as labels
        headings = ["TestID", "InfectionID","TestName","Result"]
        for col_num, heading in enumerate(headings):
            label = tk.Label(heading_frame, text=heading, borderwidth=2, relief="groove", width=10)
            label.grid(row=0, column=col_num, padx=1, pady=1)

        self.diagnosis_listbox = tk.Listbox(self, width=50)
        self.diagnosis_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

          # Configure the Listbox frame grid
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.button_add = tk.Button(self, text="Add Diagnosis", command=lambda: self.controller.show_frame("AddEditDiagnosisForm"))
        self.button_add.grid(row=2, column=0, padx=10, pady=10)

        self.button_edit = tk.Button(self, text="Edit Diagnosis", command=self.edit_diagnosis)
        self.button_edit.grid(row=3, column=0, padx=10, pady=10)

        self.button_delete = tk.Button(self, text="Delete Diagnosis", command=self.delete_diagnosis)
        self.button_delete.grid(row=4, column=0, padx=10, pady=10)

        self.button_delete = tk.Button(self, text="Manage Treatment", command=lambda: self.controller.show_frame("TreatmentManagementForm"))
        self.button_delete.grid(row=5, column=0, padx=10, pady=10)

        self.load_diagnoses()

    def load_diagnoses(self):
        self.diagnosis_listbox.delete(0, tk.END)
        query = "SELECT * FROM diagnosis"
        diagnoses = execute_query(query)
        for diagnosis in diagnoses:
            self.diagnosis_listbox.insert(tk.END, f"{diagnosis[0]} - {diagnosis[1]} - {diagnosis[2]} - {diagnosis[3]}")

    def edit_diagnosis(self):
        selected = self.diagnosis_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No diagnosis selected")
            return
        diagnosis_id = self.diagnosis_listbox.get(selected).split(" - ")[0]
        self.controller.frames["AddEditDiagnosisForm"].load_diagnosis(diagnosis_id)
        self.controller.show_frame("AddEditDiagnosisForm")

    def delete_diagnosis(self):
        selected = self.diagnosis_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No diagnosis selected")
            return
        diagnosis_id = self.diagnosis_listbox.get(selected).split(" - ")[0]
        query = "DELETE FROM diagnosis WHERE TestID = ?"
        execute_non_query(query, (diagnosis_id,))
        self.load_diagnoses()

if __name__ == "__main__":
    root = tk.Tk()
    frame = DiagnosisManagementForm(root, None)
    frame.pack()
    root.mainloop()
