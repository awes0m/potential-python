def miletokm():
    a=float(u_input.get())
    b=a*1.609
    result.config(text=b)

from tkinter import *

window=Tk()
window.minsize(width=100,height=100)
window.config(padx=90,pady=20)
window.title("Mile to km converter")


#Entry
u_input=Entry(width=5)
g=u_input.get()
u_input.grid(column=2,row=1)

#Label
label1=Label(text=" Miles")
label1.grid(column=3,row=1)

label2=Label(text="is Equal to")
label2.grid(column=1,row=2)

label3=Label(text="Km")
label3.grid(column=3,row=2)

result=Label(text="0")
result.grid(column=2,row=2)


#Button
but_on=Button(text="Calculate",command=miletokm)
but_on.grid(column=2,row=3)

window.mainloop()
