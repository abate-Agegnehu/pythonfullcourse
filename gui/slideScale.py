from tkinter import*
def submit():
    print(f"The temprature is {scale.get()} degree C")
window=Tk()


scale=Scale(window,
            from_=100,
            to=0,
            length=500,
            orient=VERTICAL,
            font=("Consolas",20),
            tickinterval=10,
            # showvalue=0,
            # resolution=5,
            troughcolor="#69EAFF",
            fg="#FF1C00", 
            bg="#111111"
            )
# scale.set(50)
scale.set(((scale["from"]-scale["to"])/2)+scale["to"])
scale.pack()

submit_button=Button(window,text="Submit",command=submit)
submit_button.pack()
window.mainloop()