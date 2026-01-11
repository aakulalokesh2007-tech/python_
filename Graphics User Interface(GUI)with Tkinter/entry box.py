from tkinter import*
def su():
    a=ent.get()
    ent.delete(0,END)
    print(a)
    #ent.config(state=DISABLED)
def de():
    ent.delete(0,END)
def bac():
    ent.delete(len(ent.get())-1,END)
a=Tk()
ent=Entry(a,font=("Arial",50),fg="red",bg="blue",#show="*"
          )
#ent.insert(0,"hello world")default value
ent.pack(side=LEFT)
but2=Button(a,text="delete",command=de)
but2.pack(side=RIGHT)
but=Button(a,text="sumit",command=su)
but.pack(side=RIGHT)
back=Button(a,text="back sapce",command=bac)
back.pack(side=RIGHT)
a.mainloop()
