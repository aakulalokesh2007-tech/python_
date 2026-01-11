from tkinter import *
a=Tk()

fra=Frame(a,bg="blue",bd=7,#border
          relief=SUNKEN,#type of border
          )
fra.pack(side=BOTTOM)
Button(fra,text="W",font=("consolas",25),width=3).pack(side=TOP)
Button(fra,text="A",font=("consolas",25),width=3).pack(side=LEFT)
Button(fra,text="S",font=("consolas",25),width=3).pack(side=LEFT)
Button(fra,text="D",font=("consolas",25),width=3).pack(side=LEFT)


a.mainloop()
