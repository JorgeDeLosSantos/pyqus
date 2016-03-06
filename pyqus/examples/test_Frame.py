# -*- coding: mbcs -*-
import sys
sys.path.insert(0, '../')

from iodb import *

dbpath = r"odb/Frame/Frame.odb"
inst = "FRAME-1"
stepname = "Apply load"

out_vars = "CF|E|RF|S|U".split("|")

for var in out_vars:
    fn = r"dat/Frame/%s.txt"%(var)
    fn2 = r"dat/Frame/max_%s.txt"%(var)
    get_field_var(dbpath,var,inst,stepname,nframe=-1,fname=fn)
    get_max_values(dbpath,var,fn2)

# Get elements
get_elements(dbpath,inst, r"dat/Frame/elements.txt") 

# Get nodes coordinates
get_nodes_coordinates(dbpath,inst,stepname,nframe=0,fname=r"dat/Frame/nodes.txt") # Initial frame
