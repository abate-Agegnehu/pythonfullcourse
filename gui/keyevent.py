from tkinter import*

def doSomething(event):
    print("You clicked "+event.keysym)

window=Tk()
window.bind("<Key>",doSomething)
window.mainloop()