#progam for file handling
e=0
with open("expence.txt",'w') as a:
    b=input("enter number of months")
    for c in range(int(b)):
        a.write("month No {}".format(c)+input("enter month {}s entry".format(c+1))+"\n")
    b=input("enter the no of months to get enteries")

with open("expence.txt",'r') as a:
    for c in range(int(b)):
        d=a.readline()
        d=int(d[-4:-1])
        e+=d
print("{}months entry is {}".format(b,e))
