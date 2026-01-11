while True:
 a=input("enter the number of terms ")
 if a.isdigit():
   b=0
   c=1
   print("fibonacci series:")
   print("              0 1 ",end='')
   for d in range (int(a)-2):
     e=b+c
     print(e,end=' ')
     b,c=c,e
   print('')
   break
 else:
    print("enter only number")
input()
