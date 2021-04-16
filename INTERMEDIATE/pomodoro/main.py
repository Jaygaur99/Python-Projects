from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    start_button.config(state=NORMAL)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start_button.config(state=DISABLED)
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_secs)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_secs)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # Getting hold on the seconds and minutes to show on the canvas
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # Method of canvas like config() of other widgets
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ''
        work_sessions = floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# Creating a Window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100, bg=YELLOW)


# Creating a Label
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, 'bold'), bg=YELLOW)
title_label.grid(column=1, row=0)


# Creating the Canvas
# highlightthickness=0 shows that we should not have any border visible around the canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Canvas can not directly get an image, Instead it need PhotoImage to load an image to the create_image to canvas
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
# Creating a variable "timer_text" in order to pass it into the canvas.itemconfig() to get the required functionality
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


# Button to Start the Timer and Reset
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
check_marks.grid(column=1, row=3)

window.mainloop()
