import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

grid = 400
radii = []
centers = []
ratio = [0 ,0] #outside:inside

def close(center, grid):
    #x coords
    a = center[0]
    b = grid- a
    #y coors
    c = center[1]
    d = grid - c
    return min(a, b, c, d)

for x1 in range(1, grid+1, 1):
    print(x1)
    for y1 in range(1, grid+1, 1):
        for x2 in range(1, grid+1, 1):
            for y2 in range(1, grid+1, 1):
                center = [(x1+x2)/2, (y1 + y2)/2]
                radius = (x1 - x2)**2 + (y1-y2)**2
                if (close(center, grid)*2)**2 < radius:
                    ratio[0] += 1
                else:
                    ratio[1] += 1
prob = ratio[0]/(ratio[0]+ratio[1])
print(prob)
print(0.47857924, 0.477258165, 0.4768912474074074) #100, 200, 300
