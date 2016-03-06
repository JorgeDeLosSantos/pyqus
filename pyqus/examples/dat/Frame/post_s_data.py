# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

data = np.loadtxt("S.txt", delimiter=",")
elements = data[:,0]
smaxp = data[:,1]/1e6 # MPa
seqv = data[:,2]/1e6 # MPa

plt.plot(elements, smaxp, "r-*", label="Max. Principal")
plt.plot(elements, seqv, "g-x", label="Mises")
plt.xlabel("Elements")
plt.ylabel("Stress (MPa)")
plt.xticks(elements)
plt.legend()
plt.show()
