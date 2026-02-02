import tkinter as tk 
from tkinter import messagebox
def print_table():
    try:
        num = int(entry.get())
        table = ""
        for i in range(1, 11):
            table += f"{num} x {i} = {num * i}\n"
        result_label.config(text=table, fg="brown", justify="left")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer") 
# Create window
root = tk.Tk()

root.title("Multiplication Table Printer")
root.geometry("300x300")   
# Heading
title_label = tk.Label(root, text="Multiplication Table Printer", font=("Arial", 16,"bold"))
title_label.pack(pady=10)
# Entry
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)
# Button
print_btn = tk.Button(root, text="Print Table", font=("Arial", 12), command=print_table)
print_btn.pack(pady=10)
# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12), justify="left")
result_label.pack(pady=10)
# Run app
root.mainloop()