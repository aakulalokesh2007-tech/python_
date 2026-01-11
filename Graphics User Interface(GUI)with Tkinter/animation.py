from tkinter import *
import time

WIDTH=500
HEIGHT=500
x_velocity=1
y_velocity=1
a=Tk()

b=Canvas(a,width=WIDTH,height=HEIGHT)
b.pack()

img2=PhotoImage(file="background.png")
bg_img=b.create_image(0,0,image=img2,anchor=NW)

img=PhotoImage(file="icon.png")
b_img=b.create_image(0,0,image=img,anchor=NW)

img_wid=img.width()
img_hei=img.height()

while True:
    coordinates=b.coords(b_img)
    print(coordinates)
    if coordinates[0]>=(WIDTH-img_wid) or coordinates[0]<0:
        x_velocity=-(x_velocity)
    if coordinates[1]>=(HEIGHT-img_hei) or coordinates[1]<0:
        y_velocity=-(y_velocity)
    b.move(b_img,x_velocity,y_velocity)
    a.update()
    time.sleep(0.01)
 

a.mainloop()
