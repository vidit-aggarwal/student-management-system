import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title('Student Management System | DIT University')

label_1 = tk.Label(mainWindow, text="\nDIT UNIVERSITY STUDENT MANAGEMENT PORTAL\n", font=("Georgia", 30))
label_1.pack(padx=100, pady=50)


button_1 = tk.Button(mainWindow, text="Add Student", command=lambda: add(), padx=275, pady=25)
button_1.pack()

button_2 = tk.Button(mainWindow,text="Update Student Details", command=lambda: update(), padx=240, pady=25)
button_2.pack()

button_3 = tk.Button(mainWindow, text="View Student Details", command=lambda: view(), padx=248, pady=25)
button_3.pack()

button_4 = tk.Button(mainWindow,text="Delete Student", command=lambda: delete(), padx=267, pady=25)
button_4.pack()

button_5 = tk.Button(mainWindow, text="Search Student", command=lambda: search(), padx=267, pady=25)
button_5.pack()

label_2 = tk.Label(mainWindow, text="\n")
label_2.pack()


def add():
    add_window = tk.Tk()
    add_window.title("Add Student Details")

    name_label = tk.Label(add_window, text="Student Name:", padx=100)
    name_label.pack()
    name_entry = tk.Entry(add_window)
    name_entry.pack()
    branch_label = tk.Label(add_window, text="Branch:")
    branch_label.pack()
    branch_entry = tk.Entry(add_window)
    branch_entry.pack()
    class_label = tk.Label(add_window, text="Section:")
    class_label.pack()
    class_entry = tk.Entry(add_window)
    class_entry.pack()
    roll_label = tk.Label(add_window, text="Roll Number(University):")
    roll_label.pack()
    roll_entry = tk.Entry(add_window)
    roll_entry.pack()
    grade_label = tk.Label(add_window, text="Updated CGPA:")
    grade_label.pack()
    grade_entry = tk.Entry(add_window)
    grade_entry.pack()
    add_window.mainloop()


def update():
    update_window = tk.Tk()
    update_window.title("Update Student Details")


def view():
    view_window = tk.Tk()
    view_window.title("View Student Details")


def delete():
    delete_window = tk.Tk()
    delete_window.title("Delete Student ")


def search():
    search_window = tk.Tk()
    search_window.title("SEARCH STUDENT DETAIL")


mainWindow.mainloop()
