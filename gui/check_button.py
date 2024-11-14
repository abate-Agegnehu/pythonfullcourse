from tkinter import*

def display():
    if(x.get()):
        print("You agree to do somthing")
    else :
        print("You don't agree to do something")    
window=Tk()

x=IntVar( )
photo=PhotoImage(file='logo.png')
check_button=Checkbutton(window,
                         text="I agree with something",
                         variable=x,
                         onvalue=1,
                         offvalue=0,
                         command=display,
                         font=("Arial",20),
                         fg="#00FF00",
                         bg="#000000",
                         activeforeground="#00FF00",
                         activebackground="#000000",
                         image=photo,
                         compound=RIGHT
                         ).pack()
window.mainloop()