from tkinter import *
from tkinter.ttk import *
import tkinter as tk

m = tk.Tk()


m.title("MDDB 1.0")


def Show_Patients():

    sp = Toplevel(m)
    sp.title("Patient List(MDDB 1.0)")

    testpatient = tk.Button(sp,
                            text="Test Patient",
                            width=25,
                            command=Patient_Button)
    testpatient.pack()


def Patient_Button():

    pb = Toplevel(m)
    pb.title("Test Patient(MDDB 1.0)")

    pblabel = Label(pb,
                    text=("Name = Test\n Surname = Patient \n Age = Test Age\n Phone Number = 00 000 00\n E-mail = test@test.com\n illness = test illness\n Doctor Name = Prof. Dr. Test ")).pack()


def Add_Patient():

    global firstname
    global patientnamelabel

    ap = Toplevel(m)
    ap.title("Add Patient(MDDB 1.0)")

    Label(ap, text="First Name:").pack()
    firstnameentry = Entry(ap)
    firstnameentry.pack()
    firstname = firstnameentry.get()

    Label(ap, text="Last Name:").pack()
    lastnameentry = Entry(ap)
    lastnameentry.pack()
    lastname = lastnameentry.get()

    Label(ap, text="Age:").pack()
    ageentry = Entry(ap)
    ageentry.pack()
    age = ageentry.get()

    Label(ap, text="Phone Number:").pack()
    phonenumberentry = Entry(ap)
    phonenumberentry.pack()
    phonenumber = phonenumberentry.get()

    Label(ap, text="E-mail:").pack()
    emailentry = Entry(ap)
    emailentry.pack()
    email = emailentry.get()

    Label(ap, text="İllness:").pack()
    illnessentry = Entry(ap)
    illnessentry.pack()
    illness = illnessentry.get()

    Label(ap, text="Doctor Name:").pack()
    doctornameentry = Entry(ap)
    doctornameentry.pack()
    doctorname = doctornameentry.get()

    patientnamelabel = Label(ap).pack()

    addpatientbutton = tk.Button(ap,
                                 text="Add Patient")

    addpatientbutton.pack()


introduction = Label(m,
                     text="Welcome to MDDB 1.0 \n Made by 3arii \n This is a test version of the GUI, continue using the terminal version for safer usage!")
introduction.pack()

patientbutton = tk.Button(m,
                          text="View Patients",
                          width=25,
                          command=Show_Patients)
patientbutton.pack()

addpatient = tk.Button(m,
                       text="Add a patient to the database",
                       width=25,
                       command=Add_Patient)
addpatient.pack()

m.mainloop()
