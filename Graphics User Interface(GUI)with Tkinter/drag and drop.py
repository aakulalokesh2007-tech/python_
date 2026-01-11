from tkinter import *
def fun(ev):
    we=ev.widget
    we.startx = ev.x
    we.starty=ev.y
    

def fun1(ev):
    we=ev.widget
    x=we.winfo_x() - we.startx  + ev.x
    y=we.winfo_y() - we.starty + ev.y
    we.place(x=x,y=y)
    
    
a=Tk()

a.geometry("300x300")



label=Label(a,bg="red",width=10,height=5)
label.place(x=0,y=0)
label.bind("<Button-1>",fun)
label.bind("<B1-Motion>",fun1)



label2=Label(a,bg="blue",width=15,height=3)
label2.place(x=50,y=20)
label2.bind("<Button-1>",fun)
label2.bind("<B1-Motion>",fun1)



a.mainloop()
