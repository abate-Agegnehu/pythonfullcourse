
from tkinter import *
from tkinter import messagebox#import messagebox library

def click():
    # messagebox.showinfo(title="This is an infor message box",message="You are a person")
    # messagebox.showerror(title="ERROR",message="something went wrong")
    # messagebox.showwarning(title="WARNING",message="YOU HAVE A VIRUS")
#    if messagebox.askokcancel(title="ask ok cancel",message="Do you want to do thing"):
#       print("You did thing")
#    else:
#       print("You canceled a thing")
#    if messagebox.askretrycancel(title="ask retry cancel",message="Do you want to retry a thing"):
#       print("You retried thing")
#    else:
#       print("You canceled a thing")
#    if messagebox.askyesno(title="ask yes  or no",message="Do you like cake?"):
#       print("I like cake too")
#    else:
#       print("Why you don't like cake?")
    #  print(messagebox.askquestion(title="ask question",message="Do you like pie!"))
    #  answer=messagebox.askquestion(title="ask question",message="Do you like pie!")
    #  if (answer=="yes"):
    #       print("I like to pie!")
    #  else:
    #       print("Why you don't like pie?")

       answer= messagebox.askyesnocancel(title="yes no cancel",message="Do you like to code?")
       if(answer==True):
              print("I like too")
       elif(answer==False):
              print("Why you dont like")   
       elif(answer==None):
              print("Huh?")       


window=Tk()

button=Button(window,command=click,text="Click Me")
button.pack()

window.mainloop()