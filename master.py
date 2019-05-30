import tkinter as tk
import student_database as sd

mainWindow = tk.Tk()
mainWindow.title('Student Management System | DIT University')

label_1 = tk.Label(mainWindow, text="\n  DIT UNIVERSITY STUDENT MANAGEMENT PORTAL  \n", font=("Georgia", 30))
label_1.pack(padx=100, pady=50)


button_1 = tk.Button(mainWindow, text="Add Student", command=lambda: sd.insert(), padx=275, pady=25,
                     activebackground='grey', activeforeground='white')
button_1.pack()

button_2 = tk.Button(mainWindow, text="Update Student Details", command=lambda: sd.update(), padx=240, pady=25,
                     activebackground='grey', activeforeground='white')
button_2.pack()

button_3 = tk.Button(mainWindow, text="View Student Details", command=lambda: sd.display(), padx=248, pady=25,
                     activebackground='grey', activeforeground='white')
button_3.pack()

button_4 = tk.Button(mainWindow, text="Delete Student", command=lambda: sd.delete(), padx=267, pady=25,
                     activebackground='grey', activeforeground='white')
button_4.pack()

button_5 = tk.Button(mainWindow, text="Search Student", command=lambda: sd.search(), padx=267, pady=25,
                     activebackground='grey', activeforeground='white')
button_5.pack()

label_2 = tk.Label(mainWindow, text="\n")
label_2.pack()


mainWindow.mainloop()
