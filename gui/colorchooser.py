from tkinter import*
from tkinter import colorchooser

def click():
    color=colorchooser.askcolor()
    # print(color)
    window.config(bg=color[1])
window=Tk()
window.geometry("420x420")

button=Button(window,text="Click me",command=click)
button.pack()

window.mainloop()