import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

grid = 71
radii = []
dist = []
temp = []

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
                temp.append([radius, close(center)])
                #radii += [radius]
                #dist += [close(center)]
temp = sorted(temp, key=lambda x:x[0])
temp = temp[::-1]
temp2 = []
temp_dist = []
#print(temp)
for i in range(len(temp)):
    if temp[i][1] in temp_dist:
        pass
    else:
        temp2.append(temp[i])
        temp_dist.append(temp[i][1])
x = []
y = []
for i in range(len(temp2)):
    x.append(temp2[i][1])
    y.append(temp2[i][0])

curve = np.polyfit(x, y, 3)
poly = np.poly1d(curve)
print(poly, max(x))

new_x = []
new_y = []
for i in range(37):
    new_x.append(i+1)
    calc = poly(i+1)
    new_y.append(calc)

#print(temp2)
plt.plot(new_x, new_y)
plt.scatter(x, y)
#plt.scatter(0, 0)
plt.show()