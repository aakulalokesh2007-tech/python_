from tkinter import *
from tkinter.ttk import *
import time
def fun():
    for x in range(100):
        bar["value"]+=1
        time.sleep(0.05)
        v.set(str(int(x+1))+"%")
        
        a.update_idletasks()
        b.set(str(x+1)+"/"+"100"+"Tasks done")
a=Tk()
v=StringVar()
b=StringVar()

bar=Progressbar(a,orient=HORIZONTAL,length=300)
bar.pack()

Label(a,textvariable=v).pack()
Label(a,textvariable=b).pack()


Button(a,text="download",command=fun).pack()

a.mainloop()
