#canvas=widget that used to draw graphs,plots,images in a window

from tkinter import *

window=Tk()
canvas=Canvas(window,width=500,height=500)
canvas.pack()
# canvas.create_line(0,0,500,500,fill="blue",width=5) 
# canvas.create_line(0,500,500,0,fill="red",width=5)
# canvas.create_rectangle(50,50,250,250,fill="purple")

canvas.create_arc(0,0,500,500,fill="red",width=10,extent=180)
canvas.create_arc(0,0,500,500,fill="white",width=10,extent=180,start=180)


window.mainloop()   