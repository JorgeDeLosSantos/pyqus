# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-2 replay file
# Internal Version: 2014_08_22-09.00.46 134497
# Run by User on Sat Mar 05 00:50:52 2016
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
#: Abaqus Error: 
#: This error may have occurred due to a change to the Abaqus Scripting
#: Interface. Please see the Abaqus Scripting Manual for the details of
#: these changes. Also see the "Example environment files" section of 
#: the Abaqus Site Guide for up-to-date examples of common tasks in the
#: environment file.
#: Execution of "onCaeGraphicsStartup()" in the site directory failed.
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=258.289886474609, 
    height=146.438812255859)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
import sys
sys.path.insert(9, 
    r'c:/SIMULIA/Abaqus/6.14-2/code/python2.7/lib/abaqus_plugins/examples')
import os
os.system(
    r'"C:\SIMULIA\Abaqus\6.14-2\code\bin\abq6142.exe" fetch job=gsi_frame_caemodel.py')
execfile('gsi_frame_caemodel.py')
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: The model database has been saved to "C:\Users\User\Desktop\LABPro\PX1505 - PyQus\pyqus\pyqus\examples\odb\Frame.cae".
#: The model "explicit" has been created.
#: The model database has been saved to "C:\Users\User\Desktop\LABPro\PX1505 - PyQus\pyqus\pyqus\examples\odb\Frame.cae".
p = mdb.models['explicit'].parts['Frame']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.96404, 
    farPlane=4.75376, width=3.931, height=1.44321, viewOffsetX=0.50064, 
    viewOffsetY=0.00212158)
a = mdb.models['explicit'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['standard'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.02609, 
    farPlane=4.69171, width=3.31614, height=1.21747, viewOffsetX=0.230355, 
    viewOffsetY=0.0421588)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Frame'].submit(consistencyChecking=OFF)
#: The job input file "Frame.inp" has been submitted for analysis.
#: Job Frame: Analysis Input File Processor completed successfully.
#: Job Frame: Abaqus/Standard completed successfully.
#: Job Frame completed successfully. 
o3 = session.openOdb(
    name='C:/Users/User/Desktop/LABPro/PX1505 - PyQus/pyqus/pyqus/examples/odb/Frame.odb')
#: Model: C:/Users/User/Desktop/LABPro/PX1505 - PyQus/pyqus/pyqus/examples/odb/Frame.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       1
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.76535, 
    farPlane=7.56348, width=2.32583, height=0.853896, viewOffsetX=-0.00347275, 
    viewOffsetY=0.00904724)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.85206, 
    farPlane=8.01231, width=4.41256, height=1.62001, viewOffsetX=0.642331, 
    viewOffsetY=0.00498317)
mdb.save()
#: The model database has been saved to "C:\Users\User\Desktop\LABPro\PX1505 - PyQus\pyqus\pyqus\examples\odb\Frame.cae".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='CF', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Max. In-Plane Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.87729, 
    farPlane=7.98708, width=3.71426, height=1.36364, viewOffsetX=-0.0880915, 
    viewOffsetY=-0.146219)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['standard'].parts['Frame']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.94113, 
    farPlane=4.77667, width=4.15775, height=1.52646, viewOffsetX=0.223283, 
    viewOffsetY=-0.153448)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
