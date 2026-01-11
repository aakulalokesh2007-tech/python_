a=[1,2,3,4,5]
try:
    a.insert((int(input("position")))-1,(eval(input("element ''plz give 'corts' if it is str'' "))))
    print(a)
except NameError:
    print("plz enter with 'corts' for string")
    
input()
