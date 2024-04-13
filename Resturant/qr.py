import qrcode

image = qrcode.make("https://127.0.0.1:8000") # chsnge this to public domain and rhen give the qr code to poeple
image.save("qr.png")