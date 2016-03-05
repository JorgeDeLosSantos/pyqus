# -*- coding: mbcs -*-
"""
Functions for read Abaqus odb files.

Generate plain data about:

* Parts
* Instances
* Materials
* Steps 
* Nodes coordinates
* Deformed shapes
* Max. Von Mises Stresses
* Max. Nominal Strains
* Max. Plastic EQV. Strains
* Max. Reactions forces
"""

import_error_str = """
Please try run in Abaqus/CAE script mode, as follows:

>> abaqus cae noGUI="test_script.py"

or verify that you have Abaqus installed.
"""

import numpy as np
try:
	from odbAccess import *
	from abaqusConstants import *
except ImportError:
	print import_error_str
	pass


def get_max_eqvs(dbpath,fname="max_eqvs.txt"):
	"""
	Get Max. Von Mises EQV. Stresses (all steps - all nodes)
	
	Parameters
	----------
	dbpath  : str
		Abaqus ODB file
	fname   : str
		Filename for output data
	"""
	odb = openOdb(path=dbpath)
	f = open(fname,"w")
	k = 0
	for step in odb.steps.keys():
		tbystep = odb.steps[step].frames[-1].frameValue
		for frame in odb.steps[step].frames:
			temp_list = []
			for td in frame.fieldOutputs['S'].values:
				temp_list.append(td.mises)	
			maxv = max(temp_list) # Max value
			f.write("%6.6f\t%6.4f\n"%(frame.frameValue + k*tbystep, maxv))
		k += 1
	f.close()


def get_max_pe(dbpath,fname="max_pe.txt"):
	""""
	Get Max. Plastic Strains (all nodes - all steps)
	
	Parameters
	----------
	dbpath  : str
		Abaqus ODB file
	fname   : str
		Filename for output data
	"""
	odb = openOdb(path=dbpath)
	f = open(fname,"w")
	k = 0
	for step in odb.steps.keys():
		tbystep = odb.steps[step].frames[-1].frameValue
		for frame in odb.steps[step].frames:
			temp_list = []
			for td in frame.fieldOutputs['PE'].values:
				temp_list.append(td.maxPrincipal)
			maxv = max(temp_list)
			f.write("%6.6f\t%6.6f\n"%(frame.frameValue + k*tbystep, maxv))
		k += 1
	f.close()


def get_max_ne(dbpath,fname="max_pe.txt"):
	"""
	Get Maximum Nominal Strains (Max. principal)

	Parameters
	----------
	dbpath  : str
		Abaqus ODB file
	fname   : str
		Filename for output data
	"""
	odb = openOdb(path=dbpath)
	f = open(fname,"w")
	k = 0
	for step in odb.steps.keys():
		tbystep = odb.steps[step].frames[-1].frameValue
		for frame in odb.steps[step].frames:
			temp_list = []
			for td in frame.fieldOutputs['NE'].values:
				temp_list.append(td.maxPrincipal)
			maxv = max(temp_list)
			f.write("%6.6f\t%6.6f\n"%(frame.frameValue + k*tbystep, maxv))
		k += 1
	f.close()
	
	
def get_max_rt(dbpath,fname="max_rt.txt"):
	"""
	Get maximum reactions forces

	Parameters
	----------
	dbpath  : str
		Abaqus ODB file
	fname   : str
		Filename for output data
	"""
	odb = openOdb(path=dbpath)
	f = open(fname,"w")
	k = 0
	for step in odb.steps.keys():
		tbystep = odb.steps[step].frames[-1].frameValue
		for frame in odb.steps[step].frames:
			temp_list = []
			for td in frame.fieldOutputs['RT'].values:
				temp_list.append(td.magnitude)
			maxv = max(temp_list)
			f.write("%6.6f\t%6.6f\n"%(frame.frameValue + k*tbystep, maxv))
		k += 1
	f.close()

def get_max_v(dbpath,fname="max_v.txt"):
	"""
	Get Max. Velocity  (all steps - all nodes - all components)
	
	Parameters
	----------
	dbpath  : str
		Abaqus ODB file
	fname   : str
		Filename for output data
	"""
	odb = openOdb(path=dbpath)
	f = open(fname,"w")
	k = 0
	for step in odb.steps.keys():
		tbystep = odb.steps[step].frames[-1].frameValue
		for frame in odb.steps[step].frames:
			temp_list = []
			for td in frame.fieldOutputs['V'].values:
				temp_list.append(td.magnitude)
			maxv = max(temp_list)
			f.write("%6.6f\t%6.6f\n"%(frame.frameValue + k*tbystep, maxv))
		k += 1
	f.close()


def get_nodes_coordinates(dbpath,inst,stepname,nframe=-1,fname="nodes.txt"):
	"""
	Get nodes coordinates from meshed instance // last frame by default
	
	Parameters
	----------
	dbpath   : str
		Abaqus ODB file
	inst     : str  
		Instance name
	stepname : str  
		Step name
	nframe   : int  
		Number of frame
	fname    : str
		Filename for output data
	"""
	odb = openOdb(path=dbpath)
	f = open(fname,"w")
	_inst = odb.rootAssembly.instances[inst]
	ic = odb.rootAssembly.instances[inst].nodes # Initial coordinates
	valofinst = odb.steps[stepname].frames[nframe].fieldOutputs['U'].getSubset(region=_inst).values
	for k,jj in enumerate(valofinst):
		if _inst.embeddedSpace == THREE_D: # 3D case
			#f.write("%g,"%(ic[k].label)) # Write node label ? 
			f.write("%0.4f,%0.4f,%0.4f\n"%(ic[k].coordinates[0]+jj.data[0],
										   ic[k].coordinates[1]+jj.data[1],
										   ic[k].coordinates[2]+jj.data[2]))
		else: # 2D case
			f.write("%0.4f,%0.4f\n"%(ic[k].coordinates[0]+jj.data[0],
									 ic[k].coordinates[1]+jj.data[1]))
	f.close()


def get_nodes_distance(dbpath,node1,node2,inst,stepname,nframe=-1):
	"""
	Calculate distance between two nodes 

	Parameters
	----------	
	dbpath   : str   
		Abaqus ODB file
	node1    : int  
		Number of node 1
	node2    : int  
		Number of node 2
	inst     : str  
		Instance name
	stepname : str  
		Step name
	nframe   : int   
		Number of frame, -1 for last frame (See Python List Indexing)
	"""
	odb = openOdb(path=dbpath)
	_inst = odb.rootAssembly.instances[inst]
	ic = odb.rootAssembly.instances[inst].nodes
	us = odb.steps[stepname].frames[nframe].fieldOutputs['U'].getSubset(region=_inst).values
	xx1 = ic[node1-1].coordinates[0]+us[node1-1].data[0]
	yy1 = ic[node1-1].coordinates[1]+us[node1-1].data[1]
	xx2 = ic[node2-1].coordinates[0]+us[node2-1].data[0]
	yy2 = ic[node2-1].coordinates[1]+us[node2-1].data[1]
	if _inst.embeddedSpace == THREE_D:
		zz1 = ic[node1-1].coordinates[2]+us[node1-1].data[2]
		zz2 = ic[node2-1].coordinates[2]+us[node2-1].data[2]
		d = np.sqrt((xx2-xx1)**2 + (yy2-yy1)**2 + (zz2-zz1)**2)
	else:
		d = np.sqrt((xx2-xx1)**2+(yy2-yy1)**2)
	return d
	

def get_distances(dbpath,M1,M2,inst,stepname,nframe=-1,filename="distances.txt"):
	"""
	Get distances between two arrays of nodes. For example, if M1 and M2 
	are two arrays of nodes defined by:
	
	::
	
		M1 = (1,2,3)
		M2 = (4,5,6)
	
	it returns the distances between 1-4, 2-5 and 3-6 nodes.
	
	Parameters
	----------
	dbpath  : str
		Abaqus ODB file
	M1      : tuple, list 
		Arrays of nodes, i.e.  M1 = (3,9,31)
	M2      : tuple, list  
		Arrays of nodes, i.e.  M2 = (10,18,38)
	inst    : str
		Instance name
	stepname: str
		Step name
	nframe  : int
		Number of frame, -1 for last frame (See Python List Indexing)
	filename: str
		Name of output file
	"""
	f = open(filename,"w")
	for ii,jj in enumerate(M1):
		f.write("%4.6f\n"%(get_nodes_distance(dbpath,jj,M2[ii],inst,stepname,nframe),))
	f.close()
	

def get_elements(dbpath,inst,fname="elements.txt"):
	"""
	Get connectivity elements.
	
	Parameters
	----------
	dbpath : str
		Abaqus ODB file
	inst   : str
		Instance name
	fname  : str
		Name of output file
	"""
	odb = openOdb(path=dbpath)
	f = open(fname,"w")
	_inst = odb.rootAssembly.instances[inst]
	for el in _inst.elements:
		econn = el.connectivity
		if len(econn)==2:
			f.write("%g,%g\n"%(econn[0],econn[1]))
		elif len(econn)==3:
			f.write("%g,%g,%g\n"%(econn[0],econn[1]))
		elif len(econn)==4:
			f.write("%g,%g,%g,%g\n"%(econn[0],econn[1]))
		elif len(econn)==6:
			f.write("%g,%g,%g,%g,%g,%g\n"
					%(econn[0],econn[1],econn[2],
					  econn[3],econn[4],econn[5]))
		elif len(econn)==8:
			f.write("%g,%g,%g,%g,%g,%g,%g,%g\n"
					%(econn[0],econn[1],econn[2],econn[3],
					  econn[4],econn[5],econn[6],econn[7]))
		else:
			raise SyntaxError
	f.close()
	

def find_deformable_body(dbpath):
	"""
	Return name of first deformable body in the analysis.
	
	Parameters
	----------
	dbpath : str
		Abaqus ODB file
	"""
	odb = openOdb(path=dbpath)
	for name,_inst in odb.rootAssembly.instances.items():
		if _inst.type == DEFORMABLE_BODY and name!="ASSEMBLY":
			return name
	return None
	

def find_last_step(dbpath):
	"""
	Return last step name from odb file
	
	Parameters
	----------
	dbpath : str
		Abaqus ODB file
	"""
	odb = openOdb(path=dbpath)
	_steps = odb.steps.keys()
	last_step = _steps[-1]
	return last_step


def get_steps(dbpath):
	"""
	Return all steps names from odb file, also include 
	additional information as time duration, number of frames 
	per step and procedure type. 
	
	Parameters
	----------
	dbpath : str
		Abaqus ODB file
	"""
	odb = openOdb(path=dbpath)
	_steps = []
	for _name,_stp in odb.steps.items():
		_time = _stp.timePeriod
		_procedure = _stp.procedure
		_nframes = len(_stp.frames)
		_steps.append((_name,_time,_nframes,_procedure))
	return _steps


def get_materials(dbpath):
	"""
	Return all materials names from odb file

	Parameters
	----------
	dbpath : str
		Abaqus ODB file
	"""
	odb = openOdb(path=dbpath)
	_materials = []
	for _name in odb.materials.items():
		_materials.append(_name)
	return _materials


def get_materials_properties(dbpath): #<un-named>nook
	"""
	Get elastic/plastic properties for all materials in the odb file.
	Return a list of tuples, one tuple for every material.
	
	Parameters
	----------
	dbpath : str
		Abaqus ODB file
	"""
	odb = openOdb(path=dbpath)
	data = []
	for _name,_mat in odb.materials.items():
		_elastic_mod = _mat.elastic.table[0][0]
		_poisson = _mat.elastic.table[0][1]
		_plastic = _mat.plastic.table
		data.append((_name,_elastic_mod,_poisson,_plastic))
	return data
	
	
def get_parts(dbpath):
	"""
	Get parts names and types. Return a list of tuples.

	Parameters
	----------
	dbpath : str
		Abaqus ODB file
	"""
	odb = openOdb(path=dbpath)
	_parts = []
	for _name,_prt in odb.parts.items():
		_type = _prt.type
		_parts.append((_name,_type))
	return _parts

	
def get_instances(dbpath):
	"""
	Get instances names. Return a list of tuples.
	
	Parameters
	----------
	dbpath : str
		Abaqus ODB file
	"""
	odb = openOdb(path=dbpath)
	_instances = []
	for _name,_inst in odb.rootAssembly.instances.items():
		_nodes = len(_inst.nodes)
		_elements = len(_inst.elements)
		_instances.append((_name,_nodes,_elements))
	return _instances

	
def get_job(dbpath):
	"""
	Get job info:
	
    - Analysis code (type of analysis i.e. Dynamic/Explicit)
    - Creation time (date + time string)
    - Precision (double/single)
	
	Parameters
	----------
	dbpath : str
		Abaqus ODB file
	"""
	odb = openOdb(path=dbpath)
	analysis_code = odb.jobData.analysisCode
	creation_time = odb.jobData.creationTime
	precision = odb.jobData.precision
	return [(analysis_code,creation_time,precision)]


if __name__ == '__main__':
	pass
