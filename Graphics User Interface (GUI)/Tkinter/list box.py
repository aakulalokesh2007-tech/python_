from tkinter import *
def fun():
    #print(b.get(b.curselection())) #for single
    for x in b.curselection():
        print(b.get(x))
    d.delete(0,END)
def add():
    b.insert(b.size(),d.get())
    b.config(height=b.size())
    d.delete(0,END)
def de():
    #b.delete(b.curselection())#for single
    for x in reversed(b.curselection()):
        b.delete(x)
        
    b.config(height=b.size())
    
a=Tk()
b=Listbox(a,bg="brown",font=("constantia",20),fg="white",
          width=30,
          selectmode=MULTIPLE)#to select muti items
b.pack()
b.insert(0,"pizza")
b.insert(1,"curd")
b.insert(2,"sambar")
b.insert(3,"rice")
b.insert(4,"upma")

b.config(height=b.size())

c=Button(a,text="sumit",command=fun)
c.pack()

d=Entry(a)
d.pack()

e=Button(a,text="ADD",command=add)
e.pack()

f=Button(a,text="delete",command=de)
f.pack()
a.mainloop()
