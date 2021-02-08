import matplotlib.pyplot as plt
import scipy.ndimage
import numpy as np
import sys
import pygame
from pygame.locals import *
try:
    image = np.array(plt.imread(input("Enter file name with path and extension : ")))
except:
    print("Path not found!")
    sys.exit()
x = image
shit = [[0 for _ in range(x.shape[1])] for __ in range(x.shape[0])]
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        shit[i][j] = x[i][j][0] * 0.3 + x[i][j][1] * 0.59 + x[i][j][2] * 0.11
vertical = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
vertizontal = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]
z = np.array(scipy.ndimage.convolve(shit, vertizontal, mode='reflect'))
pygame.init()
x1 = x.shape[1]
y1 = x.shape[0]
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
        
x117 = [[[0, 0, 0] for _ in range(x1)] for __ in range(y1)]
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
                    x117[k[0]][k[1]] = x[k[0]][k[1]]
        else:
            for k in l0:
                if list(x[k[0]][k[1]]) != [255, 0, 0]:
                    x117[k[0]][k[1]] = x[k[0]][k[1]]
    except:
        pass
plt.imshow(x117)