from tkinter import *
def func(ev):
    print("pressed"+str(ev.x)+","+str(ev.y))
a=Tk()
#a.bind("<Button-1>",func)  #left button mouse
#a.bind("<Button-2>",func)   #scrol buton mouse
#a.bind("<Button-3>",func)  #right button
#a.bind("<ButtonRelease>",func)#do the function when we release the mouse button
#a.bind("<Enter>",func)# do the function when we enter the cursor into the window
#a.bind("<Leave>",func)#do the function when we leave the window
#a.bind("<Motion>",func)# do the function when we move the mouse inside the window

a.mainloop()
