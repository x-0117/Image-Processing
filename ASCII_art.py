import numpy as np
from PIL import Image as im
import random, sys


try:
    imageFile = input("Enter file name with path and extension : ")
    i = im.open(imageFile)
    i.thumbnail((150, 150))
    global x
    x = np.array(i)
except:
    print("Path not found!")
    sys.exit()


threshold = int(input("Set threshold : "))
shit = [[0 for _ in range(x.shape[1])] for __ in range(x.shape[0])]
text = [[0 for _ in range(x.shape[1])] for __ in range(x.shape[0])]


for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        shit[i][j] = x[i][j][0] * 0.3 + x[i][j][1] * 0.59 + x[i][j][2] * 0.11


for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        if shit[i][j] < threshold:
            shit[i][j] = ' '
            text[i][j] = str(random.randint(0, 1))
        else:
            shit[i][j] = str(random.randint(0, 1))
            text[i][j] = ' '


for i in shit:
    print(''.join(i), end='\n\t\t\t\t\t')


f = open(imageFile.split('.')[0] + " ASCII art.txt", 'a')
for i in text:
    f.write('\n\t\t\t\t\t' + ''.join(i))
f.close()