from PIL import Image
img = Image.open(r"C:\Users\user\Downloads\jpg2png\test.png")
print(img.mode)
print(img.size)
print(img.format)