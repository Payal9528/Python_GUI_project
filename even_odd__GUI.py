import tkinter as tk
from tkinter import messagebox

def check_even_odd():
    try:
        num = int(entry.get())
        if num % 2 == 0:
            result_label.config(text="Result: Even Number", fg="green")
        else:
            result_label.config(text="Result: Odd Number", fg="blue")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")

# Create window
root = tk.Tk()
root.title("Even Odd Checker")
root.geometry("300x200")

# Heading
title_label = tk.Label(root, text="Even Odd Checker", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Entry
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

# Button
check_btn = tk.Button(root, text="Check", font=("Arial", 12), command=check_even_odd)
check_btn.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

# Run app
root.mainloop()