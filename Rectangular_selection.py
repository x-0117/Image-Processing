# -*- coding: utf-8 -*-
import numpy as np
import sys
from PIL import Image as im
import pygame
from pygame.locals import *


try:
    imageFile = input("Enter file name with path and extension : ")
    i = im.open(imageFile)
    global x
    x = np.array(i)
except:
    print("Path not found!")
    sys.exit()
x1 = x.shape[1]
y1 = x.shape[0]
global x_start, y_start, x_end, y_end
x_start = -1
y_start = -1
x_end = -1
y_end = -1


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
        if x_start == -1:
            x_start, y_start = mx, my
        else:
            for index in range(min(x_start, x_end), max(x_start, x_end)):
                DISPLAYSURF.set_at((index, y_start), x[y_start, index])
                DISPLAYSURF.set_at((index, y_end), x[y_end, index])
            for index in range(min(y_start, y_end), max(y_start, y_end)):
                DISPLAYSURF.set_at((x_start, index), x[index, x_start])
                DISPLAYSURF.set_at((x_end, index), x[index, x_end])
        x_end, y_end = mx, my
        for index in range(min(x_start, x_end), max(x_start, x_end)):
            DISPLAYSURF.set_at((index, y_start), (255, 0, 0))
            DISPLAYSURF.set_at((index, y_end), (255, 0, 0))
        for index in range(min(y_start, y_end), max(y_start, y_end)):
            DISPLAYSURF.set_at((x_start, index), (255, 0, 0))
            DISPLAYSURF.set_at((x_end, index), (255, 0, 0))
    pygame.display.update()


src = x[min(y_start, y_end) :  max(y_start, y_end), min(x_start, x_end) : max(x_start, x_end)]
im.fromarray(src).save(imageFile.split('.')[0] + "_cropped.png")