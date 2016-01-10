# -*- coding: utf-8 -*-
# __replaces.py
# =============================
# (c) 2015, Jorge De Los Santos
# ITC-Bypasa
# =============================
#

from cfg import *

CONTENTS_REPLACES = {
"_deformedshape_":r"graphs/elements.png",
"_misesstress_":r"graphs/stress.png",
"_nominalstrain_":r"graphs/strain.png",
"_materialcurve_":r"graphs/strain.png",
"_material_":"1018 Steel",
"_friction_":str(FRICTION_COEFF),
"_poisson_":str(POISSON_COEFF),
"_density_":str(STEEL_DENSITY),
"_young_":str(YOUNG_MOD),
"_elementtype_":"CPS4",
"_meshsize_":str(MESH_SIZE_QUAD)
}

PARTS_REPLACE = {
"_partname_":1,
"_parttype_":2,
}
