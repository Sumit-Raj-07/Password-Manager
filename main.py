from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import json

grey = "#E2DBDB"

# Random pasword generation-----------------------------------------------------------------------------------
def passwordgenerator():
    num = ['0','1','2','3','4','5','6','7','8','9']
    letters = ['a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    symbols = ['!','@','#','&','_','-']

    pwd_l = [choice(letters) for _ in range(randint(6,8))]
    pwd_n = [choice(num) for _ in range(randint(2,4))]
    pwd_s = [choice(symbols) for _ in range(randint(2,3))]
    pwd_list = pwd_l + pwd_n + pwd_s

    shuffle(pwd_list)
    password = "".join(pwd_list)
    pwd_box.delete(0, END)
    pwd_box.insert(0, password)

# function to save the given inputs in a txt file-------------------------------------------------------------
def save_info():
    web_name = web_box.get()
    email_id = id_box.get()
    pwd = pwd_box.get()
    info = {
        web_name : {
            "email_id" : email_id,
            "password" : pwd
                }
    }

    if web_box.get()=="" or id_box.get()=="" or pwd_box.get()=="":
        messagebox.showerror(title="Warning",message="You need to fill all the details to save.")
    else:
        confirm = messagebox.askyesno(title="Confirm your details",message=f"website = {web_name}\nemail/id = {email_id}\npassword = {pwd}\n Do yo want to save it")
        if confirm:
            try:
                with open("my_paswords.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("my_paswords.json", "w") as file:
                    json.dump(info, file, indent=4)
            else:
                data.update(info)
                with open("my_paswords.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                web_box.delete(0,END)
                pwd_box.delete(0,END)

# Creating the search function--------------------------------------------------------------------------------
def search():
    with open("my_paswords.json", "r") as file:
        search_data = json.load(file)
        website = web_box.get()
        if website in search_data:
            search_id = search_data[website]["email_id"]
            search_pwd = search_data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email/ID = {search_id}\nPassword = {search_pwd}")
        else:
            messagebox.showinfo(title=website,message="No data found")
    pass

# Creating the window-----------------------------------------------------------------------------------------
window = Tk()
window.minsize(width=600,height=600)
window.config(padx=30,pady=30,bg=grey)
window.grid()

# adding the logo through canvas------------------------------------------------------------------------------
lock = PhotoImage(file="lock.png")
canvas = Canvas(width=300,height=300,highlightthickness=0,bg=grey)
canvas.create_image(150,150,image=lock)
canvas.grid(column=1,row=0)

# adding the texts--------------------------------------------------------------------------------------------
web = Label(text="Website",highlightthickness=0,font=("normal",12,"bold"),padx=5,pady=5,bg=grey)
web.grid(column=0,row=1)

id = Label(text="Email / User_ID",highlightthickness=0,font=("normal",12,"bold"),padx=5,pady=5,bg=grey)
id.grid(column=0,row=2)

pwd = Label(text="Pasword",highlightthickness=0,font=("normal",12,"bold"),padx=5,pady=5,bg=grey)
pwd.grid(column=0,row=3)

# adding the input boxes--------------------------------------------------------------------------------------
web_box = Entry(width=35)
web_box.focus()
web_box.grid(column=1,row=1,columnspan=2,sticky="w")

id_box = Entry(width=60)
id_box.grid(column=1,row=2,columnspan=2,sticky="w")

pwd_box = Entry(width=35)
pwd_box.grid(column=1,row=3,sticky="w")

# Adding the buttons-----------------------------------------------------------------------------------------
search_but = Button(text="Search",highlightthickness=0,font=("normal",10),width=15,command=search)
search_but.grid(column=1,row=1,columnspan=2,sticky="e")

pwd_but = Button(text="Pasword",highlightthickness=0,font=("normal",10),width=15,command=passwordgenerator)
pwd_but.grid(column=1,row=3,columnspan=2,sticky="e")

add_but = Button(text="add",highlightthickness=0,font=("normal",12),width=40,command=save_info)
add_but.grid(column=1,row=4,columnspan=2)

window.mainloop()