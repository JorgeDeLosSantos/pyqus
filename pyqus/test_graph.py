# -*- coding: mbcs -*-
from graph import *

plot_elements(figname=r"img/elements_frame.svg",nodesfile=r"dat/nodes_frame.txt",elementsfile=r"dat/elements_frame.txt")
#plot_elements(figname=r"img/elements_beam.svg",nodesfile=r"dat/nodes_beam.txt",elementsfile=r"dat/elements_beam.txt")
plot3D_elements(figname=r"img/elements_hole_plate.svg",nodesfile=r"dat/nodes_hole_plate.txt",elementsfile=r"dat/elements_hole_plate.txt")
plot3D_elements(figname=r"img/elements_bending_test.svg",nodesfile=r"dat/nodes_bending_test.txt",elementsfile=r"dat/elements_bending_test.txt")
