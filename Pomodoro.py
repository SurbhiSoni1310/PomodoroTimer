from tkinter import *
import math
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
part = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    label.config(text="TIMER")
    canvas.itemconfig(timer_text, text="00:00")
    label_check.config(text="")
    global part
    part = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global part
    part += 1
    working_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if part % 8 == 0:
        playsound("mixkit-happy-bells-notification-937.wav")
        countdown(long_break_sec)
        label.config(text="LONG BREAK", fg=RED)
    elif part % 2 == 0:
        playsound("mixkit-happy-bells-notification-937.wav")
        countdown(break_sec)
        label.config(text="SHORT BREAK", fg=PINK)
    else:
        playsound("mixkit-happy-bells-notification-937.wav")
        countdown(working_sec)
        label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 or count_sec <= 9:
        count_sec = f"0{count_sec}"
    if count > 0:
        global timer
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        working_sessions = math.floor(part / 2)
        for _ in range(0, working_sessions):
            mark += text
        label_check.config(text=mark)
        label_check.grid(row=3, column=1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
label = Label(text="TIMER", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
label.grid(row=0, column=1)
button_start = Button(bg=YELLOW, fg=RED, text="START", font=(FONT_NAME, 12, "bold"), highlightthickness=0,
                      command=start_timer)
button_start.grid(row=2, column=0)
button_reset = Button(bg=YELLOW, fg=RED, text="RESET", font=(FONT_NAME, 12, "bold"), highlightthickness=0,
                      command=reset_timer)
button_reset.grid(row=2, column=2)
text = "✔"
label_check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))

window.mainloop()
