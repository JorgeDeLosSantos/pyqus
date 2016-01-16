# -*- coding: utf-8 -*-
# =============================
# (c) 2015, Jorge De Los Santos
# ITC-Bypasa
# =============================
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.patches import Polygon
"""
NC = np.array([
			[0,0,0],
			[0,1,0],
			[0,1,1],
			[0,0,1],
			[-1,0,0],
			[-1,1,0],
			[-1,1,1],
			[-1,0,1],
			[-2,0,0],
			[-2,1,0],
			[-2,1,1],
			[-2,0,1],])
EC = np.array([
			[1,2,3,4],
			[2,6,7,3],
			[6,5,8,7],
			[5,1,4,8],
			[4,3,7,8],
			[1,5,6,2],
			[6,10,11,7],
			[10,9,12,11],
			[9,5,8,12],
			[10,9,5,6],
			[11,12,8,7]])"""

NC = np.array([
			[0,0,0],
			[0,1,0],
			[0,1,1],
			[0,0,1],
			[-1,0,0],
			[-1,1,0],
			[-1,1,1],
			[-1,0,1]])
EC = np.array([[1,2,3,4,5,6,7,8]])

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
#x,y=np.meshgrid(np.arange(0,limx,0.1),np.arange(0,limy,0.1))
#z=x**2*np.sin(x)*np.cos(y)
#f = plt.figure()
#ax = f.add_subplot(111)
plt.hold(True)

for CURE in EC:
	TEC = np.array([
			[CURE[0],CURE[1],CURE[2],CURE[3]],
			[CURE[2],CURE[5],CURE[6],CURE[2]],
			[CURE[5],CURE[4],CURE[7],CURE[6]],
			[CURE[4],CURE[0],CURE[3],CURE[7]],
			[CURE[3],CURE[2],CURE[6],CURE[7]],
			[CURE[0],CURE[4],CURE[5],CURE[1]]])
	for telement in TEC:
		XX,YY,ZZ = ([],[],[])
		for node in telement:
			XX.append(NC[node-1,0])
			YY.append(NC[node-1,1])
			ZZ.append(NC[node-1,2])
		ax.plot_wireframe(XX,YY,ZZ,facecolor="#fefefe")
plt.axis('equal')
ax.set_xlim(np.min(NC[:,0]),np.max(NC[:,0]))
ax.set_ylim(np.min(NC[:,1]),np.max(NC[:,1]))
ax.set_zlim(np.min(NC[:,2]),np.max(NC[:,2]))
plt.axis('off')
plt.show()
