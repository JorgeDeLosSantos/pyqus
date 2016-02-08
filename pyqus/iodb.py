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
import numpy as np
from odbAccess import *
from abaqusConstants import *
	
def get_max_eqvs_bystep(dbpath,nstep=1,fname="max_eqvs.txt"):
	"""
	Get Max. EQV. Mises Stresses
	
	Parameters
	----------
	
	dbpath  :		Abaqus OBD File
	nstep   :       Step number
	fname   :       Filename for output data
	"""
	odb = openOdb(path=dbpath)
	f = open(fname,"w")
	#for step in odb.steps.keys():
	for frame in odb.steps[nstep].frames:
		temp_list = []
		for td in frame.fieldOutputs['S'].values:
			temp_list.append(td.mises)
			#f.write("%s  %s  %s\n"%(step,frame.frameValue,td.mises))
			#f.write("%s  %s  %s  %s\n"%(step,frame.frameValue,td.nodeLabel,td.magnitude))
		maxv = max(temp_list)
		f.write("%6.6f\t%6.4f\n"%(frame.frameValue, maxv))
	f.close()
	
def get_max_eqvs(dbpath,fname="max_eqvs.txt"):
	"""
	Get Max. Von Mises EQV. Stresses (all steps - all nodes)
	
	Parameters
	----------
	
	dbpath  :      Abaqus ODB file
	fname   :      Filename for output data
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
				#f.write("%s  %s  %s\n"%(step,frame.frameValue,td.mises))
				#f.write("%s  %s  %s  %s\n"%(step,frame.frameValue,td.nodeLabel,td.magnitude))
			maxv = max(temp_list)
			f.write("%6.6f\t%6.4f\n"%(frame.frameValue + k*tbystep, maxv))
		k += 1
	f.close()
			
def get_max_pe_bystep(dbpath,nstep=1,fname="max_pe.txt"):
	"""
	Get Max. Plastic Strains (by step - all nodes)
	
	Parameters
	----------
	
	dbpath  :      Abaqus ODB file
	nstep   :      Step number
	fname   :      Filename for output data
	"""
	odb = openOdb(path=dbpath)
	f = open(fname,"w")
	#for step in odb.steps.keys():
	for frame in odb.steps[nstep].frames:
		temp_list = []
		for td in frame.fieldOutputs['PE'].values:
			temp_list.append(td.maxPrincipal)
			#f.write("%s\n"%td)}
			#f.write("%s  %s  %s  %s\n"%(step,frame.frameValue,td.nodeLabel,td.magnitude))
		maxv = max(temp_list)
		f.write("%6.6f\t%6.6f\n"%(frame.frameValue, maxv))
	f.close()

def get_max_pe(dbpath,fname="max_pe.txt"):
	""""
	Get Max. Plastic Strains (all nodes - all steps)
	
	Parameters
	----------
	
	dbpath  :      Abaqus ODB file
	fname   :      Filename for output data
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
	
	dbpath  :      Abaqus ODB file
	fname   :      Filename for output data
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
	
	dbpath  :      Abaqus ODB file
	fname   :      Filename for output data
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
	
	dbpath  :      Abaqus ODB file
	fname   :      Filename for output data
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
		

def get_deformed_sequence(dbpath,inst,fname="sequence.txt"):
	"""
	Untested function, please don't use.
	"""
	odb = openOdb(path=dbpath)
	f = open(fname,"w")
	_inst = odb.rootAssembly.instances[inst]
	ic = odb.rootAssembly.instances[inst].nodes
	#vofplate = odb.steps[stepname].frames[nframe].fieldOutputs['U'].getSubset(region=_inst).values
	#odb.steps[stepname].frames[nframe].fieldOutputs['U'].values
	for _nstep,_step in odb.steps.items():
		for _frame in range(len(odb.steps[_nstep].frames)):
			f.write(40*"="+"\n")
			vofplate = odb.steps[_nstep].frames[_frame].fieldOutputs['U'].getSubset(region=_inst).values
			for k,jj in enumerate(vofplate):
				f.write("%4.6f,%4.6f\n"%(ic[k].coordinates[0]+jj.data[0],ic[k].coordinates[1]+jj.data[1]))
	f.close()

def get_nodes_coords_undef(dbpath,inst,fname="nodes_undef.txt"):
	"""
	Get Nodes coordinates from meshed instance (last frame)
	
	Parameters
	----------
	
	dbpath  :      Abaqus ODB file
	inst    :      Instance name
	fname   :      Filename for output data
	"""
	odb = openOdb(path=dbpath)
	f = open(fname,"w")
	_inst = odb.rootAssembly.instances[inst]
	for node in _inst.nodes:
		f.write("%s,%s\n"%(node.coordinates[0],node.coordinates[1]))
	f.close()

def get_nodes_coordinates(dbpath,inst,stepname,nframe=-1,fname="nodes.txt"):
	"""
	Get nodes coordinates from meshed instance // last frame by default
	
	Parameters
	----------
	
	dbpath   :      Abaqus ODB file
	inst     :      Instance name
	stepname :      Step name
	nframe   :      Number of frame
	fname    :      Filename for output data
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
			f.write("%0.4f,%0.4f\n"%(ic[k].coordinates[0]+jj.data[0]*1e2,
									 ic[k].coordinates[1]+jj.data[1]*1e2))
	f.close()


def get_nodes_distance(dbpath,node1,node2,inst,stepname,nframe=-1):
	"""
	Calculate distance between two nodes

	Parameters
	----------
	
	dbpath   :      Abaqus ODB file
	node1    :      Number of node 1
	node2    :      Number of node 2
	inst     :      Instance name
	stepname :      Step name
	nframe   :      Number of frame, -1 for last frame (See List Indexing)
	"""
	odb = openOdb(path=dbpath)
	_inst = odb.rootAssembly.instances[inst]
	ic = odb.rootAssembly.instances[inst].nodes
	us = odb.steps[stepname].frames[nframe].fieldOutputs['U'].getSubset(region=_inst).values
	xx1 = ic[node1-1].coordinates[0]+us[node1-1].data[0]
	yy1 = ic[node1-1].coordinates[1]+us[node1-1].data[1]
	xx2 = ic[node2-1].coordinates[0]+us[node2-1].data[0]
	yy2 = ic[node2-1].coordinates[1]+us[node2-1].data[1]
	d = np.sqrt((xx2-xx1)**2+(yy2-yy1)**2)
	return d
	
def get_distances(dbpath,inst,M1,M2,stepname,nframe=-1,filename="distances.txt"):
	"""
	Get distances between two arrays of nodes 
	"""
	f = open(filename,"w")
	for ii,jj in enumerate(M1):
		f.write("%4.6f\n"%(get_nodes_distance(dbpath,jj,M2[ii],inst,stepname,nframe),))
	f.close()
	
def get_elements(dbpath,inst,fname="elements.txt"):
	"""
	Get connectivity elements. (For 2D elements)
	
	If is a triangular element, in last node component append "NaN" string (Not a Number), 
	for display purposes.
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
	Return name of first deformable body in the analysis
	"""
	odb = openOdb(path=dbpath)
	for name,_inst in odb.rootAssembly.instances.items():
		if _inst.type == DEFORMABLE_BODY and name!="ASSEMBLY":
			return name
	return None
	
def find_last_step(dbpath):
	"""
	Return last step name from odb file 
	"""
	odb = openOdb(path=dbpath)
	_steps = odb.steps.keys()
	last_step = _steps[-1]
	return last_step

def get_steps(dbpath):
	"""
	Return all steps names from odb file
	"""
	odb = openOdb(path=dbpath)
	data = []
	for _stp in odb.steps.items():
		_time = _stp[1].timePeriod
		_procedure = _stp[1].procedure
		_name = _stp[0]
		_nframes = len(_stp[1].frames)
		data.append((_name,_time,_nframes,_procedure))
	return data
	
def get_materials_properties(dbpath):
	"""
	Return all materials names from odb file
	"""
	odb = openOdb(path=dbpath)
	data = []
	for _mat in odb.materials.items():
		_elastic_mod = _mat[1].elastic.table[0][0]
		_poisson = _mat[1].elastic.table[0][1]
		_density = _mat[1].density.table[0][0]
		_name = _mat[0]
		data.append((_name,_elastic_mod,_poisson,_density))
	return data
	
def get_plastic_properties(dbpath): #<un-named>nook
	"""
	Get elastic/plastic properties for all materials in the odb file
	
	Return a list of tuples, one tuple for every material.
	"""
	odb = openOdb(path=dbpath)
	data = []
	for _mat in odb.materials.items():
		_elastic_mod = _mat[1].elastic.table[0][0]
		_poisson = _mat[1].elastic.table[0][1]
		_plastic = _mat[1].plastic.table
		_name = _mat[0]
		data.append((_name,_elastic_mod,_poisson,_plastic))
	return data
	
	
def get_parts(dbpath):
	"""
	Get parts names. Return a list of names.
	"""
	odb = openOdb(path=dbpath)
	data = []
	for _prt in odb.parts.items():
		_type = _prt[1].type
		_name = _prt[0]
		data.append((_name,_type))
	return data
	
def get_instances(dbpath):
	"""
	Get instances names. Return a list of names.
	"""
	odb = openOdb(path=dbpath)
	data = []
	for _inst in odb.rootAssembly.instances.items():
		_name = _inst[0]
		_nodes = len(_inst[1].nodes)
		_elements = len(_inst[1].elements)
		data.append((_name,_nodes,_elements))
	return data
	
def get_job(dbpath):
	"""
	Get job info:
	
		>> analysis code (type of analysis i.e. Dynamic/Explicit)
		>> creation time (date + time string)
		>> precision (double/single)
	"""
	odb = openOdb(path=dbpath)
	analysis_code = odb.jobData.analysisCode
	creation_time = odb.jobData.creationTime
	precision = odb.jobData.precision
	return [(analysis_code,creation_time,precision)]

if __name__ == '__main__':
	pass
