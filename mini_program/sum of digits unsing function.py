def sum(a):
    global c
    if a!=0:
        c+=a%10
        a=a//10
        return sum(a)
    return c
c=0
print(sum(12345))
        
    
  
