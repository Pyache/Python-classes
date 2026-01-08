from tkinter import *
def multiply():
    try:
        number1 = float(input1.get())
        number2 = float(input2.get())
        answer = number1 * number2
        result.delete("1.0", END)
        result.insert(END, f"Answer: {answer}")
    except:
        result.delete("1.0", END)
        result.insert(END, "Please type numbers only!")
widget = Tk()
widget.geometry("400x300")
widget.title("Multiply Two Numbers")
info1 = Label(widget, text="Type two numbers to multiply.")
info1.pack(pady=5)
label1 = Label(widget, text="First number:")
label1.pack()
input1 = Entry(widget)
input1.pack()
label2 = Label(widget, text="Second number:")
label2.pack()
input2 = Entry(widget)
input2.pack()
button = Button(widget, text="Multiply", command=multiply)
button.pack(pady=10)
result = Text(widget, height=2, width=30)
result.pack(pady=5)
widget.mainloop()