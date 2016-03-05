# -*- coding: mbcs -*-
import sys
sys.path.insert(0, '../')

from iodb import *

ODB_PLATE = r"odb/hole_plate.odb"
ODB_BENDING = r"odb/bending_test.odb"
ODB_BEAM = r"odb/beam.odb"
ODB_FRAME = r"odb/frame.odb"
ODB_FILES = [ODB_PLATE,ODB_BENDING,ODB_BEAM,ODB_FRAME]
#db = ODB_FRAME
#get_nodes_coordinates(db,find_deformable_body(db),find_last_step(db),nframe=0,fname=r"dat/"+r"nodes_01_"+db[4:-3]+"txt")
for db in ODB_FILES:
	get_max_eqvs(db,fname=r"dat/"+r"max_eqvs_"+db[4:-3]+"txt")

for db in ODB_FILES:
	get_max_pe(db,fname=r"dat/"+r"max_pe_"+db[4:-3]+"txt")
	
for db in ODB_FILES:
	get_elements(db,find_deformable_body(db),fname=r"dat/"+r"elements_"+db[4:-3]+"txt")

for db in ODB_FILES:
	get_nodes_coordinates(db,find_deformable_body(db),find_last_step(db),nframe=-1,fname=r"dat/"+r"nodes_"+db[4:-3]+"txt")


