# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

data = np.loadtxt("u.txt", delimiter=",")
nodes = data[:,0]
ux = data[:,1]
uy = data[:,2]
usum = data[:,3]

plt.plot(nodes, ux, "r--", label="ux")
plt.plot(nodes, uy, "g--", label="uy")
plt.plot(nodes, usum, "b", label="usum")
plt.xlabel("Nodes")
plt.ylabel("Displacement (m)")
plt.xticks(nodes)
plt.legend()
plt.show()
