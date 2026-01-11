a=input("enter the string ")
b=input("enter the letter which you want to find ")
c=a.count(b)
if b.isalpha():
     print("the leter ",b,"occers",c,"times")
elif b.isdigit():
     print("the number ",b,"occers",c,"times")
else:
     print("the spical charecter ",b,"occers",c,"times")
input()
