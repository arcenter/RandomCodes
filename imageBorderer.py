# Code by arcenter
# https://github.com/arcenter/RandomCodes/

# This script adds a black border to an image to get its dimensions to a required one. Also resizes it to final width and height if image size is over that.

from PIL import Image, ImageOps
from os import chdir, listdir

chdir(input('Enter directory containing images\n>>> '))

finalWidth  = int(input('\nEnter Final Width : '))
finalHeight = int(input('Enter Final Height: '))
print()

for i in listdir():
    print(i)
    img = Image.open(i)
    width, height = img.size
    if height > width:
        border = round(((height*finalWidth/finalHeight)-width)/2), 0
    else:
        border = 0, round(((width*finalHeight/finalWidth)-height)/2)
    img_with_border = ImageOps.expand(img,border,fill='black')
    img_with_border.thumbnail((finalWidth, finalHeight), Image.Resampling.LANCZOS)
    img_with_border.save(i[:i.rfind('.'):] + '_modified' + i[i.rfind('.')::])

# Code by arcenter
# https://github.com/arcenter/RandomCodes/
