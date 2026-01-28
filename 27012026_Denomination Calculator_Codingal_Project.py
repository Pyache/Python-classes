from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Length Converter App")

lbl1 = Label(root, text="Enter your password:", bg="light green")
lbl1.pack(pady=5)

ask = Entry(root, show="*")
ask.pack(pady=5)

text_box = Text(root, height=2, width=40)
text_box.pack(pady=5)
text_box.insert(END, "Welcome to the Application!\nThe strength of your password is:")
text_box.config(state=DISABLED)

text_box2 = Text(root, height=1, width=20, fg="black")
text_box2.pack(pady=5)
text_box2.config(state=DISABLED)

def check():
    password = ask.get()
    value = len(password)
    message_ = ""
    a = ""
    
    if value <= 5:
        message_ = "Weak"
        a = "Red"
    elif value <= 8:
        message_ = "Medium"
        a = "Yellow"
    elif value <= 12:
        message_ = "Strong"
        a = "Light Green"
    else:
        message_ = "Very Strong"
        a = "Dark Green"

    text_box2.config(state=NORMAL)
    text_box2.delete(1.0, END)
    text_box2.insert(END, message_)
    text_box2.config(fg=a)
    text_box2.config(state=DISABLED)

btn = Button(root, text="Check Strength", command=check)
btn.pack(pady=10)

root.mainloop()
