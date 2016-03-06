# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # 3D mpl 

coords = np.loadtxt("nodes.txt",delimiter=",")
elms = np.loadtxt("elements.txt",delimiter=",")

x = []
y = []
for conn in elms:
    for el in conn:
        x.append(coords[el-1,0])
        y.append(coords[el-1,1])

ax.plot(x, y, 'o')
ax.set_aspect("equal")
plt.show()
