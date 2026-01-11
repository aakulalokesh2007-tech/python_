a=eval(input("enter your list ,(don't forgot '[]')"))
while True:
    print('''1.Insert an element
             2.Delete an element
             3.sorting the element''')
    b=input()
    if b==1:
            c=input('entr the element to insert')
            d=input('enter the position ')
            a.insert(d,c)
    elif b==2:
      while True:
        c=input('enter the element to delete')
        if c not in a:
            print("please enter a element from list")
            continue
        a.remove(c)
    elif b==3:
        while True:
            print('''How to sort
                    1.ascending order
                    2.descending order''')
            c=input()
    
