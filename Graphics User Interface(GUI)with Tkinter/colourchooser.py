from tkinter import *
from tkinter import colorchooser as x
def col():
    v=x.askcolor()
    a.config(bg=v[1])
a=Tk()
a.geometry("420x420")
b=Button(a,text="pick color",command=col)
b.pack()
a.mainloop()
