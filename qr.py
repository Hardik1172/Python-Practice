import qrcode
data = "www.makemytrip.com"

img = qrcode.make(data)

img.save("qrcode.png")
