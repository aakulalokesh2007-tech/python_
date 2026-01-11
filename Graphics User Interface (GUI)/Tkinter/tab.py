from tkinter import *
from tkinter import ttk

a=Tk()

note=ttk.Notebook(a)#widget that manages a collection of windows/displays

tab1=Frame(note)
tab2=Frame(note)

note.add(tab1,text="tab1")
note.add(tab2,text="tab2")
note.pack(expand=True,#=to fill any space not otherwise used
            fill="both"#wil fill the space on 'x' and 'y'
          )

Label(tab1,text=" hello in tab 1",width=50,height=25).pack()
Label(tab2,text=" bye in tab 2",width=50,height=25).pack()


a.mainloop()
