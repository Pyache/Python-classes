from tkinter import *

root = Tk()
root.title("Number pad")
root.geometry("250x300")

nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["#", 0, "*"]]

for i in range(4):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=75)
    for j in range(0, 3):
        frame = Frame(master=root,
                      relief=RAISED,
                      borderwidth=1)
        frame.grid(row=i, column=j)
        label1 = Button(master=frame, text=nums[i][j], bg="#00ff73")
        label1.pack(padx=3, pady=3)
root.mainloop()

#-------------------------------------------------------

from tkinter import *
root = Tk()
root.title("Pymail account")
root.geometry("400x400")

frame = Frame(master=root, height=200, width=360, bg="#00ff73")
lbl1 = Label(frame, text="Full name", bg="#00ff73",
             fg="black", width=12)
lbl2 = Label(frame, text="Pymail ID", bg="#00ff73",
             fg="black", width=12)
lbl3 = Label(frame, text="Enter Password", bg="#00ff73",
             fg="black", width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

def display():
    name = name_entry.get()
    greet = "Hey " + name
    message = "\nCongratulations! You just created a " \
    "pymail account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(bg="#00ff73", fg="black")
btn = Button(text="Create account", command=display, bg="orange")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
pass_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)
root.mainloop()