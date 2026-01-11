from tkinter import *
a=Tk()

Label(a,text="ENTER YOUR INFO").grid(row=0,column=0,columnspan=2)


fnl=Label(a,text="FIRST NAME:",width=20,bg="red")
fne=Entry(a)

fnl.grid(row=1,column=0)
fne.grid(row=1,column=1)


lnl=Label(a,text="LAST NAME:",bg="green")
lne=Entry(a)

lnl.grid(row=2,column=0)
lne.grid(row=2,column=1)


lnl=Label(a,text="EMAIL :",bg="blue",width=30)
lne=Entry(a)

lnl.grid(row=3,column=0)
lne.grid(row=3,column=1)



Button(a,text="sumit").grid(row=4,column=0,columnspan=2)

a.mainloop()
