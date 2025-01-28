import tkinter as tk
from tkinter import messagebox
from db_utils import execute_non_query, execute_query

class AddEditDiagnosisForm(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.diagnosis_id = None
        self.create_widgets()

    def create_widgets(self):
        self.label_TID = tk.Label(self, text="Test ID")
        self.label_TID.grid(row=0, column=0, padx=10, pady=10)

        self.entry_TID = tk.Entry(self)
        self.entry_TID.grid(row=0, column=1, padx=10, pady=10)

        self.label_IID = tk.Label(self, text="Infection ID")
        self.label_IID.grid(row=1, column=0, padx=10, pady=10)

        self.entry_IID = tk.Entry(self)
        self.entry_IID.grid(row=1, column=1, padx=10, pady=10)

        self.label_name = tk.Label(self, text="Test Name")
        self.label_name.grid(row=2, column=0, padx=10, pady=10)

        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=2, column=1, padx=10, pady=10)

        self.label_result = tk.Label(self, text="Result")
        self.label_result.grid(row=3, column=0, padx=10, pady=10)

        self.entry_result = tk.Entry(self)
        self.entry_result.grid(row=3, column=1, padx=10, pady=10)

        self.button_save = tk.Button(self, text="Save", command=self.save_diagnosis)
        self.button_save.grid(row=4, column=0, columnspan=2, pady=10)

        self.button_cancel = tk.Button(self, text="Cancel", command=lambda: self.controller.show_frame("DiagnosisManagementForm"))
        self.button_cancel.grid(row=5, column=0, columnspan=2, pady=10)

    def load_diagnosis(self, diagnosis_id):
        self.diagnosis_id = diagnosis_id
        query = "SELECT testID, infectionID FROM diagnosis WHERE TestID = ?"
        diagnosis = execute_query(query, (diagnosis_id,))
        if diagnosis:
            self.entry_TID.delete(0, tk.END)
            self.entry_TID.insert(0, diagnosis[0][0])
            self.entry_IID.delete(0, tk.END)
            self.entry_IID.insert(0, diagnosis[0][1])

    def save_diagnosis(self):
        TestID = self.entry_TID.get()
        # infectionID = self.entry_IID.get()
        Testname = self.entry_name.get()
        result = self.entry_result.get()
        if self.diagnosis_id:
            query = "UPDATE diagnosis SET TestID = ?, testname=?, result = ? WHERE TestID = ?"
            execute_non_query(query, (TestID, Testname, result, self.diagnosis_id))
        else:
            query = "INSERT INTO diagnosis (TestID, testname, result) VALUES (?, ?, ?)"
            execute_non_query(query, (TestID, Testname, result))
        self.controller.show_frame("DiagnosisManagementForm")
        self.controller.frames["DiagnosisManagementForm"].load_diagnoses()

if __name__ == "__main__":
    root = tk.Tk()
    frame = AddEditDiagnosisForm(root, None)
    frame.pack()
    root.mainloop()
