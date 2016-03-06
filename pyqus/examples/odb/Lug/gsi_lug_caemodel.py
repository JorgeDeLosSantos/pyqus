#
# Getting Started with Abaqus: Interactive Edition
#
# Script for elastic lug example
#
from abaqus import *
from abaqusConstants import *
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
session.journalOptions.setValues(replayGeometry=COORDINATE, 
    recoverGeometry=COORDINATE)
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
Mdb()

mdb.models.changeKey(fromName='Model-1', toName='standard')

session.viewports['Viewport: 1'].setValues(displayedObject=None)

##  Sketch profile of the lug

s = mdb.models['standard'].ConstrainedSketch(name='__profile__', 
    sheetSize=0.25)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(decimalPlaces=3)
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(-0.0275, 0.0225), point2=(0.02125, -0.01375))
s.delete(objectList=(g.findAt((0.02125, 0.004375)), ))
s.EqualLengthConstraint(entity1=g.findAt((-0.003125, -0.01375)), 
    entity2=g.findAt((-0.003125, 0.0225)))
s.ObliqueDimension(vertex1=v.findAt((-0.0275, -0.01375)), vertex2=v.findAt((
    0.02125, -0.01375)), textPoint=(-0.010330107063055, -0.023654306307435), 
    value=0.1)
s.move(vector=(-0.025625, 0.0), objectList=(g.findAt((-0.0275, 0.004375)), 
    g.findAt((0.0225, -0.01375)), g.findAt((0.0225, 0.0225))))    
session.viewports['Viewport: 1'].view.fitView()
s.ObliqueDimension(vertex1=v.findAt((-0.053125, 0.0225)), vertex2=v.findAt((
    -0.053125, -0.01375)), textPoint=(-0.0564765408635139, 
    0.00896133482456207), value=0.05)
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.230597, 
    farPlane=0.279546, width=0.144889, height=0.121934)
s.Arc3Points(point1=(0.046875, 0.03625), point2=(0.046875, -0.01375), point3=(
    0.0625, 0.02375))
s.TangentConstraint(entity1=g.findAt((-0.003125, 0.03625)), entity2=g.findAt((
    0.0657, 0.01125)))
s.move(vector=(-0.001797, 0.0), objectList=(g.findAt((-0.053125, 0.01125)), 
    g.findAt((-0.003125, -0.01375)), g.findAt((-0.003125, 0.03625)), g.findAt((
    0.071875, 0.01125))))
s.TangentConstraint(entity1=g.findAt((-0.004922, -0.01375)), entity2=g.findAt((
    0.070078, 0.01125)))
session.viewports['Viewport: 1'].view.fitView()
s.RadialDimension(curve=g.findAt((0.070078, 0.01125)), textPoint=(
    0.0655877739191055, -0.0193991288542748), radius=0.025)
d[2].setValues(reference=ON)
s.CircleByCenterPerimeter(center=(0.0425, 0.0125), point1=(0.0525, 0.01625))
s.ConcentricConstraint(entity1=g.findAt((0.0325, 0.00875)), entity2=g.findAt((
    0.070078, 0.01125)))
s.RadialDimension(curve=g.findAt((0.035078, 0.0075)), textPoint=(
    0.0297759883105755, 0.0219836011528969), radius=0.015)
s.VerticalDimension(vertex1=v.findAt((0.045078, 0.01125)), vertex2=v.findAt((
    0.059123, 0.016517)), textPoint=(0.0632773488759995, 0.0129371425136924), 
    value=0.0)
s.VerticalDimension(vertex1=v.findAt((0.045078, 0.01125)), vertex2=v.findAt((
    0.067003, 0.023263)), textPoint=(0.0746369957923889, 0.012744665145874), 
    value=0.0)
s.move(vector=(0.034922, 0.00375), objectList=(g.findAt((-0.054922, 0.01125)), 
    g.findAt((-0.004922, -0.01375)), g.findAt((-0.004922, 0.03625)),
    g.findAt((0.070078, 0.01125)), g.findAt((0.030078, 0.01125))))
p = mdb.models['standard'].Part(name='Lug', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['standard'].parts['Lug']
p.BaseSolidExtrude(sketch=s, depth=0.02)
s.unsetPrimaryObject()
p = mdb.models['standard'].parts['Lug']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['standard'].sketches['__profile__']

c, f, e, v, d  = p.cells, p.faces, p.edges, p.vertices, p.datums


##
##  Create material 'Steel'
##
mdb.models['standard'].Material('Steel')
mdb.models['standard'].materials['Steel'].Elastic(table=((200.0E9, 0.3), ))
##
##  Create solid section 
##
mdb.models['standard'].HomogeneousSolidSection(name='LugSection', 
    material='Steel', thickness=1.0)
##
##  Assign solid section 
##
c = p.cells
cells = c
region = regionToolset.Region(cells=cells)
p.SectionAssignment(region=region, sectionName='LugSection', offset=0.0)
##
##  Set coordinate system (done by default)
##
a = mdb.models['standard'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
##
##  Instance the lug
##
a.Instance(name='Lug-1', part=p, dependent=ON)
##
##  Create a static general step
##
mdb.models['standard'].StaticStep(name='LugLoad', 
    previous='Initial', description='Apply uniform pressure to the hole')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='LugLoad')
##
##  Modify output requests
##
mdb.models['standard'].fieldOutputRequests['F-Output-1'].setValues(
    variables=('S', 'U', 'RF', 'NFORC'), region=MODEL)
del mdb.models['standard'].historyOutputRequests['H-Output-1']
##
##  Apply encastre bc to left end
##
f = a.instances['Lug-1'].faces
faces = f.findAt(((-0.02, 0.006667, 0.013333), ))
region = regionToolset.Region(faces=faces)
mdb.models['standard'].EncastreBC(name='Fix left end',
    createStepName='LugLoad', region=region)

session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
##
##  Partition the lug
##
c, f, e, v, d  = p.cells, p.faces, p.edges, p.vertices, p.datums

pickedCells = c.findAt(((-0.02, 0.006667, 0.013333), ))
p.PartitionCellByPlaneThreePoints(point1=v.findAt(coordinates=(0.095, 0.015, 
    0.02)), cells=pickedCells, point2=p.InterestingPoint(edge=e.findAt(
    coordinates=(0.08, 0.03, 0.02)), rule=MIDDLE), point3=p.InterestingPoint(
    edge=e.findAt(coordinates=(0.08, 0.03, 0.0)), rule=MIDDLE))
c, f, e, v, d  = p.cells, p.faces, p.edges, p.vertices, p.datums

##
##  Apply pressure load to bottom of hole
##
a.regenerate()
s = a.instances['Lug-1'].faces
side1Faces = s.findAt(((0.094968, 0.01402, 0.013333), ))
region = regionToolset.Region(side1Faces=side1Faces)
mdb.models['standard'].Pressure(name='Pressure load',
    createStepName='LugLoad', region=region, magnitude=5.0E7)


##
##  Create partitions
##
pickedCells = c.findAt(((-0.02, 0.006667, 0.006667), ), ((-0.02, 0.023333, 
    0.013333), ))
p.PartitionCellByPlaneThreePoints(cells=pickedCells, point1=p.InterestingPoint(
    edge=e.findAt(coordinates=(0.069393, 0.004393, 0.0)), rule=MIDDLE), 
    point2=p.InterestingPoint(edge=e.findAt(coordinates=(0.069393, 0.004393, 
    0.02)), rule=MIDDLE), point3=p.InterestingPoint(edge=e.findAt(
    coordinates=(0.090607, 0.025607, 0.02)), rule=MIDDLE))

c, f, e, v, d  = p.cells, p.faces, p.edges, p.vertices, p.datums

p.DatumPointByEdgeParam(edge=e.findAt(coordinates=(0.055, -0.01, 0.02)), 
    parameter=0.25)
pickedCells = c.findAt(((-0.02, 0.006667, 0.006667), ), ((-0.02, 0.023333, 
    0.013333), ))
p.PartitionCellByPlanePointNormal(point=d[5], normal=e.findAt(coordinates=(
    0.055, -0.01, 0.02)), cells=pickedCells)
c, f, e, v, d  = p.cells, p.faces, p.edges, p.vertices, p.datums

##
##  Assign global seed
##
p.seedPart(size=0.007)
import re, uti
if re.search('Student', uti.getProductVersion()):
   p.seedPart(size=0.01)
##
##  Assign element type
##
elemType1 = mesh.ElemType(elemCode=C3D20R)
elemType2 = mesh.ElemType(elemCode=C3D15)
elemType3 = mesh.ElemType(elemCode=C3D10M)
cells = c
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
##
##  Generate the mesh
##
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].assemblyDisplay.geometryOptions.setValues(
    datumPoints=OFF)
##
##  Create job
##
a.regenerate()
mdb.Job(name='Lug', model='standard', 
    description='Linear Elastic Steel Connecting Lug')
##
##  Save model database
##
mdb.saveAs('Lug.cae')
##
##  Explicit dynamics model
##
mdb.Model(name='explicit', objectToCopy=mdb.models['standard'])

##
##  add density
##
mdb.models['explicit'].materials['Steel'].Density(table=((7800.0, ), ))

##
##  replace static step with explicit dynamics step
##
a = mdb.models['explicit'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.models['explicit'].ExplicitDynamicsStep(name='LugLoad',
    previous='Initial', maintainAttributes=True, timePeriod=0.005)

##
##  change number of field output intervals to 125
##
mdb.models['explicit'].fieldOutputRequests['F-Output-1'].setValues(
    numIntervals=125)

##
##  change element type to linear and library to EXPLICIT
##
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, 
    hourglassControl=ENHANCED)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=EXPLICIT)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)
p = mdb.models['explicit'].parts['Lug']
c = p.cells
cells = c
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))

if re.search('Student', uti.getProductVersion()):
   p.seedPart(size=0.007)
   p.generateMesh()

##
##  create job
##
mdb.Job(name='expLug', model='explicit', type=ANALYSIS, 
    description='dynamic analysis of lug')

a = mdb.models['standard'].rootAssembly
a.regenerate()
a = mdb.models['explicit'].rootAssembly
a.regenerate()

mdb.save()
