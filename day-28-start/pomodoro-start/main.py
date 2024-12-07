import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text="LongBreak", fg=RED)
        count_down(long_break)
    elif reps % 2 == 0:
        timer_label.config(text="ShortBreak", fg=PINK)
        count_down(short_break)
    else:
        timer_label.config(text="Work")
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """count down"""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = (math.floor(reps/2))
        for _ in range(work_sessions):
            mark += "✔ "
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

##window config
window = Tk()
window.title("Pomodoro")
window.config(padx=80, pady=60, bg=YELLOW)


#timer label
timer_label = Label()
timer_label.config(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40), pady=10)
timer_label.grid(column=1, row=0)


##canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
## path to image location
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.grid(column=1, row=1)


## timer in the middle of tomato
timer_text = canvas.create_text(100, 137, text="00:00", font=(FONT_NAME, 35, "bold"))


##buttons configs
start = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", highlightbackground=YELLOW,command=reset_timer)
reset.grid(column=2, row=2)

##check mark config
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)












window.mainloop()