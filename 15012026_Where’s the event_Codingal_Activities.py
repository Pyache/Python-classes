from tkinter import *
from tkinter import messagebox

'''window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def handle_keypress(event):
    print(event.char)
window.bind("<Key>", handle_keypress)
def handle_click(event):
    print("The button was clicked!")

btn = Button(text="Click me!", bg="#ffa600", fg="black")
btn.pack()

btn.bind("<Button-1>", handle_click)
window.mainloop()'''


root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert!", "Stop! Virus Found.")

btn = Button(root, text="Scan for Virus", command=msg)
btn.place(x=40, y=80)
root.mainloop()
