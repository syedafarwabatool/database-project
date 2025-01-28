import tkinter as tk
from user_login_form import UserLoginForm
from registration_form import RegistrationForm
from patient_management_form import PatientManagementForm
from diagnosis_management_form import DiagnosisManagementForm
from treatment_management_form import TreatmentManagementForm
from physician_management_form import PhysicianManagementForm
from infection_management_form import InfectionManagementForm
from etiology_management_form import EtiologyManagementForm
from cause_management_form import CauseManagementForm
from assigned_management_form import AssignedManagementForm

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pinkeye Disease Management System")
        self.geometry("800x600")

        self.frames = {}
        for F in (UserLoginForm, RegistrationForm, PatientManagementForm,
                  DiagnosisManagementForm, TreatmentManagementForm, PhysicianManagementForm,
                  InfectionManagementForm, EtiologyManagementForm, CauseManagementForm, AssignedManagementForm):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("UserLoginForm")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
