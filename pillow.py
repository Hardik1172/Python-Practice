from PIL import Image , ImageDraw , ImageFont
img = Image.open(r"C:\Users\user\Downloads\jpg2png\test.png")
fnt  = ImageFont.truetype(r"C:\Users\user\Downloads\jpg2png\arial.ttf",30)
draw = ImageDraw.Draw(img)
draw.text(xy=(50,200),
          text = "This is Image",
          font = fnt,
          fill = (0,127,0))
img.show()


