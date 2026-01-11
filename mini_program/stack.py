def push(list,ele):
    if len(list)==sc:
        print("overflow Error")
    else:
        list.append(ele)
def pop(list):
    if len(list)==0:
        print("under flow")
    else:
        return list.pop()
#main
sc=1
li=[]
push(li,2)
push(li,6)