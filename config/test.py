import qrcode

qr = qrcode.make("http://138.68.74.218/menu/spicyx/")
print("SSSS")
qr.save('spicyx_qr.jpg')