h=[]
k=[]
print(''' information:
                cartype can be of three kinds :big,medium,or small which are represented by 1,2,3 respectively''')
while True:
    b=input("number of big sized cars can parked ")
    if b.isdigit():
        b=int(b)
        break
    else:
        print("please enter a number  ")
while True:
    c=input("number of middium sized cars can parked ")
    if c.isdigit():
        c=int(c)
        break
    else:
         print("please enter a number ")
while True:
    d=input("number of small sized cars can parked ")
    if d.isdigit():
        d=int(d)
        break
    else:
        print("please enter a number ")
a=[b,c,d]
while True:
    e=input("number of cars are there enter less than 1000 ")
    if e.isdigit() and int(e)<1000:
        e=int(e)
        break
    else:
        print("please enter a number less 1000")
for f in range (e):
    while True:
        g=input("enter the code of the car type ")
        if g.isdigit():
            g=int(g)
            if g>4:
                print("plz enter a valid code")
                continue
            else:
                break
        else:
            print("please enter a number")
    i=[g]
    h.append(i)
h.insert(0,a)
print("Input is :")
print("       ",h)
h.remove(a)
for j in h:
    if j[0]==1:
        if a[0]>0:
            a[0]-=1
            k.append(True)
        else:
            k.append(False)
    elif j[0]==2:
        if a[1]>0:
            a[0]-=1
            k.append(True)
        else:
            k.append(False)
    elif j[0]==3:
        if a[2]>0:
            a[2]-=1
            k.append(True)
        else:
            k.append(False)
k.insert(0,'null')
print("the output is :")
print("         ",k)
        
        
