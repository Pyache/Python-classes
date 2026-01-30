from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.geometry("400x400")
root.title("Rock Paper Scissors Game")

lbl1 = Label(text="Welcome to the game!", fg="black", bg="light blue", height=3, width=20)
lbl1.pack()

# Harika ma'am, I'll miss you a lot. That day, when I had my class,
# the reason why my camera was off was because, I couldn't face my tears and started weeping/crying
# Ma'am, thank you for everything...
# print("I'll always remeber you ma'am...")

def ok():
    top = Toplevel(root)
    top.geometry("300x300")
    top.title("Choose: ")
    lbl2 = Label(top, text="Choose: ")
    lbl2.pack()
    rockbtn = Button(top, text="Rock 🪨", command=rock)
    rockbtn.pack()
    paperbtn = Button(top, text="Paper 📄", command=paper)
    paperbtn.pack()
    scissorsbtn = Button(top, text="Scissors ✂️", command=scissors)
    scissorsbtn.pack()

def rock():
    comp_options = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(comp_options)
    user_choice = "Rock"
    if comp_choice == "Rock":
        text1 = "It's a tie!"
    elif comp_choice == "Paper":
        text1 = "Computer wins!"
    else:
        text1 = "You win!"
    
    result = messagebox.showinfo(("Who won the game?"), ("You chose:", user_choice, "and the computer chose:", comp_choice, "So the result is:", text1))

def paper():
    comp_options = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(comp_options)
    user_choice = "Paper"
    if comp_choice == "Paper":
        text1 = "It's a tie!"
    elif comp_choice == "Scissors":
        text1 = "Computer wins!"
    else:
        text1 = "You win!"
    
    result = messagebox.showinfo(("Who won the game?"), ("You chose:", user_choice, "and the computer chose:", comp_choice, "So the result is:", text1))

def scissors():
    comp_options = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(comp_options)
    user_choice = "Scissors"
    if comp_choice == "Scissors":
        text1 = "It's a tie!"
    elif comp_choice == "Rock":
        text1 = "Computer wins!"
    else:
        text1 = "You win!"

    result = messagebox.showinfo(("Who won the game?"), ("You chose:", user_choice, "and the computer chose:", comp_choice, "So the result is:", text1))

startbtn = Button(text="Start Game", command=ok)
startbtn.pack()

root.mainloop()