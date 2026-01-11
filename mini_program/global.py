def f():
    global a
    a+=5
    return a
a=2
print(f())
