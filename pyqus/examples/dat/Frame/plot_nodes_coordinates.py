# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

coords = np.loadtxt("nodes.txt",delimiter=",")
elms = np.loadtxt("elements.txt",delimiter=",")

x = []
y = []
for conn in elms:
    for el in conn:
        x.append(coords[el-1,0])
        y.append(coords[el-1,1])

plt.plot(x, y, "b-o")
plt.xlim(min(x)-0.1, max(x)+0.1)
plt.ylim(min(y)-0.1, max(y)+0.1)
plt.gca().set_aspect("equal")
plt.show()
