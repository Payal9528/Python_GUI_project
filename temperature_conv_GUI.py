import tkinter as tk
from tkinter import messagebox
def temperature_conversion():
    try:
        temp = float(entry.get())
        conversion_type = var.get()
        if conversion_type == "C to F":
            converted_temp = (temp * 9/5) + 32
            result_label.config(text=f"Result: {converted_temp:.2f} °F", fg="red")
        elif conversion_type == "F to C":
            converted_temp = (temp - 32) * 5/9
            result_label.config(text=f"Result: {converted_temp:.2f} °C", fg="blue")
        else:
            messagebox.showerror("Error", "Please select a conversion type")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
# Create window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x250")
# Heading
title_label = tk.Label(root, text="Temperature Converter", font=("Arial", 16,
"bold"))
title_label.pack(pady=10)
# Entry
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)
# Radio buttons for conversion type
var = tk.StringVar()
radio_c_to_f = tk.Radiobutton(root, text="Celsius to Fahrenheit", variable=var, value="C to F", font=("Arial", 12))
radio_c_to_f.pack(pady=2)
radio_f_to_c = tk.Radiobutton(root, text="Fahrenheit to Celsius", variable=var, value="F to C", font=("Arial", 12))
radio_f_to_c.pack(pady=2)
# Button
convert_btn = tk.Button(root, text="Convert", font=("Arial", 12), command=temperature_conversion)
convert_btn.pack(pady=10)
# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)
# Run app
root.mainloop()
