from tkinter import *
from tkinter import filedialog
def op():
    print(file:=filedialog.askopenfilename(initialdir=("C://Users//monis//Desktop"),#open this location as opened
                                                                                   title="open file",
                                                                                   filetypes=(("text file","*.txt"),("all files","*.*"))))
    x=open(file)
    print(x.read())
a=Tk()
bb=Button(a,text="open",command=op)
bb.pack()
a.mainloop()
