# I did not get time to do the project, but I didn't want my points to get cut too.. So ma'am please give one more chance to submit this project!
from tkinter import *
from datetime import datetime
# I did not get time to do the project, but I didn't want my points to get cut too.. So ma'am please give one more chance to submit this project!
root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

frame = Frame(master=root, height=200, width=360, bg="#00ff73")
lbl1 = Label(frame, text="Full name", bg="#00ff73",
             fg="black", width=12)
lbl2 = Label(frame, text="Date (numerical)", bg="#00ff73",
             fg="black", width=12)
lbl3 = Label(frame, text="Month", bg="#00ff73",
             fg="black", width=12)
lbl4 = Label(frame, text="Year", bg="#00ff73",
             fg="black", width=12)

# I did not get time to do the project, but I didn't want my points to get cut too.. So ma'am please give one more chance to submit this project!

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame)
year_ = Entry(frame)
# I did not get time to do the project, but I didn't want my points to get cut too.. So ma'am please give one more chance to submit this project!
def display():
    name = name_entry.get()
    date1 = datetime.today()
    year = date1.year
    message = name + " is " + int(year2) + "years old"
    year2 = int(year) - email_entry
    textbox.insert(END, message)

textbox = Text(bg="#00ff73", fg="black")
btn = Button(text="j", command=display, bg="orange")
# I did not get time to do the project, but I didn't want my points to get cut too.. So ma'am please give one more chance to submit this project!
frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
pass_entry.place(x=150, y=140)
lbl4.place(x=20, y = 200)
btn.place(x=130, y=210)
textbox.place(y=250)
root.mainloop()