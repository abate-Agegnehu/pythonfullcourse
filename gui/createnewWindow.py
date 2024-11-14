from tkinter import*
def click():
    print("You clicked me in other window") 
def create_window():
    # newwindow=Toplevel()#new window on to of other window 
    # Button(newwindow,text="Click Me",command=click).pack()
     new_window=Tk()#new independent window 
     Button(new_window,text="Click Me",command=click).pack()
     old_window.destroy()#close out of old window
old_window=Tk()

Button(old_window,text="Create new window",command=create_window).pack()
old_window.mainloop()