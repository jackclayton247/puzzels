import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

grid = 41
radii = []
dist = []

def close(center):
    #x coords
    a = center[0]
    b = grid- a
    #y coors
    c = center[1]
    d = grid - c
    return min(a, b, c, d)

for x1 in range(1, grid, 1):
    print(x1)
    for x2 in range(1, grid, 1):
        for y1 in range(1, grid, 1):
            for y2 in range(1, grid, 1):
                radius = math.sqrt((x1 - x2)**2 + (y1-y2)**2)/2
                center = [(x1+x2)/2, (y1 + y2)/2]
                radii += [radius]
                dist += [close(center)]
x = []
y = []                   
for i in range(12):
    x.append(i)
    y.append(i)
plt.plot(x, y)
plt.scatter(dist, radii)
plt.show()

#print(x_values)
#print(y_values)


