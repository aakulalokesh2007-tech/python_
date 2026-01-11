e=0
a=input("str")
b=input("sub str")
for c in range(len(b)):
    d=a.index(b[0])
    e+=a.count(b[1],d+1)
    a=a[d+1:]
print(e)
