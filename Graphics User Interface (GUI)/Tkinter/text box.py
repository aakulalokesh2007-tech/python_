from tkinter import *
from tkinter import *
def sum():
    print(b.get("1.0",END))
a=Tk()
b=Text(a,bg="light yellow",font=("Ink free",20),fg="blue",height=8,width=10,padx=30,pady=10)
b.pack()
c=Button(a,text="summit",command=sum)
c.pack()
a.mainloop()

