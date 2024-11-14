"""
grid = is geometry manager that organize in form of table like structure    
"""
from tkinter import *
def submit():
    print("You successfully submited")
window=Tk()

firstNameLabel=Label(window,text="First Name : ").grid(row=0,column=0)
firstNameEntry=Entry(window).grid(row=0,column=1)


lastNameLabel=Label(window,text="Last Name : ").grid(row=1,column=0)
lastNameEntry=Entry(window).grid(row=1,column=1)


emailLabel=Label(window,text="Email : ").grid(row=2,column=0)
emailEntry=Entry(window).grid(row=2,column=1)


submitButton=Button(window,text="Submit",command=submit).grid(row=3,column=0,columnspan=2)

window.mainloop()