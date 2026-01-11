from tkinter import *
def open():
    print("opened")
def close():
    print("closed")
def save():
    print("saved")

def edit():
    print("edited")
def crop():
    print("croped")
def trim():
    print("trimed")
def cut():
    print("cuted")

a=Tk()
img=PhotoImage(file="red dot.png")
b=Menu(a)

a.config(menu=b)

c=Menu(b,tearoff=0)
b.add_cascade(label="file",menu=c)

c.add_command(label="open",command=open)
c.add_command(label="close",command=close)
c.add_command(label="save",command=save)

c.add_separator()#draw a line 

c.add_command(label="exit",command=quit,image=img,compound="left")





e=Menu(b,tearoff=0)

b.add_cascade(label="edit",menu=e)
e.add_command(label="crop",command=crop,image=img,compound="left")
e.add_command(label="trim",command=trim)
e.add_command(label="cut",command=cut)
              

a.mainloop()
