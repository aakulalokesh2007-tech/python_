#scale
from tkinter import *
def fun():
    print(s.get())
a=Tk()
img=PhotoImage(file=("mario.png"))
la=Label(a,image=img)
la.pack()
s=Scale(a,from_=100,to=0,
        length=500,
        orient=VERTICAL,#DEFAULT 2.HORIZONTAL
        font=("CONSOLAS",25),
        tickinterval=10,#adds numeric indicators
        #showvalue=0,#hides current value
        resolution=5,#increment of slider
        troughcolor="lightblue",#scale line
        fg="green",
        bg="purple")
s.set(20)#to define a default value to scale
s.pack()
b=Button(a,text="sumit",command=fun)
b.pack()
a.mainloop()
