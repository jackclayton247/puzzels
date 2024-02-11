import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

grid = 41
radii = []
rfreq = []
distribution = []
x_values = []
y_values = []
centers = []

for x1 in range(1, grid, 1):
    print(x1)
    for x2 in range(1, grid, 1):
        for y1 in range(1, grid, 1):
            for y2 in range(1, grid, 1):
                centers += [(x1+x2)/2, (y1 + y2)/2]
                radius = math.sqrt((x1 - x2)**2 + (y1-y2)**2)/2
                if radius in radii:
                    rfreq[radii.index(radius)] += 1
                else:
                    radii.append(radius)
                    rfreq.append(1)
for i in range(len(rfreq)):
    distribution += [[radii[i], rfreq[i]]]
distribution = sorted(distribution, key=lambda x:x[0])
    
for i in range(len(rfreq)):
    #print([distribution[i][1]])
    x_values.append(distribution[i][0])
    y_values.append(distribution[i][1])

curve = np.polyfit(x_values, y_values, 2)
poly = np.poly1d(curve)

new_x = []
new_y = []
for i in range(30):
    new_x.append(i+1)
    calc = poly(i+1)
    new_y.append(calc)

#plt.plot(new_x, new_y)
plt.scatter(y_values, x_values)
plt.show()

#print(x_values)
#print(y_values)


