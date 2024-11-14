from tkinter import*

food=["pizza","hamburger","hotdog"]
def order():
    if (x.get()==0):
        print("You order pizza")
    elif (x.get()==1) :
        print("You order hamburger")   
    elif(x.get()==2):
        print("You order hotdog")
    else:
        print("huh?")        
window=Tk()
x=IntVar()
for index in range(len(food)):
    radio_button=Radiobutton(window,
                             text=food[index],
                             variable=x,
                             value=index,
                             padx=25,
                             font=("Arial",50),
                             command=order,
                             indicatoron=0,#eliminate the circle button
                             width=375
                             ).pack(anchor=W)
window.mainloop()