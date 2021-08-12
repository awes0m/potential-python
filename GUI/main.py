from tkinter import *
import turtle

window=Tk()
window.title("GUIIIIIIII")
window.minsize(width=600,height=400)
window.config(padx=100,pady=200)

#Label1
my_label=Label(text="This is the Label",font=("Arial",24,"bold"))
my_label.grid(column=2,row=1)

#Label2
my_label2=Label(text="This is the result",font=("Arial",24,"bold"))
my_label2.grid(column=2,row=4)
#Button
def button_click():
    print("button clicked")
    my_label2.config(text=t_input.get())

button=Button(text="click",command=button_click)
button.grid(column=2, row=3)

#Entry
t_input=Entry(width=10)
t_input.grid(column=2, row=2)
window.mainloop()