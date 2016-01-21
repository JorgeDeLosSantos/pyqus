# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

def import_defbody(odbpath,nframe,inst="PLATE",nstep=1,pname="plate",model="Model-1"):
	mdb.models[model].PartFromOdb(frame=int(nframe), instance=inst, name=pname, 
    odb=session.openOdb(odbpath), shape=DEFORMED, step=nstep)


def create_2d_analytical(asname,stp_path,MODEL_NAME):
	print "Current part: ",asname
	mdb.openStep(stp_path + asname + ".STEP", scaleFromFile=OFF)
	mdb.models[MODEL_NAME].ConstrainedSketchFromGeometryFile(geometryFile=mdb.acis, name=asname)
	mdb.models[MODEL_NAME].ConstrainedSketch(name='__profile__', sheetSize=10.0)
	mdb.models[MODEL_NAME].sketches['__profile__'].sketchOptions.setValues(gridOrigin=(0.0, 0.0))
	mdb.models[MODEL_NAME].sketches['__profile__'].retrieveSketch(sketch=mdb.models[MODEL_NAME].sketches[asname])
	mdb.models[MODEL_NAME].Part(dimensionality=TWO_D_PLANAR, name=asname[7::], type=ANALYTIC_RIGID_SURFACE)
	mdb.models[MODEL_NAME].parts[asname[7::]].AnalyticRigidSurf2DPlanar(sketch=mdb.models[MODEL_NAME].sketches['__profile__'])
	del mdb.models[MODEL_NAME].sketches['__profile__']

def create_2d_deformable(bname,stp_path,MODEL_NAME):
	mdb.openStep(stp_path + 'sketch_mp_mod' + '.STEP', scaleFromFile=OFF)
	mdb.models[MODEL_NAME].ConstrainedSketchFromGeometryFile(geometryFile=mdb.acis, name=bname)
	mdb.models[MODEL_NAME].ConstrainedSketch(name='__profile__', sheetSize=10.0)
	mdb.models[MODEL_NAME].sketches['__profile__'].sketchOptions.setValues(gridOrigin=(0.0, 0.0))
	mdb.models[MODEL_NAME].sketches['__profile__'].retrieveSketch(sketch=mdb.models[MODEL_NAME].sketches[bname])
	mdb.models[MODEL_NAME].Part(dimensionality=TWO_D_PLANAR, name=bname, type=DEFORMABLE_BODY)
	mdb.models[MODEL_NAME].parts[bname].BaseShell(sketch=mdb.models[MODEL_NAME].sketches['__profile__'])
	del mdb.models[MODEL_NAME].sketches['__profile__']

def create_material(matname,dens,elmod,nu,plastic,MODEL_NAME):
	mdb.models[MODEL_NAME].Material(name=matname)
	mdb.models[MODEL_NAME].materials[matname].Density(table=((dens, ), 
		))
	mdb.models[MODEL_NAME].materials[matname].Elastic(table=((elmod, 
		nu), ))
	mdb.models[MODEL_NAME].materials[matname].Plastic(table=plastic)
	
def create_reference_point(_part,idxvert,MODEL_NAME,center=False):
	"""
	Create a reference point in a rigid part.
	
	Parameters:
	-----------
	
	_part      :   Part name
	idxvert    :   Index of vertex (i.e. 0,1,2,3...)
	MODEL_NAME :   Name of model
	center     :   Puts the point on center
	
	"""
	if not(center):
		mdb.models[MODEL_NAME].parts[_part].ReferencePoint(
		point=mdb.models[MODEL_NAME].parts[_part].vertices[idxvert])
	else:
		mdb.models[MODEL_NAME].parts[_part].ReferencePoint(point=
		mdb.models[MODEL_NAME].parts[_part].InterestingPoint(
		mdb.models[MODEL_NAME].parts[_part].edges[0], CENTER))
	

def translate_instance(inst,vect,MODEL_NAME):
	mdb.models[MODEL_NAME].rootAssembly.instances[inst].translate(vector=vect)
