import tkinter as tk
from tkinter import messagebox
from db_utils import execute_query, execute_non_query

class PatientManagementForm(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # label = tk.Label(self, text="PatientID - Age - Gender - Contact - Address")
        # label.grid(row=0, column=0, padx=20, pady=20)

        # Create a frame for the heading
        heading_frame = tk.Frame(self)
        heading_frame.grid(row=0, column=0, columnspan=1, padx=5, pady=(5, 0))
        
        # Add headings as labels
        headings = ["PatientID", "Age","Gender","Contact","Address"]
        for col_num, heading in enumerate(headings):
            label = tk.Label(heading_frame, text=heading, borderwidth=2, relief="groove", width=10)
            label.grid(row=0, column=col_num, padx=1, pady=1)

        self.patient_listbox = tk.Listbox(self, width = 50)
        self.patient_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

          # Configure the Listbox frame grid
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.button_add = tk.Button(self, text="Add Patient", command=lambda: self.controller.show_frame("AddEditPatientForm"))
        self.button_add.grid(row=2, column=0, padx=10, pady=10)

        self.button_edit = tk.Button(self, text="Edit Patient", command=self.edit_patient)
        self.button_edit.grid(row=3, column=0, padx=10, pady=10)

        self.button_delete = tk.Button(self, text="Delete Patient", command=self.delete_patient)
        self.button_delete.grid(row=4, column=0, padx=10, pady=10)

        self.button_delete = tk.Button(self, text="Manage Diagnosis", command=lambda: self.controller.show_frame("DiagnosisManagementForm"))
        self.button_delete.grid(row=5, column=0, padx=10, pady=10)

        self.load_patients()

    def load_patients(self):
        self.patient_listbox.delete(0, tk.END)
        query = "SELECT * FROM patients"
        patients = execute_query(query)
        for patient in patients:
            self.patient_listbox.insert(tk.END, f"{patient[0]} - {patient[1]} - {patient[2]} - {patient[3]} - {patient[4]}")

    def edit_patient(self):
        selected = self.patient_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No patient selected")
            return
        patient_id = self.patient_listbox.get(selected).split(" - ")[0]
        self.controller.frames["AddEditPatientForm"].load_patient(patient_id)
        self.controller.show_frame("AddEditPatientForm")

    def delete_patient(self):
        selected = self.patient_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No patient selected")
            return
        patient_id = self.patient_listbox.get(selected).split(" - ")[0]
        query = "DELETE FROM Patients WHERE patientID = ?"
        execute_non_query(query, (patient_id,))
        self.load_patients()

if __name__ == "__main__":
    root = tk.Tk()
    frame = PatientManagementForm(root, None)
    frame.pack()
    root.mainloop()
