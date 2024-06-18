from PIL import Image, ImageFont, ImageDraw
img = Image.open(r"")
img.show()
draw = ImageDraw.Draw(img)
draw.rectangle(xy=(50,50,150,150),
               fill= (0,127,0),
               outline=(255,255,255),
               width = 5)
draw.line(xy= (30,30,60,60),
          fill= (0,127,0),
          width= 40)
draw.arc(xy= (50,50,80,80),
         fill=(0,80,80),
         outline=(60,60,50),
         width=60)
