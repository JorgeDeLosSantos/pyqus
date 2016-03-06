# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

data = np.loadtxt("max_U.txt", delimiter=",")
time = data[:,0]
u = data[:,1]*1e3 # to mm

plt.plot(time, u, "b", label="Displacement")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (mm)")
plt.legend()
plt.show()
