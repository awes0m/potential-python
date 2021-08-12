import math
from tkinter import*
from winsound import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
Checkmark="✔"
reps= 0
timer=None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer
    window.after_cancel(timer)
    global reps
    reps=0
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="Timer")
    start_b["state"] = NORMAL



# ---------------------------- TIMER MECHANISM ------------------------------- # 
import tkinter.messagebox
def start_timer():
    start_b["state"]=DISABLED
    global reps
    reps += 1
    print(reps)
    if reps > 8:
        reset()
    elif reps%8==0:
        tkinter.messagebox.showinfo(title="Break", message="Long break!")
        countdown(LONG_BREAK_MIN*60)
        label.config(text="BREAK",fg=RED)
    elif reps%2==0:
        tkinter.messagebox.showinfo(title="Work", message="Small break!")
        countdown(SHORT_BREAK_MIN*60)
        label.config(text="Break",fg=PINK)
    else :
        tkinter.messagebox.showinfo(title="Work", message="Start working~")
        countdown(WORK_MIN*60)
        label.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    if count_min<10:
        count_min=f"0{count_min}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        timer=window.after(1000,countdown,count-1)
    else:
        start_timer()
        marks = "".join("✔" for _ in range(math.floor(reps/2)))
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro-Time manager")
window.config(padx=100,pady=100,bg=YELLOW)


#Labels
label = Label(text="Timer",fg=PINK,bg=YELLOW,font=(FONT_NAME,40,"bold"))
label.grid(column=2,row=1)
checkmark=Label(fg=PINK,bg=YELLOW,font=(FONT_NAME,40,"bold"))
checkmark.grid(column=2,row=3)

#canvas
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_pic=PhotoImage(file=r"C:\Users\Som D God\Documents\Python projects\time-manage\tomato.png")
canvas.create_image(100,112,image=tomato_pic)
timer_text=canvas.create_text(103,133,text="00:00",fill="white",font=("Times",28,"bold"))
canvas.grid(column=2,row=2)

#Buttons
#calls action() when pressed
start_b= Button(text="Start", command=start_timer,highlightthickness=0)
start_b.grid(column=1,row=3,pady=20)

reset_b= Button(text="Reset", command=reset,highlightthickness=0)
reset_b.grid(column=3,row=3)


window.mainloop()