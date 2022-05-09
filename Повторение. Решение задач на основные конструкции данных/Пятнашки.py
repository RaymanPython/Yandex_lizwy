from PIL import Image
from os import remove

img = Image.open("image.bmp")
x, y = img.size
for i in range(4):
    for j in range(4):
        if i != 4 and j != 4:
            img1 = img.crop((i * (x / 4), j * (y / 4), (i + 1) * (x / 4), (j + 1) * (y / 4)))
            img1.save('image{x}{y}.bmp'.format(x=str(j + 1), y=str(i + 1)))
remove('image44.bmp')
