from pickle import*
with open("test.dat","rb+") as a:
    for i in range(int(input("no of recrds"))):
        dump([input("0th"),input("1st")],a)
    a.seek(0)
    print(load(a))
