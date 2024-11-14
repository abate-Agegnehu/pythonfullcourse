from tkinter import*
count=0
def printsomthing():
    global count
    count+=1
    print(count)
window=Tk()

"""
button=you can click and you can do stuff
"""
image=PhotoImage(file='logo.png')
button=Button(window,
              command=printsomthing,
              text="Click me",
              font=("Comic Sans",30),
              fg="#00FF00",
              bg="#000000",
              activeforeground="#00FF00",
              activebackground="#000000",
              image=image,
              compound="bottom"
            #   state=ACTIVE
            #   state=DISABLED,
              )
button.pack()

window.mainloop()