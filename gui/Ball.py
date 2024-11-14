class Ball:
    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color) :
                self.canvas=canvas
                self.image=canvas.create_oval(x,y,diameter,diameter,fill=color)
                self.xVelocity=xVelocity
                self.yVelocity=yVelocity

    def move(self):
            coordinate=self.canvas.coords(self.image)
            # print(coordinate)   

            if(coordinate[2]>=(self.canvas.winfo_width())or coordinate[0]<0):
               self.xVelocity=-self.xVelocity
            if(coordinate[3]>=(self.canvas.winfo_height())or coordinate[1]<0):
               self.yVelocity=-self.yVelocity
            self.canvas.move(self.image,self.xVelocity,self.yVelocity)         
               
