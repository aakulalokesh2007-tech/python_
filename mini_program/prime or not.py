#to check input is prime or not
a=(input("enter any number"))
if a.isdigit():
    a=int(a)
    c=1
    for b in range(2,a):
        c=a%b
        if c==0:
            print("the number '",a,"'is composite") 
            break
    if a==1:
        print("the number '1' neither prime nor composite")
    elif a==0:
        print("'0' is nothing")
    else:
        print("the number '",a,"'is  prime")
else:
    print("plz enter a number")
