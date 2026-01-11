import pyqrcode
s="https://www.youtube.com/"
x=pyqrcode.create(s)
x.svg("qrcode.svg",scale=8)
#x.png("qrcode1.png",scale=10)
print("copm")
