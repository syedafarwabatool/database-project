import tkinter as tk
from tkinter import messagebox
from db_utils import execute_non_query, execute_query

class AddEditPatientForm(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.patient_id = None
        self.create_widgets()

    def create_widgets(self):

        self.label_id = tk.Label(self, text="ID")
        self.label_id.grid(row=0, column=0, padx=10, pady=10)

        self.entry_id = tk.Entry(self)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)

        self.label_age = tk.Label(self, text="Age")
        self.label_age.grid(row=1, column=0, padx=10, pady=10)

        self.entry_age = tk.Entry(self)
        self.entry_age.grid(row=1, column=1, padx=10, pady=10)

        self.label_gender = tk.Label(self, text="Gender")
        self.label_gender.grid(row=2, column=0, padx=10, pady=10)

        self.entry_gender = tk.Entry(self)
        self.entry_gender.grid(row=2, column=1, padx=10, pady=10)

        self.label_contact = tk.Label(self, text="Contact")
        self.label_contact.grid(row=3, column=0, padx=10, pady=10)

        self.entry_contact = tk.Entry(self)
        self.entry_contact.grid(row=3, column=1, padx=10, pady=10)

        self.label_address = tk.Label(self, text="Address")
        self.label_address.grid(row=4, column=0, padx=10, pady=10)

        self.entry_address = tk.Entry(self)
        self.entry_address.grid(row=4, column=1, padx=10, pady=10)

        self.button_save = tk.Button(self, text="Save", command=self.save_patient)
        self.button_save.grid(row=5, column=0, columnspan=2, pady=10)

        self.button_cancel = tk.Button(self, text="Cancel", command=lambda: self.controller.show_frame("PatientManagementForm"))
        self.button_cancel.grid(row=6, column=0, columnspan=2, pady=10)

    def load_patient(self, patient_id):
        self.patient_id = patient_id
        query = "SELECT Contact FROM Patients WHERE PatientID = ?"
        patient = execute_query(query, (patient_id,))
        if patient:
            self.entry_contact.delete(0, tk.END)
            self.entry_contact.insert(0, patient[0][0])

    def save_patient(self):
        id = self.entry_id.get()
        age = self.entry_age.get()
        gender = self.entry_gender.get()
        contact = self.entry_contact.get()
        address = self.entry_address.get()
        if self.patient_id:
            query = "UPDATE Patients SET PatientID = ?, Age = ?, Gender = ?, Contact = ?, Address = ?  WHERE PatientID = ?"
            execute_non_query(query, (id, age, gender, contact, address, self.patient_id))
        else:
            query = "INSERT INTO Patients (PatientID,Age,Gender,Contact,Address) VALUES (?, ?, ?, ?, ?)"
            execute_non_query(query, (id, age, gender, contact, address))
        self.controller.show_frame("PatientManagementForm")
        self.controller.frames["PatientManagementForm"].load_patients()

if __name__ == "__main__":
    root = tk.Tk()
    frame = AddEditPatientForm(root, None)
    frame.pack()
    root.mainloop()
