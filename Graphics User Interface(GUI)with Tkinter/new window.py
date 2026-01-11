from tkinter import *
def fun():
    #new=Toplevel()   #== new window 'on top' of other windows.linked to a 'bottom' window
    new=Tk()
    a.destroy()#close the window



    
a=Tk()

Button(a,text="create",command=fun).pack()





a.mainloop()
