from tkinter import*
def move_up(event):
    canvas.move(my_image,0,-10)

def move_down(event):
       canvas.move(my_image,0,10)

def move_right(event):
        canvas.move(my_image,10,0)
   
def move_left(event):
        canvas.move(my_image,-10,0)
  
    
window=Tk()


canvas=Canvas(window,width=500,height=500)
canvas.pack()

photo_image=PhotoImage(file="folder.png")
my_image=canvas.create_image(0,0,image=photo_image,anchor=NW)




window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

window.mainloop()