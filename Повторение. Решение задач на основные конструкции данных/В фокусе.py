from PIL import Image

im = Image.open("image.png")
pixels = im.load()
x, y = im.size
dr = pixels[0, 0]
t, d, le, r = y + 1, 0, x + 1, 0
for i in range(x):
    for j in range(y):
        if pixels[i, j] != dr:
            if j < t:
                t = j
            if j > d:
                d = j
            if i > r:
                r = i
            if i < le:
                le = i
im2 = im.crop((le, t, r + 1, d + 1))
im2.save('res.png')
