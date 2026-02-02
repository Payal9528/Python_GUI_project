import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ---------------- Database Setup ----------------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll TEXT NOT NULL,
    course TEXT,
    email TEXT,
    phone TEXT
)
""")
conn.commit()

# ---------------- Functions ----------------
def add_student():
    name = name_var.get()
    roll = roll_var.get()
    course = course_var.get()
    email = email_var.get()
    phone = phone_var.get()

    if name == "" or roll == "":
        messagebox.showerror("Error", "Name and Roll No are required")
        return

    cursor.execute("INSERT INTO students (name, roll, course, email, phone) VALUES (?, ?, ?, ?, ?)",
                   (name, roll, course, email, phone))
    conn.commit()
    messagebox.showinfo("Success", "Student added successfully")
    clear_fields()
    view_students()

def view_students():
    # Clear old data
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for index, row in enumerate(rows):
        if index % 2 == 0:
            tree.insert("", tk.END, values=row, tags=("evenrow",))
        else:
            tree.insert("", tk.END, values=row, tags=("oddrow",))

def delete_student():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a student to delete")
        return
    student_id = tree.item(selected_item)["values"][0]
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    messagebox.showinfo("Deleted", "Student deleted successfully")
    view_students()

def clear_fields():
    name_var.set("")
    roll_var.set("")
    course_var.set("")
    email_var.set("")
    phone_var.set("")

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("800x500")
root.configure(bg="#f0f0f0")

# Style for Treeview
style = ttk.Style()
style.configure("Treeview.Heading",
                font=("Helvetica", 11, "bold"),
                background="#d9d9d9",   # heading background light gray
                foreground="black")     # heading text black

style.configure("Treeview",
                font=("Helvetica", 10),
                rowheight=25,
                foreground="black")     # rows text black

# Variables
name_var = tk.StringVar()
roll_var = tk.StringVar()
course_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()

label_font = ("Helvetica", 10, "bold")
entry_font = ("Helvetica", 10)

# Labels & Entries
tk.Label(root, text="Name", bg="#f0f0f0", font=label_font).grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=name_var, font=entry_font, fg="black", bg="white").grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Roll No", bg="#f0f0f0", font=label_font).grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=roll_var, font=entry_font, fg="black", bg="white").grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Course", bg="#f0f0f0", font=label_font).grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=course_var, font=entry_font, fg="black", bg="white").grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Email", bg="#f0f0f0", font=label_font).grid(row=3, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=email_var, font=entry_font, fg="black", bg="white").grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Phone", bg="#f0f0f0", font=label_font).grid(row=4, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=phone_var, font=entry_font, fg="black", bg="white").grid(row=4, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Student", command=add_student,
          bg="#4CAF50", fg="white", font=label_font).grid(row=5, column=0, pady=10)

tk.Button(root, text="Delete Student", command=delete_student,
          bg="#E74C3C", fg="white", font=label_font).grid(row=5, column=1, pady=10)

tk.Button(root, text="Clear Fields", command=clear_fields,
          bg="#3498DB", fg="white", font=label_font).grid(row=5, column=2, pady=10)

# Treeview (Table)
tree = ttk.Treeview(root, columns=("ID", "Name", "Roll", "Course", "Email", "Phone"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Roll", text="Roll No")
tree.heading("Course", text="Course")
tree.heading("Email", text="Email")
tree.heading("Phone", text="Phone")
tree.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=6, column=3, sticky="ns")

# Row Colors
tree.tag_configure("oddrow", background="#f9f9f9", foreground="black")
tree.tag_configure("evenrow", background="#e6f7ff", foreground="black")

view_students()

root.mainloop()
