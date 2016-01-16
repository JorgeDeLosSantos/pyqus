# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.14-2 replay file
# Internal Version: 2014_08_22-09.00.46 134497
# Run by User on Fri Jan 15 18:37:12 2016
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
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=256.878479003906, 
    height=146.438812255859)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o2 = session.openOdb(name='bending_test.odb')
#: Model: C:/Users/User/Desktop/LABPro/PX1505 - PyQus/pyqus/pyqus/odb/bending_test.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     5
#: Number of Meshes:             5
#: Number of Element Sets:       0
#: Number of Node Sets:          4
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=37.4296, 
    farPlane=42.5241, width=22.1703, height=8.7851, viewOffsetX=0.165751, 
    viewOffsetY=0.0930782)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    triadFont='-*-arial-medium-r-normal-*-*-120-*-*-p-*-*-*', 
    legendFont='-*-arial-medium-r-normal-*-*-120-*-*-p-*-*-*', 
    titleFont='-*-arial-medium-r-normal-*-*-120-*-*-p-*-*-*', 
    stateFont='-*-arial-medium-r-normal-*-*-120-*-*-p-*-*-*')
session.viewports['Viewport: 1'].view.setValues(nearPlane=37.2128, 
    farPlane=42.7409, width=22.0419, height=8.73422, viewOffsetX=-0.0975804, 
    viewOffsetY=0.262952)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=37.0825, 
    farPlane=42.129, width=21.9608, height=8.7021, viewOffsetX=0.0959852, 
    viewOffsetY=0.162927)
session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
