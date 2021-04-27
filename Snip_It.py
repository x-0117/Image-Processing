# -*- coding: utf-8 -*-
import scipy.ndimage, numpy as np
import sys
from PIL import Image as im
import pygame
from pygame.locals import *


try:
    imageFile = input("Enter file name with path and extension : ")
    x = np.array(im.open(imageFile))
except:
    print("Path not found!")
    sys.exit()
x1 = x.shape[1]
y1 = x.shape[0]


x117 = np.array([[[0, 0, 0, 0] for _ in range(x1)] for __ in range(y1)])
for i in range(y1):
    for j in range(x1):
        x117[i][j] = list(x[i][j]) + [0]


shit = [[0 for _ in range(x.shape[1])] for __ in range(x.shape[0])]
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        shit[i][j] = x[i][j][0] * 0.3 + x[i][j][1] * 0.59 + x[i][j][2] * 0.11


vertizontal = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]
z = np.array(scipy.ndimage.convolve(shit, vertizontal, mode='reflect'))


pygame.init()
DISPLAYSURF = pygame.display.set_mode((x1, y1), 0, 32)
pygame.display.set_caption('Black Board')
for i in range(x1):
    for j in range(y1):
        DISPLAYSURF.set_at((i, j), x[j][i])
flag = 0
flag2 = 0
while True:
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            flag2 = 1
    if flag2 == 1:
        break
    if event.type == MOUSEBUTTONDOWN:
        if flag == 0:
            flag = 1 - flag
            pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (5, 5), 5, 0)
        else:
            flag = 1 - flag
            pygame.draw.circle(DISPLAYSURF, (0, 0, 0), (5, 5), 5, 0)
    if flag == 1:
        min_ = 255
        j1 = 0
        for j in range(mx - 3, mx + 3):
            if z[my][j] < min_:
                min_ = z[my][j]
                j1 = j
        DISPLAYSURF.set_at((j1, my), (255, 0, 0))
        x[my][j1] = [255, 0, 0]
    pygame.display.update()


flag3 = 0
for i in range(y1):
    flag3 = -1
    l0 = []
    l1 = []
    for j in range(x1):
        if flag3 == 0:
            l0.append([i, j])
        elif flag3 == 1:
            l1.append([i, j])
        if list(x[i, j]) == [255, 0, 0] and list(x[i, j + 1] != [255, 0, 0]):
            if flag3 == -1:
                flag3 = 0
            elif flag3 == 0:
                flag3 = 1
            elif flag3 == 1:
                flag3 = 0
    try:
        if l0[-1][-1] == x1 - 1:
            for k in l1:
                if list(x[k[0]][k[1]]) != [255, 0, 0]:
                    x117[k[0]][k[1]][3] = 255
        else:
            for k in l0:
                if list(x[k[0]][k[1]]) != [255, 0, 0]:
                    x117[k[0]][k[1]][3] = 255
    except:
        pass
for i in range(y1):
    for j in range(x1):
        if x117[i][j][3] == 0:
            try:
                if 255 in x117[i - 3:i, j, 3] and 255 in x117[i + 1:i + 4, j, 3]:
                    x117[i][j][3] = 255
            except:
                pass


src = im.new('RGBA', (x1, y1))
image_save = np.array(src)
for i in range(y1):
    for j in range(x1):
        image_save[i][j] = x117[i][j]


im.fromarray(image_save).save(imageFile.split('.')[0] + "_cropped.png")
