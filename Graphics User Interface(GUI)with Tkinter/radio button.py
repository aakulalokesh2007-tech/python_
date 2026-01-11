#radiobutton
from tkinter import *
def fun():
    print("you ordered a ",food[x.get()])
food=["White Rice","curd","Sambar"]
a=Tk()
img=PhotoImage(file="icon.png")
x=IntVar()
for c in range(len(food)):
    b=Radiobutton(a,text=food[c],
                  variable=x,#groups radiobuttons together if they share the same variable
                  value=c,#asssigns each radio button a different value
                  padx=20,font=("Impact",20),image=img,compound=LEFT,
                  indicatoron=0,#eliminate circle indicators
                  width=300,#sets width of radio buton
                  command=fun)
    b.pack(anchor=W)
a.mainloop()
