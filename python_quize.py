import tkinter as tk
from tkinter import messagebox

# ------------------ Questions Data ------------------
questions = [
    {"q": "What is the capital of India?", "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"], "ans": "Delhi"},
    {"q": "Which language is used for GUI in Python?", "options": ["C++", "Java", "Tkinter", "HTML"], "ans": "Tkinter"},
    {"q": "What is 5 + 3?", "options": ["5", "8", "10", "15"], "ans": "8"},
    {"q": "Which one is a loop in Python?", "options": ["if", "for", "def", "print"], "ans": "for"},
    {"q": "What is the output of print(2*3)?", "options": ["5", "6", "23", "Error"], "ans": "6"},
    {"q": "Which symbol is used for comments in Python?", "options": ["//", "#", "/*", "--"], "ans": "#"},
]

# ------------------ Variables ------------------
current_q = 0
score = 0
time_left = 10
timer_id = None

# ------------------ Functions ------------------
def load_question():
    global time_left, timer_id
    time_left = 10
    timer_label.config(text=f"Time Left: {time_left}s")

    selected_option.set("")

    q_data = questions[current_q]
    question_label.config(text=f"Q{current_q+1}. {q_data['q']}")

    for i in range(4):
        radio_buttons[i].config(
            text=q_data["options"][i],
            value=q_data["options"][i],
            fg="black",
            state="normal"
        )

    next_btn.config(state="disabled")
    start_timer()

def start_timer():
    global time_left, timer_id
    if time_left > 0:
        timer_label.config(text=f"Time Left: {time_left}s")
        time_left -= 1
        timer_id = root.after(1000, start_timer)
    else:
        check_answer(auto=True)

def check_answer(auto=False):
    global score, current_q, timer_id

    if timer_id:
        root.after_cancel(timer_id)

    selected = selected_option.get()
    correct = questions[current_q]["ans"]

    # Disable options
    for rb in radio_buttons:
        rb.config(state="disabled")

    # Color feedback
    for rb in radio_buttons:
        if rb.cget("text") == correct:
            rb.config(fg="green")
        elif rb.cget("text") == selected:
            rb.config(fg="red")

    if selected == correct:
        score += 1

    next_btn.config(state="normal")

def next_question():
    global current_q
    current_q += 1
    if current_q < len(questions):
        load_question()
    else:
        show_result()

def show_result():
    result_win = tk.Toplevel(root)
    result_win.title("Result")
    result_win.geometry("300x200")

    percent = (score / len(questions)) * 100

    tk.Label(result_win, text="Quiz Finished!", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(result_win, text=f"Your Score: {score} / {len(questions)}", font=("Arial", 12)).pack(pady=5)
    tk.Label(result_win, text=f"Percentage: {percent:.2f}%", font=("Arial", 12)).pack(pady=5)

    if percent >= 50:
        msg = "Good Job! 🎉"
    else:
        msg = "Keep Practicing! 💪"

    tk.Label(result_win, text=msg, font=("Arial", 12)).pack(pady=10)

    tk.Button(result_win, text="Close", command=root.destroy).pack(pady=10)

# ------------------ GUI ------------------
root = tk.Tk()
root.title("Advanced Quiz App")
root.geometry("500x400")

question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=450)
question_label.pack(pady=20)

timer_label = tk.Label(root, text="Time Left: 10s", font=("Arial", 12), fg="blue")
timer_label.pack()

selected_option = tk.StringVar()

radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=selected_option, value="", font=("Arial", 12))
    rb.pack(anchor="w", padx=50, pady=5)
    radio_buttons.append(rb)

check_btn = tk.Button(root, text="Check Answer", command=lambda: check_answer(auto=False), font=("Arial", 12))
check_btn.pack(pady=10)

next_btn = tk.Button(root, text="Next", command=next_question, font=("Arial", 12), state="disabled")
next_btn.pack(pady=10)

# Load first question
load_question()

root.mainloop()