import tkinter as tk
from tkinter import messagebox
from db_utils import execute_non_query, execute_query

class AddEditTreatmentForm(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.treatment_id = None
        self.create_widgets()

    def create_widgets(self):
        self.label_TID = tk.Label(self, text="Treatment ID")
        self.label_TID.grid(row=0, column=0, padx=10, pady=10)

        self.entry_TID = tk.Entry(self)
        self.entry_TID.grid(row=0, column=1, padx=10, pady=10)

        self.label_IID = tk.Label(self, text="Infection ID")
        self.label_IID.grid(row=1, column=0, padx=10, pady=10)

        self.entry_IID = tk.Entry(self)
        self.entry_IID.grid(row=1, column=1, padx=10, pady=10)

        self.label_PID = tk.Label(self, text="Physician ID")
        self.label_PID.grid(row=2, column=0, padx=10, pady=10)

        self.entry_PID = tk.Entry(self)
        self.entry_PID.grid(row=2, column=1, padx=10, pady=10)

        self.label_medication = tk.Label(self, text="Medication")
        self.label_medication.grid(row=3, column=0, padx=10, pady=10)

        self.entry_medication = tk.Entry(self)
        self.entry_medication.grid(row=3, column=1, padx=10, pady=10)

        self.label_outcome = tk.Label(self, text="Outcome")
        self.label_outcome.grid(row=4, column=0, padx=10, pady=10)

        self.entry_outcome = tk.Entry(self)
        self.entry_outcome.grid(row=4, column=1, padx=10, pady=10)

        self.label_other = tk.Label(self, text="Other Therapy")
        self.label_other.grid(row=5, column=0, padx=10, pady=10)

        self.entry_other = tk.Entry(self)
        self.entry_other.grid(row=5, column=1, padx=10, pady=10)

        self.button_save = tk.Button(self, text="Save", command=self.save_treatment)
        self.button_save.grid(row=6, column=0, columnspan=2, pady=10)

        self.button_cancel = tk.Button(self, text="Cancel", command=lambda: self.controller.show_frame("TreatmentManagementForm"))
        self.button_cancel.grid(row=7, column=0, columnspan=2, pady=10)

    def load_treatment(self, treatment_id):
        self.treatment_id = treatment_id
        query = "SELECT treatmentID, infectionID, physicianID FROM treatment WHERE treatmentID = ?"
        treatment = execute_query(query, (treatment_id,))
        if treatment:
            self.entry_TID.delete(0, tk.END)
            self.entry_TID.insert(0, treatment[0][0])
            self.entry_IID.delete(0, tk.END)
            self.entry_IID.insert(0, treatment[0][1])
            self.entry_PID.delete(0, tk.END)
            self.entry_PID.insert(0, treatment[0][2])

    def save_treatment(self):
        TID = self.entry_TID.get()
        # IID = self.entry_IID.get()
        # PID = self.entry_PID.get()
        medication = self.entry_medication.get()
        outcome = self.entry_outcome.get()
        other = self.entry_other.get()
        if self.treatment_id:
            query = "UPDATE treatment SET treatmentID = ?, medication = ?, outcome = ?, otherTherapy = ? WHERE treatmentID = ?"
            execute_non_query(query, (TID, medication, outcome, other, self.treatment_id))
        else:
            query = "INSERT INTO treatment (treatmentID, medication, outcome, otherTherapy) VALUES (?, ?, ?, ?)"
            execute_non_query(query, (TID, medication, outcome, other))
        self.controller.show_frame("TreatmentManagementForm")
        self.controller.frames["TreatmentManagementForm"].load_treatments()

if __name__ == "__main__":
    root = tk.Tk()
    frame = AddEditTreatmentForm(root, None)
    frame.pack()
    root.mainloop()
