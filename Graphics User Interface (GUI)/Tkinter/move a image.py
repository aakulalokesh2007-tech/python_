from tkinter import *

def q(ev):
    y=b.winfo_y() - 10
    b.place(y=y)
    
    



a=Tk()
a.geometry("500x500")

img=PhotoImage(file="mario.png")
b=Label(a,image=img)
b.place(x=100,y=200)
a.bind("<w>",q)


a.mainloop()
