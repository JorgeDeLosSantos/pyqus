# -*- coding: mbcs -*-
import sys
sys.path.insert(0, '../')

from iodb import *

dbpath = r"odb/Lug/Lug.odb"
inst = "LUG-1"
stepname = "LugLoad"

out_vars = "RF|S|U".split("|")

for var in out_vars:
    fn = r"dat/Lug/%s.txt"%(var)
    fn2 = r"dat/Lug/max_%s.txt"%(var)
    get_field_var(dbpath,var,inst,stepname,nframe=-1,fname=fn)
    get_max_values(dbpath,var,fn2)

# Get elements
get_elements(dbpath,inst, r"dat/Lug/elements.txt")

# Get nodes coordinates
get_nodes_coordinates(dbpath,inst,stepname,nframe=0,fname=r"dat/Lug/nodes.txt") # Initial frame
