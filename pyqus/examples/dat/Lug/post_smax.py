# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

data = np.loadtxt("max_S.txt", delimiter=",")
time = data[:,0]
s = data[:,1]/1e6 # MPa

plt.plot(time, s, "bo", label="Mises")
plt.xlabel("Time (s)")
plt.ylabel("Stress (MPa)")
plt.legend()
plt.show()
