from tkinter import *
import time
from winsound import *


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
STUDY_MIN = 2
SHORT_BREAK_MIN = 1.5
LONG_BREAK_MIN = 2
my_counter = 0
myTimer = None


def alarm_sound():
    PlaySound('Sound.wav', SND_ALIAS)


def myReset():
    global my_counter
    window.after_cancel(myTimer)
    concave.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer", fg='black')
    my_counter = 0


def starts():
    global my_counter
    my_counter += 1
    study = STUDY_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if my_counter == 6:
        count_down(long_break)
        my_counter = 1
        label1.config(text="L. Break", fg="#fc8621")
    elif my_counter % 2 == 0:
        count_down(short_break)
        label1.config(text="S. Break", fg="red")
    else:
        count_down(study)
        label1.config(text="Study", fg="green4")


def count_down(count):
    global myTimer
    count_minute = count // 60
    count_second = count % 60
    concave.itemconfig(timer_text, text=f"{count_minute:02d}:{count_second:02d}")
    if count > 0:
        myTimer = window.after(1000, count_down, count-1)
    else:
        alarm_sound()
        starts()


window = Tk()
window.title('Study Timer')
label1 = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 25, 'bold'))
label1.grid(row=0, column=1)
window.config(padx=60, pady=50, bg=YELLOW)
concave = Canvas(width=220, height=220, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
concave.create_image(110, 100, image=tomato)
timer_text = concave.create_text(120, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
concave.grid(row=1, column=1)
start = Button(text=' Start ', font=(FONT_NAME, 10, "bold"), relief="ridge", command=starts)
start.grid(row=3, column=0)
reset = Button(text=' Reset ', font=(FONT_NAME, 10, "bold"), relief="ridge", command=myReset)
reset.grid(row=3, column=2)
check_mark = Label(text="", bg=YELLOW)
check_mark.grid(row=2, column=1)


window.mainloop()
