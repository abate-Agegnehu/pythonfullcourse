from tkinter import*

window=Tk()
# window.geometry("430x430")
window.title("GUI learnig window")
# icon=PhotoImage(file='logo.png')
# window.iconphoto(True,icon)
# window.config(bg="#FF0000")
"""
label=is an area widget that hold text and /or an image within a window
"""
potho=PhotoImage(file='logo.png')
label=Label( 
            window,
            text="GUI IN PYTHON",
            font=("Arial",40,"bold"),
            fg="#00FF00",
            bg="#000000",
            relief=SUNKEN ,#or RAISED
            bd=10,
            padx=20,
            pady=20,
            image=potho,
            compound="bottom"
            )
# label.place(x=0,y=0)
label.pack()
window.mainloop()
