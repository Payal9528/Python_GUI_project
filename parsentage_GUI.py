import tkinter as tk
from tkinter import messagebox

def calculate_percentage():
    try:
        total_marks = float(entry_total.get())
        obtained_marks = float(entry_obtained.get())
        
        if total_marks <= 0:
            messagebox.showerror("Error", "Total marks must be greater than zero")
            return
        
        if obtained_marks < 0:
            messagebox.showerror("Error", "Obtained marks cannot be negative")
            return
        
        if obtained_marks > total_marks:
            messagebox.showerror("Error", "Obtained marks cannot exceed total marks")
            return
        
        percentage = (obtained_marks / total_marks) * 100
        result_label.config(text=f"Result: {percentage:.2f}%", fg="orange")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create window
root = tk.Tk()
root.title("Percentage Calculator")
root.geometry("350x250")

# Heading
title_label = tk.Label(root, text="Percentage Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Entry for total marks
entry_total = tk.Entry(root, font=("Arial", 14))
entry_total.pack(pady=5)

# Entry for obtained marks
entry_obtained = tk.Entry(root, font=("Arial", 14))
entry_obtained.pack(pady=5)

# Button
calc_btn = tk.Button(root, text="Calculate Percentage", font=("Arial", 12), command=calculate_percentage)
calc_btn.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

# Run app
root.mainloop()
