from tkinter import *
def w(cr):
    b.move(canvasimage,0,-10)
def s(cr):
    b.move(canvasimage,0,10)
def A(cr):
    b.move(canvasimage,-10,0)
def d(cr):
    b.move(canvasimage,10,0)
a=Tk()
b=Canvas (a,width=500,height=500)
b.pack()

img=PhotoImage(file="mario.png")
canvasimage=b.create_image(0,0,image=img,anchor=NW)


a.bind("<w>",w)
a.bind("<s>",s)
a.bind("<a>",A)
a.bind("<d>",d)

a.mainloop()
