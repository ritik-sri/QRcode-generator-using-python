import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl&index=1")
img.save("ritik.png")