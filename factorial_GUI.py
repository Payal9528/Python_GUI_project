import tkinter as tk 
from tkinter import messagebox
def calculate_factorial():
    try:
        num = int(entry.get())
        if num < 0:
            messagebox.showerror("Error", "Please enter a non-negative integer")
            return
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        result_label.config(text=f"Result: {factorial}", fg="purple")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")

root = tk.Tk() 
root.title("Factorial Calculator")
root.geometry("300x200")

title_label = tk.Label(root, text="Factorial Calculator", font=("Arial", 16,"bold"))
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14)) 
entry.pack(pady=5)
# Button
calc_b = tk.Button(root, text="Calculate", font=("Arial", 12), command=calculate_factorial)
calc_btn.pack(pady=10)
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
                       