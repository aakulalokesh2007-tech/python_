from tkinter import *
def w(cr):
    b.place(x=b.winfo_x(),y=b.winfo_y()-10)
def s(cr):
    b.place(x=b.winfo_x(),y=b.winfo_y()+10)
def A(cr):
    b.place(x=b.winfo_x()-10,y=b.winfo_y())
def d(cr):
    b.place(x=b.winfo_x()+10,y=b.winfo_y())

a=Tk()
a.geometry("500x500")
img=PhotoImage(file="mario.png")
b=Label(a,image=img)
b.place(x=10,y=10)






a.bind("<w>",w)
a.bind("<s>",s)
a.bind("<a>",A)
a.bind("<d>",d)
a.bind("<Up>",w)
a.bind("<Down>",s)
a.bind("<Left>",A)
a.bind("<Right>",d)




a.mainloop()
