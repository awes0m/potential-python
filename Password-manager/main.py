from  tkinter import messagebox
from  tkinter import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

from random import randint,shuffle,choice
def password_generator():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters=[choice(letters) for _ in range(nr_letters)]
    password_symbols=[choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[choice(numbers) for _ in range(nr_numbers)]
    password_list = password_numbers+password_symbols+password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    if len(website)==0 or len(password)==0 or len(email)==0:
        messagebox.showinfo(title="Oops!",message= "1 or more fields are empty")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"Details entered are \n Email= {email} \n Password={password}")

        if is_ok:
            with open("data.csv","a") as data_file:
                data_file.write(f" {website}, {email}, {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
logo=PhotoImage(file=r"Password-manager/logo.png")
canvas.create_image(100,100,image=logo)
canvas.create_text(100,190,text="(pas-secure)",fill="Black",font=("Times",12,"bold"))
canvas.grid(row=0,column=1)

#Labels
website_label=Label(text="Website")
website_label.grid(column=0,row=1)

email_label=Label(text="Email/Userame")
email_label.grid(column=0,row=2)

password_label=Label(text="Password")
password_label.grid(column=0,row=3)

#Entry
website_entry=Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2,sticky="EW")
website_entry.focus()

email_entry=Entry(width=35)
email_entry.insert(0,"dgr8@gmail.com")
email_entry.grid(column=1,row=2,columnspan=2,sticky="EW")

password_entry=Entry(width=21)
password_entry.grid(column=1,row=3,sticky="EW")

#Buttons
generatePassword_b=Button(text="Generate Password",command=password_generator)
generatePassword_b.grid(column=2,row=3)

add_b=Button(text="Add",width=36,command=save)
add_b.grid(column=1,row=4,columnspan=2,sticky="EW")

window.mainloop()

