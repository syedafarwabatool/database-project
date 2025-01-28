import tkinter as tk
from tkinter import font
from patient_management_form import PatientManagementForm
from add_edit_patient_form import AddEditPatientForm
from diagnosis_management_form import DiagnosisManagementForm
from add_edit_diagnosis_form import AddEditDiagnosisForm
from treatment_management_form import TreatmentManagementForm
from add_edit_treatment_form import AddEditTreatmentForm
from etiology_management_form import EtiologyManagementForm
from add_edit_etiology_form import AddEditEtiologyForm
from cause_management_form import CauseManagementForm
from add_edit_cause_form import AddEditCauseForm
from assigned_management_form import AssignedManagementForm
from add_edit_assigned_form import AddEditAssignedForm

class MainController(tk.Tk):
    def __init__(self,bg_color="pink"):
        super().__init__()
        self.title("Healthcare Management System")
        self.geometry("800x600")
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        # Define a custom font
        custom_font = font.Font(family="Helvetica", size=14)  # You can change the family and size as needed

        # Apply the custom font to all widgets
        self.option_add("*Font", custom_font)

        self.frames = {}
        self.bg_color = bg_color

        for F in (PatientManagementForm, AddEditPatientForm, DiagnosisManagementForm, AddEditDiagnosisForm, TreatmentManagementForm, AddEditTreatmentForm, EtiologyManagementForm, AddEditEtiologyForm, CauseManagementForm, AddEditCauseForm, AssignedManagementForm, AddEditAssignedForm):
            page_name = F.__name__
            frame = F(parent=self, controller=self, bg_color=self.bg_color)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PatientManagementForm")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = MainController()
    app.mainloop()
