import tkinter as tk
from tkinter import messagebox

def dec_to_bin():
    try:
        n = int(entry.get())
        result_label.config(text="Binary: " + bin(n)[2:])
    except:
        messagebox.showerror("Error", "Please enter a valid Decimal number")

def bin_to_dec():
    try:
        n = entry.get()
        result_label.config(text="Decimal: " + str(int(n, 2)))
    except:
        messagebox.showerror("Error", "Please enter a valid Binary number")

def dec_to_oct():
    try:
        n = int(entry.get())
        result_label.config(text="Octal: " + oct(n)[2:])
    except:
        messagebox.showerror("Error", "Please enter a valid Decimal number")

def dec_to_hex():
    try:
        n = int(entry.get())
        result_label.config(text="Hexadecimal: " + hex(n)[2:].upper())
    except:
        messagebox.showerror("Error", "Please enter a valid Decimal number")

def clear_all():
    entry.delete(0, tk.END)
    result_label.config(text="Result:")

# Main window
root = tk.Tk()
root.title("Number System Converter")
root.geometry("400x350")
root.configure(bg="#222222")

# Title
title = tk.Label(root, text="Number System Converter", font=("Arial", 16, "bold"), bg="#222222", fg="white")
title.pack(pady=10)

# Input
input_label = tk.Label(root, text="Enter Number:", font=("Arial", 12), bg="#222222", fg="white")
input_label.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#222222")
btn_frame.pack(pady=10)

btn1 = tk.Button(btn_frame, text="Dec → Bin", width=12, command=dec_to_bin, bg="#287683", fg="white")
btn1.grid(row=0, column=0, padx=5, pady=5)

btn2 = tk.Button(btn_frame, text="Bin → Dec", width=12, command=bin_to_dec, bg="#2196F3", fg="white")
btn2.grid(row=0, column=1, padx=5, pady=5)

btn3 = tk.Button(btn_frame, text="Dec → Oct", width=12, command=dec_to_oct, bg="#164A89", fg="white")
btn3.grid(row=1, column=0, padx=5, pady=5)

btn4 = tk.Button(btn_frame, text="Dec → Hex", width=12, command=dec_to_hex, bg="#9C27B0", fg="white")
btn4.grid(row=1, column=1, padx=5, pady=5)

# Result
result_label = tk.Label(root, text="Result:", font=("Arial", 13, "bold"), bg="#222222", fg="cyan")
result_label.pack(pady=15)

# Clear button
clear_btn = tk.Button(root, text="Clear", width=15, command=clear_all, bg="#f44336", fg="white")
clear_btn.pack(pady=5)

# Run
root.mainloop()