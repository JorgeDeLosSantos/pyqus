# -*- coding: mbcs -*-
"""
Generate a customized PDF or HTML Report from 
an Abaqus OBD file.


NON-Functional - Please don't use.
"""
import glob
import os
import os.path
import shutil
from random import random

import __templates as tmp
from __templates import *
from pyodb import *

def write_mini_report(data,filename="rpt.txt"):
	f = open(filename,"w")
	for item in data:
		for car in item:
			f.write(str(car)+"\n")
		f.write(30*"="+"\n")
	f.close()


def read_mini_report(rptpath="rpt.txt"):
	f = open(rptpath,"r")
	txt = f.readlines()
	data = []
	_mn = []
	for line in txt:
		if line.startswith("=="):
			data.append(tuple(_mn))
			_mn = []
			continue
		_mn.append(line)
	f.close()
	return data


def replace_data(data,template,toreplace):
	_STR = ""
	for x in data:
		_temp_str = template
		for k,y in enumerate(toreplace):
			_temp_str = _temp_str.replace(str(y),str(x[k]))
		_STR += _temp_str
	return _STR


def generate_html_report(dbpath,htmlname="Report.html"):
	# For table of input data
	materials_data = get_materials_properties(dbpath)
	steps_data = get_steps(dbpath)
	instances_data = get_instances(dbpath)
	parts_data = get_parts(dbpath)
	job_data = get_job(dbpath)
	
	parts_rep = ("_partname_","_parttype_")
	instances_rep = ("_instancename_","_instancenodes_","_instanceelements_")
	materials_rep = ("_materialname_","_young_","_poisson_","_density_")
	steps_rep = ("_stepname_","_steptime_","_stepframes_","_stepprocedure_")
	job_rep = ("_jobanalysiscode_","_jobcreationtime_","_jobprecision_")
	
	PARTS_STR = replace_data(parts_data,PARTS_HTML_TEMPLATE,parts_rep)
	INSTANCES_STR = replace_data(instances_data,INSTANCES_HTML_TEMPLATE,instances_rep)
	MATERIALS_STR = replace_data(materials_data,MATERIALS_HTML_TEMPLATE,materials_rep)
	STEPS_STR = replace_data(steps_data,STEPS_HTML_TEMPLATE,steps_rep)
	JOB_STR = replace_data(job_data,JOB_HTML_TEMPLATE,job_rep)
	
	CONTENTS_HTML_TEMPLATE = tmp.CONTENTS_HTML_TEMPLATE.replace("_materialstemplate_",MATERIALS_STR)
	CONTENTS_HTML_TEMPLATE = CONTENTS_HTML_TEMPLATE.replace("_partstemplate_",PARTS_STR)
	CONTENTS_HTML_TEMPLATE = CONTENTS_HTML_TEMPLATE.replace("_instancestemplate_",INSTANCES_STR)
	CONTENTS_HTML_TEMPLATE = CONTENTS_HTML_TEMPLATE.replace("_stepstemplate_",STEPS_STR)
	CONTENTS_HTML_TEMPLATE = CONTENTS_HTML_TEMPLATE.replace("_jobtemplate_",JOB_STR)
	CONTENTS_HTML_TEMPLATE = CONTENTS_HTML_TEMPLATE.replace("_deformedshape_","img/deformed_shape.png")
	CONTENTS_HTML_TEMPLATE = CONTENTS_HTML_TEMPLATE.replace("_vonmises_","img/von_mises.png")
	CONTENTS_HTML_TEMPLATE = CONTENTS_HTML_TEMPLATE.replace("_pestrain_","img/pe_strain.png")
	CONTENTS_HTML_TEMPLATE = CONTENTS_HTML_TEMPLATE.replace("_nestrain_","img/ne_strain.png")
	CONTENTS_HTML_TEMPLATE = CONTENTS_HTML_TEMPLATE.replace("_rtforce_","img/rt_force.png")
	txt = HTML_TEMPLATE.replace("_contents_",CONTENTS_HTML_TEMPLATE)
	
	f = open(htmlname,"w")
	f.write(txt)
	f.close()
	folder_name = htmlname[:-5]
	os.mkdir(folder_name)
	os.mkdir(folder_name+"\\img")
	imgs = glob.glob(os.getcwd()+"\\img\\*.png")
	for img in imgs:
		shutil.move(img,os.getcwd()+"\\"+folder_name+"\\img\\"+os.path.basename(img))
	shutil.move(htmlname,folder_name+"\\"+htmlname)
	#os.startfile(htmlname)
	

if __name__=='__main__':
	pass
	#data = read_mini_report("rpt_parts.txt")
	#replace_data(data,PARTS_TEMPLATE,("_partname_","_parttype_"))
