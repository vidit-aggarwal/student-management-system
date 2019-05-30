import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox

con = sqlite3.connect("university.db")
con.execute("CREATE TABLE IF NOT EXISTS student(name TEXT, branch TEXT, section TEXT, roll INTEGER, cgpa FLOAT);")


def insert_data(name, branch, section, roll, cgpa):
    conn = sqlite3.connect("university.db")
    conn.execute("INSERT INTO student(name, branch, section, roll, cgpa) VALUES( '" + name + "', '" + branch +
                 "', '" + section + "', '" + roll + "', '" + cgpa + "' );")
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Data Saved Successfully.")


def insert():
    add_window = tk.Tk()
    add_window.title("Add Student Details")
    tk.Label(add_window).grid(row=0, column=0, columnspan=2)
    tk.Label(add_window, text="Student Name:").grid(row=1, column=0)
    name_entry = tk.Entry(add_window, width=50)
    name_entry.grid(row=1, column=1, padx=25)
    tk.Label(add_window, text="Branch:").grid(row=2, column=0)
    branch_entry = tk.Entry(add_window, width=50)
    branch_entry.grid(row=2, column=1, padx=25)
    tk.Label(add_window, text="Section:").grid(row=3, column=0)
    class_entry = tk.Entry(add_window, width=50)
    class_entry.grid(row=3, column=1, padx=25)
    tk.Label(add_window, text="Roll Number(University):").grid(row=4, column=0, padx=20)
    roll_entry = tk.Entry(add_window, width=50)
    roll_entry.grid(row=4, column=1, padx=25)
    tk.Label(add_window, text="Updated CGPA:").grid(row=5, column=0)
    grade_entry = tk.Entry(add_window, width=50)
    grade_entry.grid(row=5, column=1, padx=25)

    tk.Button(add_window, text='Submit', activebackground='grey', activeforeground='white', command=lambda: submit()).grid(row=6, column=0, columnspan=2, pady=10)

    def submit():
        name = name_entry.get()
        branch = branch_entry.get()
        section = class_entry.get()
        roll = str(roll_entry.get())
        cgpa = str(grade_entry.get())
        insert_data(name, branch, section, roll, cgpa)
        add_window.destroy()

    add_window.mainloop()


def display():
    connn = sqlite3.connect("university.db")
    display_window = tk.Tk()
    display_window.title("Students Database")
    table = ttk.Treeview(display_window)
    table["columns"] = ("one", "two", "three", "four", "five")

    table.heading("one", text="Name")
    table.heading("two", text="Branch")
    table.heading("three", text="Section")
    table.heading("four", text="Roll No")
    table.heading("five", text="CGPA")

    cursor = connn.execute("SELECT rowid,* FROM student;")
    i = 0
    for row in cursor:
        table.insert('', i, text="Student " + str(row[0]), values=(row[1], row[2], row[3], row[4], row[5]))
        i = i + 1
    table.pack()
    connn.close()


def update():
    update_window = tk.Tk()
    update_window.title("Update Student Details")
    tk.Label(update_window, text="Select the ID of student to be Updated:").grid(row=0, column=0, sticky="W", padx=10, columnspan=2)
    s_id = tk.Entry(update_window, width=50)
    s_id.grid(row=1, column=0, sticky="W", padx=10, columnspan=2)
    tk.Label(update_window, text="\nEnter the new values:").grid(row=2, column=0, sticky="W", padx=10, pady=10, columnspan=2)
    tk.Label(update_window, text="Name:").grid(row=3, column=0, sticky="W", padx=10, pady=10)
    s_name = tk.Entry(update_window, width=50)
    s_name.grid(row=3, column=1, sticky="W", padx=10, pady=10)
    tk.Label(update_window, text="Branch:").grid(row=4, column=0, sticky="W", padx=10, pady=10)
    s_branch = tk.Entry(update_window, width=50)
    s_branch.grid(row=4, column=1, sticky="W", padx=10, pady=10)
    tk.Label(update_window, text="Section:").grid(row=5, column=0, sticky="W", padx=10, pady=10)
    s_section = tk.Entry(update_window, width=50)
    s_section.grid(row=5, column=1, sticky="W", padx=10, pady=10)
    tk.Label(update_window, text="Roll No:").grid(row=6, column=0, sticky="W", padx=10, pady=10)
    s_roll = tk.Entry(update_window, width=50)
    s_roll.grid(row=6, column=1, sticky="W", padx=10, pady=10)
    tk.Label(update_window, text="CGPA").grid(row=7, column=0, sticky="W", padx=10, pady=10)
    s_cgpa = tk.Entry(update_window, width=50)
    s_cgpa.grid(row=7, column=1, sticky="W", padx=10, pady=10)
    tk.Button(update_window, text="Update", activebackground='grey', activeforeground='white',
              command=lambda: submit()).grid(row=8, column=0, padx=10, pady=10, columnspan=2)

    def submit():
        sid = s_id.get()
        sname = s_name.get()
        sbranch = s_branch.get()
        ssection = s_section.get()
        sroll = s_roll.get()
        scgpa = s_cgpa.get()
        scon = sqlite3.connect("university.db")
        scon.execute("UPDATE student SET name = '" + sname + "',branch = '" + sbranch + "', section = '" + ssection +
                     "', roll = '" + sroll + "', cgpa = '" + scgpa + "' WHERE rowid = " + sid + ";")
        scon.commit()
        scon.close()
        messagebox.showinfo("Success", "Data Updated Successfully.")
        update_window.destroy()
    update_window.mainloop()


def delete():
    delete_window = tk.Tk()
    delete_window.title("Delete Student ")
    tk.Label(delete_window, text="Enter Student Name whose details are to be removed:").grid(row=0, column=0, padx=10, pady=10)
    d_name = tk.Entry(delete_window, width=50)
    d_name.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(delete_window, text="Delete Details", activebackground='grey', activeforeground='white',
              command=lambda: submit()).grid(row=1, column=0, columnspan=2)
    tk.Label(delete_window).grid(row=2, column=0, columnspan=2)

    def submit():
        dname = d_name.get()
        dcon = sqlite3.connect("university.db")
        dcon.execute("DELETE FROM student WHERE name = '" + dname+"';")
        dcon.commit()
        dcon.execute("VACUUM;")
        dcon.commit()
        dcon.close()
        messagebox.showinfo("Success", "Deleted Successfully.")
        delete_window.destroy()
    delete_window.mainloop()


def search():
    search_window = tk.Tk()
    search_window.title("Search Student Details")

    tk.Label(search_window, text="Enter the name of Student whose details are to be searched:").grid(row=0, column=0,
                                                                                                     padx=10, pady=10)
    f_name = tk.Entry(search_window, width=50)
    f_name.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(search_window, text="Results:").grid(row=1, column=0, sticky="W", columnspan=2, padx=10, pady=10)

    tk.Button(search_window, text="Search", activebackground='grey', activeforeground='white',
              command=lambda: submit()).grid(row=2, column=0, columnspan=2)
    tk.Label(search_window).grid(row=3, column=0, sticky="W", columnspan=2, padx=10, pady=10)
    details = ttk.Treeview(search_window)
    details["columns"] = ("one", "two", "three", "four", "five")

    details.heading("one", text="Name")
    details.heading("two", text="Branch")
    details.heading("three", text="Section")
    details.heading("four", text="Roll No")
    details.heading("five", text="CGPA")

    def submit():
        for row in details.get_children():
            details.delete(row)

        fname = f_name.get()
        fcon = sqlite3.connect("university.db")
        cursor = fcon.execute("SELECT rowid,* from student WHERE name = '" + fname + "';")
        fcon.commit()

        i = 0
        for row in cursor:
            details.insert('', i, text="Student " + str(row[0]), values=(row[1], row[2], row[3], row[4], row[5]))
            i = i + 1

        details.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        fcon.close()
    search_window.mainloop()


con.close()
