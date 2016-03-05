# -*- coding: mbcs -*-

import_error_str = """
Please try run in Abaqus/CAE script mode, as follows:

>> abaqus cae noGUI="test_script.py"

or verify that you have Abaqus installed.
"""

try:
    from part import *
    from material import *
    from section import *
    from assembly import *
    from step import *
    from interaction import *
    from load import *
    from mesh import *
    from sketch import *
except ImportError:
    print import_error_str
    pass


def import_deformed_body(odbpath,inst,nstep,nframe=-1,partname="Imported-Part",model="Model-1"):
    """
    Import deformed body from odbpath, in a specified frame, in a specified step,
    and save this as partname in the model.
    """
    mdb.models[model].PartFromOdb(frame=int(nframe), instance=inst, name=partname, 
    odb=session.openOdb(odbpath), shape=DEFORMED, step=nstep)


def create_2d_analitycal_from_file(partname,stp_path,MODEL_NAME):
    mdb.openStep(stp_path + partname + ".STEP", scaleFromFile=OFF)
    mdb.models[MODEL_NAME].ConstrainedSketchFromGeometryFile(geometryFile=mdb.acis, name=partname)
    mdb.models[MODEL_NAME].ConstrainedSketch(name='__profile__', sheetSize=10.0)
    mdb.models[MODEL_NAME].sketches['__profile__'].sketchOptions.setValues(gridOrigin=(0.0, 0.0))
    mdb.models[MODEL_NAME].sketches['__profile__'].retrieveSketch(sketch=mdb.models[MODEL_NAME].sketches[partname])
    mdb.models[MODEL_NAME].Part(dimensionality=TWO_D_PLANAR, name=partname[7::], type=ANALYTIC_RIGID_SURFACE)
    mdb.models[MODEL_NAME].parts[partname[7::]].AnalyticRigidSurf2DPlanar(sketch=mdb.models[MODEL_NAME].sketches['__profile__'])
    del mdb.models[MODEL_NAME].sketches['__profile__']

def create_2d_deformable_from_file(bname,stp_path,MODEL_NAME):
    mdb.openStep(stp_path + 'sketch_mp_mod' + '.STEP', scaleFromFile=OFF)
    mdb.models[MODEL_NAME].ConstrainedSketchFromGeometryFile(geometryFile=mdb.acis, name=bname)
    mdb.models[MODEL_NAME].ConstrainedSketch(name='__profile__', sheetSize=10.0)
    mdb.models[MODEL_NAME].sketches['__profile__'].sketchOptions.setValues(gridOrigin=(0.0, 0.0))
    mdb.models[MODEL_NAME].sketches['__profile__'].retrieveSketch(sketch=mdb.models[MODEL_NAME].sketches[bname])
    mdb.models[MODEL_NAME].Part(dimensionality=TWO_D_PLANAR, name=bname, type=DEFORMABLE_BODY)
    mdb.models[MODEL_NAME].parts[bname].BaseShell(sketch=mdb.models[MODEL_NAME].sketches['__profile__'])
    del mdb.models[MODEL_NAME].sketches['__profile__']

def create_material(name,density,E,nu,plastic=None,MODEL_NAME="Model-01"):
    """
    Temperature independent properties
    """
    mdb.models[MODEL_NAME].Material(name=matname)
    mdb.models[MODEL_NAME].materials[matname].Density(table=((dens, ),))
    mdb.models[MODEL_NAME].materials[matname].Elastic(table=((E, nu), ))
    if plastic not is None:
        mdb.models[MODEL_NAME].materials[matname].Plastic(table=plastic)
    
    
def create_reference_point(_part,idxvert,center=False,,MODEL_NAME):
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
    

def translate_instance(inst,vector,MODEL_NAME):
    mdb.models[MODEL_NAME].rootAssembly.instances[inst].translate(vector=vector)
    
    
if __name__=='__main__':
    pass
