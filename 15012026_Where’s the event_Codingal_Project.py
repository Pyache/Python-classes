from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Length Converter App")

frame = Frame(master=root, height=400, width=400, bg="#000000")
frame.pack(pady=10)

info1 = Label(frame, text="Enter a length in inches")
label1 = Label(frame, text="Length (in inches): ")
input1 = Entry(frame)

def convert():
    inches = float(input1.get())
    answer = inches * 2.54
    result.delete("1.0", END)
    result.insert(END, f"Answer: {answer} cm")

button = Button(frame, text="Convert", command=convert)
result = Text(frame, height=2, width=30)

info1.pack()
label1.pack()
input1.pack()
button.pack()
result.pack()

root.mainloop()