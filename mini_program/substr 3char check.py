a=input("str")
b=input("substr")
aa=a
g=0
while ((aa.count(b[2]))!=0)or (aa.count(b[1]))!=0 or (aa.count(b[2]))!=0:
    i=aa.index(b[0])
    e=aa.count(b[2])
    f=0
    for h in range(e):
        f=aa.index(b[2],f+1)
        g+=aa.count(b[1],aa.index(b[0]),f)
    if aa.count(b[0]) >=2:
        aa=aa[aa.index(b[0],i+1):]
    else:
        break
    print(aa)


print(g)
print(f)
