# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 13:12:10 2022

@author: ZR48SA
"""

#%% change directory to script directory (should work on windows and mac)
import os
from pathlib import Path
from inspect import getsourcefile
os.chdir(str(Path(os.path.abspath(getsourcefile(lambda:0))).parents[0]))
script_dir=os.getcwd()
print(os.getcwd())

basedir=os.getcwd()

#%%
import pandas as pd
import numpy as np
import random


files=["F:/Nadiehs_data/P52B_scan.mgf",
"F:/Nadiehs_data/P52A_scan.mgf",
"F:/Nadiehs_data/P51B_scan.mgf",
"F:/Nadiehs_data/P51A_scan.mgf"]


#deepnovo training file format example
# input_file_train = "data.training/yeast.low.coon_2013/peaks.db.mgf.train.dup"
# input_file_valid = "data.training/yeast.low.coon_2013/peaks.db.mgf.valid.dup"
# input_file_test = "data.training/yeast.low.coon_2013/peaks.db.mgf.test.dup"



scans=[]

for file in files:
    with open(file) as f:
        lines=f.readlines()
        lines=[l.splitlines()[0] for l in lines]
        lines=np.array(lines)
        scans.extend(np.array(np.split(lines,np.argwhere(lines=="BEGIN IONS").flatten()[1:])))
        
#%%


random.shuffle(scans)



with open("peaks.db.mgf.train.dup","w") as f:
    f.write("\n".join(list(np.concatenate(scans[0::3])))+"\n")
    
with open("peaks.db.mgf.valid.dup","w") as f:
    f.write("\n".join(list(np.concatenate(scans[1::3])))+"\n")
    
with open("peaks.db.mgf.test.dup","w") as f:
    f.write("\n".join(list(np.concatenate(scans[2::3])))+"\n")