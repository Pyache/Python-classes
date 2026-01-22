from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Interest Calculator App")

frame = Frame(master=root, height=200, width=360, bg="#5e858d")
frame.place(x=20, y=0)

lbl1 = Label(frame, text="Principle", bg="#5e858d", fg="black", width=12)
lbl2 = Label(frame, text="Time", bg="#5e858d", fg="black", width=12)
lbl3 = Label(frame, text="Rate", bg="#5e858d", fg="black", width=12)

prin_entry = Entry(frame)
time_entry = Entry(frame)
rate_entry = Entry(frame)

def si():
    try:
        p = float(prin_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())
        simple_interest = (p * r * t) / 100
        message = "Simple Interest: " + str(simple_interest)
        textbox.delete("1.0", END)
        textbox.insert(END, message)
    except ValueError:
        textbox.delete("1.0", END)
        textbox.insert(END, "Invalid input. Please enter numbers for Principle, Time, and Rate.")

def ci():
    try:
        p = float(prin_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())
        amount = p * (1 + r / 100) ** t
        compound_interest = amount - p
        message2 = "Compound Interest: " + str(compound_interest)
        textbox.delete("1.0", END)
        textbox.insert(END, message2)
    except ValueError:
        textbox.delete("1.0", END)
        textbox.insert(END, "Invalid input. Please enter numbers for Principle, Time, and Rate.")

lbl1.place(x=20, y=20)
prin_entry.place(x=150, y=20)

lbl2.place(x=20, y=60)
time_entry.place(x=150, y=40)

lbl3.place(x=20, y=100)
rate_entry.place(x=150, y=60)

btn = Button(root, text="Calculate Simple Interest", command=si, bg="orange")
btn2 = Button(root, text="Calculate Compound Interest", command=ci, bg="orange")

btn.place(x=50, y=220)
btn2.place(x=50, y=250)

textbox = Text(master=root, bg="#ffffff", fg="black", height=7, width=40)
textbox.place(x=150, y=100)

root.mainloop()