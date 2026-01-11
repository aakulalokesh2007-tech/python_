a=eval(input("your list"))
b=int(input("element"))
def binary(l,e):
    f=0
    la=(len(l))-1
    mid=la//2
    l.sort()
    while f<la:
        if l[mid]==e:
            return e
        elif l[mid]>e:
            la=mid
            mid=(f+la)//2
        elif l[mid]<e:
            f=mid
            mid=(f+la)//2
    return -1    
print(binary(a,b))        
    
