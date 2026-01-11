from tkinter import*
def pri():
    if x.get()==1:
        print("yes")
    else:
        print("no")
a=Tk()
img=PhotoImage(file="icon.png")

x=IntVar()
b=Checkbutton(a,text="are you 18+",variable=x,onvalue=1,#default
              offvalue=0,#default
              command=pri,fg="blue",bg="pink",activeforeground="black",
              activebackground="white",font=("Arial",30),padx=20,pady=10,
              image=img,compound=LEFT)
b.pack()

a.mainloop()

