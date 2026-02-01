import tkinter as tk 
import math
# main window 
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("400x400")
root.config(bg="#d6d1d1")
# entry box 
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=5, relief="ridge", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# button click function
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)
# button clear function
def button_clear():
    entry.delete(0, tk.END)
#one by one detelte function
def button_delete():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])
# button equal function
def button_equal():

    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def average():
    try:
        text = entry.get()
        nums = text.split(',')
        nums = [float(num) for num in nums]
        avg = sum(nums) / len(nums)
        entry.delete(0, tk.END)
        entry.insert(0, str(avg))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def percentage():
    try:
        text = entry.get()
        if "%" in text:
            part, total = text.split('%')
            part = float(part)
            total = float(total)
            result = (part / 100) * total
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        else:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def square_root():
    try:
        valu = float(entry.get())
        result = math.sqrt(valu)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
# buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '+',
    '=', 'DEL', 'AVG', '%', 'SQRT'
]
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, width=8, height=2, bg="#97AC98", fg="white", command=button_equal)
        btn.grid(row=5, column=1,columnspan=4, padx=5, pady=5)
    elif button == 'DEL':
        btn = tk.Button(root, text=button, width=8, height=2, bg="#D6C4A9", fg="white", command=button_delete)
        btn.grid(row=5, column=col_val, padx=5, pady=5)
    elif button == 'C':
        btn = tk.Button(root, text=button, width=8, height=2, bg="#9a807e", fg="white", command=button_clear)
        btn.grid(row=4, column=col_val, padx=5, pady=5)
    elif button == 'AVG':
        btn = tk.Button(root, text=button, width=8, height=2, bg="#818A92", fg="white", command=average)
        btn.grid(row=5, column=col_val, padx=5, pady=5)
    elif button == '%':
        btn = tk.Button(root, text=button, width=8, height=2, bg="#99968B", fg="black", command=percentage)
        btn.grid(row=5, column=col_val, padx=5, pady=5)
    elif button == 'SQRT':
        btn = tk.Button(root, text=button, width=8, height=2, bg="#795548", fg="white", command=square_root)
        btn.grid(row=5, column=col_val, padx=5, pady=5)
    elif button in '.+-*/':
        btn = tk.Button(root, text=button, width=8, height=2, bg="#7C999B", fg="black", command=lambda b=button: button_click(b))
        btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    else:
        btn = tk.Button(root, text=button, width=8, height=2, bg="#f0f0f0", fg="black", command=lambda b=button: button_click(b))
        btn.grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
# run the application
root.mainloop()
