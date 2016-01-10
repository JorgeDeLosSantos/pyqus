# -*- coding: mbcs -*-
# =============================
# (c) 2015, Jorge De Los Santos
# ITC-Bypasa
# =============================
# 
# Required packages:
#	    	         - Numpy
#   	             - Matplotlib

import numpy as np
from numpy import nan
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def plot_dfile(figname="dfile.png",filename="data.txt",xlabel="X",ylabel="Y",dlm=","):
	"""
	Plot a data file with two columns, separated by a delimiter.
		fname: Filename   i.e. "data_file.txt"
		xlabel: X-Axis Label  i.e. "Time (s)"
		ylabel: Y-Axis Label  i.e. "Stress (MPa)"
		dlm: Delimiter  i.e. ","
	"""
	D = np.loadtxt(filename, delimiter=dlm)
	XX = D[:,0]
	YY = D[:,1]
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(XX,YY)
	ax.set_xlabel(xlabel)
	ax.set_ylabel(ylabel)
	plt.savefig(figname)

def plot_nodes(figname="nodes.png",nodesfile="nodes.txt",dlm=","):
	"""
	Plot nodes of mesh, the data file must be contain two columns: 
	X and Y coordinates for each node separated by delimiter.
	"""
	D = np.loadtxt(nodesfile, delimiter=dlm)
	XX = D[:,0]
	YY = D[:,1]
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(XX,YY,"ko",markersize=1.0)
	plt.axis('equal')
	plt.savefig(figname)
	
def plot_elements(figname="elements.png",nodesfile="nodes.txt",elementsfile="elements.txt",dlm=","):
	"""
	Plot nodes and elements of mesh.
	
		figname:       Name of output picture
		nodesfile:     Path of node data file
		elementsfile:  Path of elements conectivity file
		dlm:           Delimiter (i.e. ",","\t")
	"""
	NC = np.loadtxt(nodesfile, delimiter=dlm)
	EC = np.loadtxt(elementsfile, delimiter=dlm)
	f = plt.figure()
	ax = f.add_subplot(111)
	plt.hold(True)
	for element in EC:
		XX = []
		for node in element:
			if str(node)!="nan":
				XX.append([NC[node-1,0],NC[node-1,1]])
		p = Polygon(XX, True, fc="#00DDDD", ec="#778877")
		ax.add_patch(p)
	plt.axis('equal')
	plt.axis('off')
	#ax.plot(NC[:,0],NC[:,1],'ko',markersize=1.0)
	plt.savefig(figname)

def plot_sequence(outfolder="img",sequencefile="sequence.txt",elementsfile="elements.txt"):
	"""
	untested
	"""
	#NC = np.loadtxt(nodesfile, delimiter=dlm)
	EC = np.loadtxt(elementsfile, delimiter=dlm)
	f = plt.figure()
	ax = f.add_subplot(111)
	plt.hold(True)
	while True:
		for element in EC:
			XX = []
			for node in element:
				if str(node)!="nan":
					XX.append([NC[node-1,0],NC[node-1,1]])
			p = Polygon(XX, True, fc="#00DDDD", ec="#778877")
			ax.add_patch(p)
		plt.axis('equal')
		plt.savefig(figname)
	
def read_one_frame(filename="sequence.txt",dlm=","):
	"""
	untested
	"""
	f = open(filename,"r")
	txt = f.readlines()
	A = []
	XX = []
	for line in txt:
		if line.startswith("="):
			A.append(XX)
			XX = []
			continue
		XX.append(np.array(line))
	A.remove([])
	return np.array(A)
				
if __name__=='__main__':
	print read_one_frame()
