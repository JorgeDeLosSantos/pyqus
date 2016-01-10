# -*- coding: mbcs -*-
# =============================
# (c) 2015, Jorge De Los Santos
# ITC-Bypasa
# =============================

from odbAccess import *
from abaqusConstants import *
from pyodb import *

region = 'ElementSet . PIBATCH'
outname = 'CFNM     ASSEMBLY_PLATE-1_SURF-1/ASSEMBLY_UPPER_LEFT_02-1_SURF-1'
ODB = r"C:/Users/User/Desktop/LABPro/PI1501 - Rassini-Bypasa/pyscript/2ndev/odb/"+"JB-STP02-2D.odb"

# get_out_history("dbex2.odb",outname,region)
#get_nodes_coords_undef("jobs/JB-STP01-2D.odb","PLATE-1",fname="nodes01.txt")
#get_nodes_coords_undef("jobs/JB-STP02-2D.odb","PLATE-1",fname="nodes02.txt")
#get_nodes_coords_undef("jobs/JB-STP03-2D.odb","PLATE-1",fname="nodes03.txt")
#for x in range(1,4):
#	get_nodes_coords("jobs/JB-STP0"+str(x)+"-2D.odb","PLATE-1","Step-0"+str(x)+"-Up",fname="n0"+str(x)+".txt")
#get_nodes_coords("jobs/JB-STP01-2D.odb","PLATE-1","Step-01-Up",fname="nodes.txt")
#get_nodes_coords("jobs/dbex3.odb","PLACA-1","Descarga_03",fname="dat/nodes.txt")
#get_elements_conect("jobs/dbex3.odb","PLACA-1",fname="dat/elements.txt")
#get_max_eqvs_bystep("dbex.odb",nstep="Step-01-Up")
#get_max_eqvs("jobs/JB-STP01-2D.odb")
#get_max_pe("jobs/JB-STP01-2D.odb")
#get_nodes_coords("JB-STP01-2D.odb","PLATE","Step-01-Up",fname="dat/nodes.txt")
#get_elements_conect("JB-STP01-2D.odb","PLATE",fname="dat/elements.txt")
#f = open("filex.txt","w")
#f.write(str(get_instances(ODB)))
#f.close()
#write_mini_report(get_steps(ODB),"rpt/rpt_steps.txt")
#write_mini_report(get_job(ODB),"rpt/rpt_job.txt")
#get_deformed_sequence(ODB,"PLATE")
#M1 = (1,75,87,63,98,57,51,5,111,103)
#M2 = (189,195,182,207,171,213,219,152,158,166)
#get_distances(ODB,"PLATE",M1,M2,"Step-02-Up")

# Nodos frontera
MN = [10]
[MN.append(k) for k in range(225,152,-1)]
[MN.append(k) for k in [9,152,8,228,5]]
[MN.append(k) for k in range(114,46,-1)]
[MN.append(k) for k in [4,227,7,226,10]]
get_border_nodes(ODB,"PLATE","Step-02-Up",MN,-1,fname="border-02.txt")
