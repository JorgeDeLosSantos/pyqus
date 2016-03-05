# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-2 replay file
# Internal Version: 2014_08_22-09.00.46 134497
# Run by User on Fri Mar 04 16:00:32 2016
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
o1 = session.openOdb(
    name='C:/Users/User/Desktop/LABPro/PX1505 - PyQus/pyqus/pyqus/odb/beam.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: C:/Users/User/Desktop/LABPro/PX1505 - PyQus/pyqus/pyqus/odb/beam.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       1
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    renderBeamProfiles=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=807.558, 
    farPlane=1189.55, width=779.189, height=286.068, cameraPosition=(716.81, 
    537.06, 634.155), cameraUpVector=(-0.345478, 0.867012, -0.359075), 
    cameraTarget=(128.5, 40.0001, 7.62939e-005))
session.viewports['Viewport: 1'].view.setValues(nearPlane=836.847, 
    farPlane=1160.28, width=807.449, height=296.443, cameraPosition=(630.734, 
    542.159, 700.67), cameraUpVector=(-0.378961, 0.859084, -0.34404), 
    cameraTarget=(128.423, 40.0047, 0.0594864))
session.viewports['Viewport: 1'].view.setValues(nearPlane=833.844, 
    farPlane=1163.28, width=804.551, height=295.379, cameraPosition=(630.734, 
    542.159, 700.67), cameraUpVector=(-0.257683, 0.863277, -0.433997), 
    cameraTarget=(128.423, 40.0047, 0.0594902))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=799.665, 
    farPlane=1195.6, width=771.572, height=283.272, cameraPosition=(877.013, 
    539.161, 431.09), cameraUpVector=(-0.369969, 0.859464, -0.352767), 
    cameraTarget=(128.424, 40.0047, 0.0580673))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.stop()
session.animationController.showLastFrame()
session.viewports['Viewport: 1'].view.setValues(nearPlane=859.922, 
    farPlane=1136.42, width=829.712, height=304.617, cameraPosition=(482.98, 
    170.379, 923.688), cameraUpVector=(-0.0917077, 0.990241, -0.104936), 
    cameraTarget=(128.079, 39.6815, 0.489815))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=806.409, 
    farPlane=1190.02, width=778.079, height=285.661, cameraPosition=(816.784, 
    341.59, 656.215), cameraUpVector=(-0.245555, 0.952428, -0.180513), 
    cameraTarget=(128.249, 39.7687, 0.3536))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=775.399, 
    farPlane=1220.73, width=748.159, height=274.676, cameraPosition=(1076.96, 
    336.405, 86.9286), cameraUpVector=(-0.301531, 0.952639, 0.0394865), 
    cameraTarget=(128.393, 39.7658, 0.0392609))
session.viewports['Viewport: 1'].view.setValues(nearPlane=818.654, 
    farPlane=1177.69, width=789.894, height=289.998, cameraPosition=(787.462, 
    323.644, 693.255), cameraUpVector=(-0.314881, 0.945077, -0.0876338), 
    cameraTarget=(128.275, 39.7606, 0.285461))
o1 = session.openOdb(
    name='C:/Users/User/Desktop/LABPro/PX1505 - PyQus/pyqus/pyqus/odb/hole_plate.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: C:/Users/User/Desktop/LABPro/PX1505 - PyQus/pyqus/pyqus/odb/hole_plate.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.69291, 
    farPlane=3.11665, width=2.18609, height=0.802591, viewOffsetX=0.0599207, 
    viewOffsetY=-0.00543801)
session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.15908, 
    farPlane=2.69212, width=2.27953, height=0.836899, viewOffsetX=0.125945, 
    viewOffsetY=-0.0525555)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.13178, 
    farPlane=2.71942, width=2.40417, height=0.882655, viewOffsetX=0.0994498, 
    viewOffsetY=-0.041943)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    triadFont='-*-verdana-medium-r-normal-*-*-120-*-*-p-*-*-*', 
    legendFont='-*-verdana-medium-r-normal-*-*-120-*-*-p-*-*-*', 
    titleFont='-*-verdana-medium-r-normal-*-*-120-*-*-p-*-*-*', 
    stateFont='-*-verdana-medium-r-normal-*-*-120-*-*-p-*-*-*')
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    ORIENT_ON_DEF, ))
#* The basic plot option 'render beam profiles' is supported only in deformed 
#* or undeformed or contour plot modes.
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.13486, 
    farPlane=2.71634, width=2.12739, height=0.781042, viewOffsetX=-0.0415284, 
    viewOffsetY=-0.0312618)
o1 = session.openOdb(
    name='C:/Users/User/Desktop/LABPro/PX1505 - PyQus/pyqus/pyqus/odb/frame.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: C:/Users/User/Desktop/LABPro/PX1505 - PyQus/pyqus/pyqus/odb/frame.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          6
#: Number of Steps:              1
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.26234, 
    farPlane=7.44261, width=5.58337, height=2.04985, viewOffsetX=0.132381, 
    viewOffsetY=-0.258394)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.71446, 
    farPlane=8.78319, width=4.20331, height=1.54318, cameraPosition=(6.30622, 
    5.88934, 2.9744), cameraUpVector=(-0.373976, 0.718838, -0.586016), 
    cameraTarget=(2.23594, 1.29193, -0.067497), viewOffsetX=0.0996598, 
    viewOffsetY=-0.194526)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.87244, 
    farPlane=8.6252, width=3.8385, height=1.40925, viewOffsetX=0.237046, 
    viewOffsetY=-0.258852)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.31373, 
    farPlane=8.79417, width=4.18615, height=1.53689, cameraPosition=(8.06012, 
    0.850479, 4.04565), cameraUpVector=(0.26592, 0.938736, -0.219231), 
    cameraTarget=(2.50547, 1.49915, 0.0856564), viewOffsetX=0.258515, 
    viewOffsetY=-0.282296)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.02051, 
    farPlane=9.21949, width=3.95516, height=1.45208, cameraPosition=(9.23027, 
    2.96506, -0.244406), cameraUpVector=(-0.218924, 0.974855, -0.041587), 
    cameraTarget=(2.54957, 1.47939, 0.098395), viewOffsetX=0.24425, 
    viewOffsetY=-0.266718)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.08454, 
    farPlane=9.15546, width=3.76527, height=1.38236, viewOffsetX=0.189854, 
    viewOffsetY=-0.268424)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.11113, 
    farPlane=8.85946, width=3.78496, height=1.38959, cameraPosition=(7.61523, 
    3.97743, 3.69263), cameraUpVector=(-0.222833, 0.925674, -0.305733), 
    cameraTarget=(2.325, 1.51695, 0.0987631), viewOffsetX=0.190847, 
    viewOffsetY=-0.269827)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.9422, 
    farPlane=9.02838, width=5.64378, height=2.07203, viewOffsetX=0.00586349, 
    viewOffsetY=-0.0979521)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.38399, 
    farPlane=7.87636, width=7.07367, height=2.597, viewOffsetX=0.450476, 
    viewOffsetY=-0.287627)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.56372, 
    farPlane=9.83691, width=7.35911, height=2.7018, viewOffsetX=0.15867, 
    viewOffsetY=-0.122393)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.42779, 
    farPlane=7.83256, width=6.64042, height=2.43794, viewOffsetX=0.172798, 
    viewOffsetY=-0.0806127)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
cliCommand("""1.2e8""")
#: 120000000.0
cliCommand("""1.2e8/1e6""")
#: 120.0
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.34868, 
    farPlane=7.91166, width=6.55871, height=2.40794, viewOffsetX=0.154455, 
    viewOffsetY=-0.105441)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Max. In-Plane Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='PEEQ', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='PEMAG', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.4253, 
    farPlane=7.83505, width=6.66502, height=2.44697, viewOffsetX=0.316353, 
    viewOffsetY=-0.0975978)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.20698, 
    farPlane=8.05337, width=7.91627, height=2.90635, viewOffsetX=0.488119, 
    viewOffsetY=-0.507843)
cliCommand("""from obdAcces import *""")
#* ImportError: No module named obdAcces
cliCommand("""from odbAcces import *""")
#* ImportError: No module named odbAcces
cliCommand("""from odbAccess import *""")
cliCommand("""odb=openOdb(path="frame.odb")""")
#: Warning: The database has been opened with readOnly flag on. It will remain readOnly.
cliCommand("""odb=openOdb(path="frame.odb")""")
#: Warning: The database has been opened with readOnly flag on. It will remain readOnly.
cliCommand("""odb.steps['Step-1'].frames[-1].frameValue""")
#: 1.0
cliCommand("""odb.steps['Step-1'].frames""")
#: openOdb(r'C:/Users/User/Desktop/LABPro/PX1505 - PyQus/pyqus/pyqus/odb/frame.odb').steps['Step-1'].frames
cliCommand("""odb.steps['Step-1'].frames""")
#: openOdb(r'C:/Users/User/Desktop/LABPro/PX1505 - PyQus/pyqus/pyqus/odb/frame.odb').steps['Step-1'].frames
cliCommand("""odb.steps['Step-1'].frames()""")
#* TypeError: 'OdbFrameArray' object is not callable
cliCommand("""len(odb.steps['Step-1'].frames)""")
#: 2
cliCommand("""odb.steps['Step-1'].frames[1]""")
#: openOdb(r'C:/Users/User/Desktop/LABPro/PX1505 - PyQus/pyqus/pyqus/odb/frame.odb').steps['Step-1'].frames[1]
cliCommand("""odb.steps['Step-1'].frames[2]""")
#* IndexError: Sequence index out of range
cliCommand("""odb.steps['Step-1'].frames[0]""")
#: openOdb(r'C:/Users/User/Desktop/LABPro/PX1505 - PyQus/pyqus/pyqus/odb/frame.odb').steps['Step-1'].frames[0]
cliCommand("""odb.steps['Step-1'].frames[1].fieldOutputs['S'].values""")
#: openOdb(r'C:/Users/User/Desktop/LABPro/PX1505 - PyQus/pyqus/pyqus/odb/frame.odb').steps['Step-1'].frames[1].fieldOutputs['S'].values
cliCommand("""odb.steps['Step-1'].frames[1].fieldOutputs['S'].values.mises""")
#* AttributeError: 'FieldValueArray' object has no attribute 'mises'
cliCommand("""odb.steps['Step-1'].frames[1].fieldOutputs['S'].values[0].mises""")
#: 0.0
cliCommand("""len(odb.steps['Step-1'].frames[1].fieldOutputs['S'].values)""")
\
    #: 5
cliCommand("""odb.steps['Step-1'].frames[1].fieldOutputs['S'].values[5].mises""")
#* IndexError: Sequence index out of range
cliCommand("""odb.steps['Step-1'].frames[1].fieldOutputs['S'].values[4].mises""")
#: 83333336.0
cliCommand("""odb.steps['Step-1'].frames[1].fieldOutputs['S'].values[4].mises/1e6""")
#: 83.333336
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.44981, 
    farPlane=7.81054, width=6.42242, height=2.3579, viewOffsetX=0.38209, 
    viewOffsetY=-0.204466)
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.52203, 
    farPlane=9.8786, width=7.77018, height=2.85271, viewOffsetX=0.564107, 
    viewOffsetY=-0.322811)
cliCommand("""odb.rootAssembly.instances['ARMADURA-1'].elements""")
#: openOdb(r'C:/Users/User/Desktop/LABPro/PX1505 - PyQus/pyqus/pyqus/odb/frame.odb').rootAssembly.instances['ARMADURA-1'].elements
cliCommand("""len(odb.rootAssembly.instances['ARMADURA-1'].elements)""")
#: 5
cliCommand("""len(odb.rootAssembly.instances['ARMADURA-1'].nodes)""")
#: 4
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.5731, 
    farPlane=9.82752, width=6.51348, height=2.39133, viewOffsetX=0.658241, 
    viewOffsetY=-0.201159)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.52204, 
    farPlane=9.87858, width=7.7702, height=2.85272, viewOffsetX=0.754792, 
    viewOffsetY=-0.132166)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(COMPONENT, 'RF1'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(COMPONENT, 'RF2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Max. In-Plane Principal'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.59717, 
    farPlane=9.80705, width=7.43365, height=2.72916, viewOffsetX=0.632929, 
    viewOffsetY=-0.138045)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.52973, 
    farPlane=9.8709, width=6.90343, height=2.5345, viewOffsetX=0.831024, 
    viewOffsetY=-0.275572)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.68189, 
    farPlane=9.71873, width=5.53817, height=2.03326, viewOffsetX=0.395828, 
    viewOffsetY=-0.137546)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
