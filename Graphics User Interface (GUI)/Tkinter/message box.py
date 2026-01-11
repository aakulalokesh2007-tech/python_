from tkinter import *
from tkinter import messagebox as c
def msg():
    #c.showinfo(title="info",message="are a person",#icon="warning")

    
    #c.showwarning(title="warning",message="be safe")

    
    #c.showerror(title="went wrong",message="be safe")

    
    #a=c.askokcancel(title="checking age",message="are you above 18")#return True if click ok #else false
    #if a:
        #print("18+")
    #else:
        #print("below 18")

    #a=c.askretrycancel(title="asking permission",message="cant able to use")#return True if click ok #else false
    #if a:
       # print("restated")
    #else:
        #print("quited")


    #a=c.askyesno(title="checking age",message="are you above 18")#return True if click ok #else false
    #if a:
     #   print("18+")
    #else:
     #   print("below 18")


    #a=c.askquestion(title="checking age",message="are you above 18")#return 'yes' if click ok #else 'no'
    #if a:
       # print("18+")
    #else:
       # print("below 18")


    #a=c.askyesnocancel(title="checking age",message="are you above 18",icon="warning")#return True if click ok #no:false #cancel:None 
    #if a:
        #print("18+")
    #elif a==None:
        #print("canceled")
    #else:
        #print("18-")
a=Tk()
b=Button(a,text="click{",command=msg)
b.pack()
a.mainloop()
