from tkinter import*

def submit():
    # print("You have ordered :")
    # print(listbox.get(listbox.curselection()))
    food=[]
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have ordered")   
    for i in food:
        print(i)

def add():
    listbox.insert(listbox.size(),entry.get())
    listbox.config(height=listbox.size())

def delete():
   for index in reversed(listbox.curselection()):
       listbox.delete(index)
       listbox.config(height=listbox.size())

window=Tk()

listbox=Listbox(window,
                bg="#f7ffde",
                font=("Constatia",25),
                width=12,
                selectmode=MULTIPLE)
                
listbox.pack()

listbox.insert(0,"Pizza")
listbox.insert(1,"Pasta")
listbox.insert(2,"Sushi")
listbox.insert(3,"Hotdog")
listbox.insert(4,"Hamburger")

listbox.config(height=listbox.size())
entry=Entry(window)
entry.pack()

submit_button=Button(window,text="Submit",command=submit)
submit_button.pack()

add_button=Button(window,text="Add",command=add)
add_button.pack()

delete_button=Button(window,text="Delete",command=delete)
delete_button.pack()
window.mainloop()