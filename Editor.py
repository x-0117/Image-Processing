# -*- coding: utf-8 -*-
import numpy as np
import sys
from PIL import Image as im
try:
    imageFile = input("Enter file name with path and extension : ")
    global x
    x = np.array(im.open(imageFile))
except:
    print("Path not found!")
    sys.exit()


def monochrome(x):
    shit = [[0 for _ in range(x.shape[1])] for __ in range(x.shape[0])]
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            shit[i][j] = int(x[i][j][0] * 0.3 + x[i][j][1] * 0.59 + x[i][j][2] * 0.11)
    return shit


def blackAndWhite(x, colour = [0, 0, 0]):
    shit = np.array(im.new('RGBA', (x.shape[1], x.shape[0])))
    mono = monochrome(x)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            shit[i][j] = colour + [255 - mono[i][j]]
    im.fromarray(shit).save(imageFile.split('.')[0] + "_edited.png")


def negative(x):
    shit = np.array(im.new('RGB', (x.shape[1], x.shape[0])))
    mono = monochrome(x)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            shit[i][j] = [255 - mono[i][j]] * 3
    im.fromarray(shit).save(imageFile.split('.')[0] + "_edited.png")


def threshold(x, colour = [0, 0, 0], threshold = 127):
    shit = np.array(im.new('RGB', (x.shape[1], x.shape[0])))
    mono = monochrome(x)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if mono[i][j] < threshold:
                shit[i][j] = colour
            else:
                shit[i][j] = [255, 255, 255]
    im.fromarray(shit).save(imageFile.split('.')[0] + "_edited.png")


command = input("""1) Black and White(syntax : 1)
2) Negative(syntax : 2)
3) Sepia(syntax : 3)
4) Threshold(pure black and white)(syntax : 4 <threshold>)
5) Coloured Monochrome(syntax : 5 <R>,<G>,<B> (RGB values comma separated without space))
6) Coloured Threshold(syntax : 6 <R>,<G>,<B>, <threshold>)\n>>""").split()

try:
    if command[0] == '1':
        blackAndWhite(x)
    elif command[0] == '2':
        negative(x)
    elif command[0] == '3':
        blackAndWhite(x, [122, 66, 20])
    elif command[0] == '4':
        threshold(x, threshold=int(command[1]))
    elif command[0] == '5':
        blackAndWhite(x, [int(_) for _ in command[1].split(',')])
    elif command[0] == '6':
        threshold(x, colour = [int(_) for _ in command[1].split(',')], threshold = int(command[2]))
    else:
        print("Please check the syntax. (Only one space wherever there's a space and no spaces around the commas!')")
except:
    print("Please check the syntax. (Only one space wherever there's a space and no spaces around the commas!')")