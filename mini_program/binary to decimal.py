e=g=0
a=input(" ")
for aa in str(a):
    if aa not in ['1','0','.']:
        break
if aa  in ['1','0']:
  if str(a).find('.')==(-1) or str(a).find('.')!=-1:
    b=a.split('.')
    c=b[0][::-1]
    if str(a).find('.')==(-1):
        pass
    else:
        f=b[1][::-1]
    for d in range(len(c)):
        e+=int(c[d])*(2**d)
    if str(a).find('.')==(-1):
        pass
    else:
        for d in range (1,(len(f))+1):
            g+=int(f[d-1]) *(1/2**d)
    if str(a).find('.')==(-1):
        print(int(e))
    else:
        print(int(e)+float(g))
else:
    print("plz enter a binary number")
input()
