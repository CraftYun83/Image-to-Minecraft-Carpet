from PIL import Image

carpet_colors = {
    "white": (253, 253, 253), #
    "orange": (255, 143, 16), #
    "dark_pink": (206, 53, 172), #
    "aqua": (3, 188, 225), #
    "yellow": (255, 203, 0), #
    "lime": (24, 178, 0), #
    "pink": (255, 164, 190), #
    "dark_grey": (64, 75, 78), #
    "grey": (151, 151, 145), #
    "dark_aqua": (0, 130, 143), #
    "purple": (147, 39, 179), #
    "blue": (51, 55, 164), #
    "brown": (144, 80, 44), #
    "green": (72, 116, 0), #
    "red": (200, 39, 30), #
    "black": (5, 6, 12) #
}
im = Image.open('image2.jpg')
im = im.convert("RGB")
pixels = []
pix_as_carpet = []

for i in range(im.width):
    for j in range(im.height):
        pixtuple = im.getpixel((i,j))
        pixels.append(pixtuple)
        averages = []
        for item in carpet_colors.keys():
            averages.append(((carpet_colors[item][0] - pixtuple[0])**2+(carpet_colors[item][1] - pixtuple[1])**2+(carpet_colors[item][2] - pixtuple[2])**2)**0.5)
        pix_as_carpet.append(carpet_colors[list(carpet_colors.keys())[averages.index(min(averages))]])

img = Image.new('RGB', (im.width, im.height))
count = 0
for i in range(img.width):
    for j in range(img.height):
        img.load()[i, j] = pix_as_carpet[count]
        count += 1

print(len(pixels))
img.show()