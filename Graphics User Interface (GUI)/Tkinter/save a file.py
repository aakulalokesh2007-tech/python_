from tkinter import *
from tkinter import filedialog

def sav():
    a=filedialog.asksaveasfile(initialdir="C:\\Users\\monis\\Desktop\\GUI",
                               defaultextension=".txt",
                               filetypes=[("text files",".txt"),
                                          ("html file",".html"),
                                          ("all files",".*")])
    if a is None:
        return 
    b=str(c.get(1.0,END))
    a.write(b)
    a.close()


a=Tk()
Button(a,text="save",command=sav).pack()
c=Text(a)
c.pack()
a.mainloop()
