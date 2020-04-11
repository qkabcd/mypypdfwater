from PIL import Image

# im=Image.open('pic.jpg')

# w,h=im.size

# print('Original image size: %sx%s' % (w, h))

# im.thumbnail((w//2, h//2))
# print('Resize image to: %sx%s' % (w//2, h//2))

# im.save('thumbnail.jpg', 'jpeg')

imageSrc = Image.open("pic.jpg")
logo = Image.open("water.png")

logo_mask = logo.convert("L").point(lambda x: min(x, 35))
logo.putalpha(logo_mask)

# 循环遍历水印
for i in range(0, 3):
    for j in range(0, 3):
        x = 33 + (374*j)
        y = 250 + (374*i)
        imageSrc.paste(logo, (x, y), mask=logo)
        


imageSrc.save('test.jpg', optimize=True)