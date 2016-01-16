# -*- coding: mbcs -*-
# =============================
# (c) 2015, Jorge De Los Santos
# ITC-Bypasa
# =============================
import re

a = [1,3,5,10]
args = tuple([a[k] for k in range(len(a))])
f = open("test.txt","w")
f.write(len(args)*"%6.4f\t"%args)
f.write("\n")
f.write(len(args)*"%6.4f\t"%args)
f.close()
