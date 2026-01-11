from tkinter import *
def func(ev):
    global c
    c.set(ev.keysym)
a=Tk()
c=StringVar()
a.bind("<Key>",func)
b=Label(a,textvariable=c,font=("BOLD",37),bg="blue")
b.pack()
a.mainloop()
