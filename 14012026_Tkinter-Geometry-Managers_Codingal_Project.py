from tkinter import *
from datetime import datetime

root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

frame = Frame(master=root, height=200, width=360, bg="#00ff73")

lbl1 = Label(frame, text="Full name", bg="#00ff73",
             fg="black", width=12)
lbl3 = Label(frame, text="Year", bg="#00ff73",
             fg="black", width=12)

name_entry = Entry(frame)
year_entry = Entry(frame)

def display():
    name = name_entry.get()
    date1 = datetime.today()
    year = date1.year
    yearsub = int(year_entry.get())
    year2 = year - yearsub
    message = name + " is " + str(year2) + " years old."
    textbox.insert(END, message)

textbox = Text(bg="#00ff73", fg="black")
btn = Button(text="Calculate Age", command=display, bg="orange")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
year_entry.place(x=150, y=140)
lbl3.place(x=20, y = 140)
btn.place(x=130, y=210)
textbox.place(y=250)
root.mainloop()
