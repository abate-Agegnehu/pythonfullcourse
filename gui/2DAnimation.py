from tkinter import *
import time


WIDTH=500
HEIGHT=500
xVelocity=3
yVelocity=2
window=Tk()

canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
# backgroud_photo=PhotoImage(file="photo  .png")
# background=canvas.create_image(0,0,image=backgroud_photo)

photo_image=PhotoImage(file="folder.png")
my_image=canvas.create_image(0,0,image=photo_image)




image_width=photo_image.width()
image_heigth=photo_image.height()

while True:
    coordinate=canvas.coords(my_image)
    print(coordinate)

    if(coordinate[0]>=WIDTH-image_width or coordinate[0]<0):
        xVelocity =-xVelocity
    if(coordinate[1]>=HEIGHT-image_heigth or coordinate[1]<0):
        yVelocity =-yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)


window.mainloop()