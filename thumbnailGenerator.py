# Code by arcenter
# https://github.com/arcenter/RandomCodes/

# This code generates thumbnails (a frame of the video anywhere between 10% and 90%) for videos within a directory.

import cv2
from os import chdir, listdir, mkdir, path
from random import randint

chdir(input('Enter directory containing MP4 videos\n>>> '))
outputDir = input('\nEnter directory to output thumbnails into\n>>> ')
print()

if not path.isdir(outputDir):
    mkdir(outputDir)

for video in [i for i in listdir() if '.mp4' in i]:

    print(video)

    cam = cv2.VideoCapture(video)
    frames = cam.get(cv2.CAP_PROP_FRAME_COUNT)
    cam.set(1, randint(frames//10, 9*frames//10))
    _, frame = cam.read()
    cv2.imwrite(f'{outputDir}/{video[:-3:]}png', frame)
    cam.release()
    cv2.destroyAllWindows()

# Code by arcenter
# https://github.com/arcenter/RandomCodes/
