from tkinter import *
import time
from Ball import *

WIDTH=800
HEIGHT=800
xVelocity=3
yVelocity=2
window=Tk()

canvas=Canvas(window,width=WIDTH,height=HEIGHT,bg="green")
canvas.pack()

volley_ball=Ball(canvas,0,0,100,1,1,"white")
tenis_ball=Ball(canvas,0,0,50,4,3,"yellow")
basket_ball=Ball(canvas,0,0,125,8,7,"orange")
foot_ball=Ball(canvas,0,0,200,6,5,"black")




while True:
    volley_ball.move()
    tenis_ball.move()
    basket_ball.move()
    foot_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()