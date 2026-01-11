from tkinter import *
def pres():
    print("yo did it")
    #press["state"]=DISABLED

dis=Tk()
img=PhotoImage(file='icon.png')
press=Button(dis,text="clickme",
             command=pres,font=("comic sans",40),
             fg="#00FF00",
             bg="black",
             activeforeground="white",activebackground="black",
             state=ACTIVE,image=img,compound="left",
             )
press.pack()
dis.mainloop
