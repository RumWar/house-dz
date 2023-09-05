from tkinter import *

def clicked():
    btn.configure(text="WoW")

window = Tk()
window.title("W")
window.geometry('200x200')
lbl = Label(window, text="", fg="red")
lbl.grid(column=0, row=0)
btn = Button(window, text="W", font=("Arial Bold", 50), bg="black", fg="red", command=clicked)
btn.grid(column=1, row=1)


window.mainloop()

