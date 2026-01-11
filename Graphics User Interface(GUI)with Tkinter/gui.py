from tkinter import *
dis=Tk()
img=PhotoImage(file="icon.png")
#dis.geometry("420x420")#size of window
dis.title("lokesh GUI")#title
img=PhotoImage(file='icon.png')
dis.iconphoto(True,img)#image
dis.config(background="blue")#bg colour
lab=Label(dis,
          text="HELLO WORLD",
          font=("Arial",40,"bold"),
          fg="#00ff00",
          bg="black",
          relief=SUNKEN,#boder style
          bd=20,                    #border size
          padx=300,
          pady=120,
          image=img,compound=TOP)                   
lab.pack()
#lab.place(x=20,y=20)
dis.mainloop()#loop
