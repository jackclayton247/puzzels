import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

grid = 21
radii = []
counter_ = []
temp = []
counter = 0
for x1 in range(1, grid, 1):
    print(x1)
    for y1 in range(1, grid, 1):
        for x2 in range(1, grid, 1):
            for y2 in range(1, grid, 1):
                radius = math.sqrt((x1 - x2)**2 + (y1-y2)**2)/2
                radii.append(radius)
                counter_.append(counter)
                counter += 1
radii.sort()
for i in range(len(radii)):
    temp.append(i)



#plt.plot(new_x, new_y)
plt.scatter(temp, radii)
plt.show()
#print(x_values)
#print(y_values)