a=input("enter any message ")
b=len(a)
c=len(a.split(" "))
d=0
e=0
for f in a:
    if f.isalpha():
        d+=1
    elif f.isdigit():
         e+=1
    else:
        1+1
g=(((d+e)/2)*100)
print(a)
print("number of words is",c)
print("number of char is",b)
print("number of numbers is",e)
print("the alphanumic percent is ",g,"%")      
input()
