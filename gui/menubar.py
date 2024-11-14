from tkinter import *

def openFile():
    print("You have been open file")
def saveFile():
   print("You have been save file")
def quit():
    print("You have been exit file")
def cut():
    print("You cut some text ")
def copy():
    print("You copy some text ")
def paste():
    print("You paste some text ")
window=Tk()

openImange=PhotoImage(file="folder.png")
saveImage=PhotoImage(file="folder.png")
exitImage=PhotoImage(file="folder.png")

menubar=Menu(window )

window.config(menu=menubar)

fileMenu=Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile,image=openImange,compound=LEFT)
fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound=LEFT)  



editMenu=Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

window.mainloop()