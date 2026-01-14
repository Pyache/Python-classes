from tkinter import *
from datetime import date

root = Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")
label_ = Label(text="Hey, there!", fg="black", bg="#ff9100", height=1, width= 300)
label_.pack()
name_label = Label(text="Full Name", bg="#ff9100")
name_label.pack()
name_entry = Entry()
name_entry.pack()

def display():
    name = name_entry.get()
    global message
    message = "Welcome to the Application! " \
    "\nToday's date is: "
    greet = "Hello " + name + "\n"
    
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box = Text(height = 3)
button_ = Button(text="Begin", command=display, height=1, 
                 bg = "#ff9100", fg="black")
button_.pack()
text_box.pack()
root.mainloop()


from tkinter import *
root = Tk()
root.title("Getting Started with Widgets")
root.geometry("500x500")
root.mainloop()