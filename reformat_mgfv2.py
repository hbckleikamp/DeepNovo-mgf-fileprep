# -*- coding: utf-8 -*-
"""
Created on Fri May 27 17:23:42 2022

@author: ZR48SA
"""
#custom reformatting script

import pandas as pd
import numpy as np

files=    ["C:/Comet/spectra/Re2_JSP_JLN_UPLIFT.mgf",
    "C:/Comet/spectra/C6_1_JSP_JLN_UPLIFT.mgf",
    "C:/Comet/spectra/C6_2_JSP_JLN_UPLIFT.mgf",
    "C:/Comet/spectra/C24_1_JSP_JLN_UPLIFT.mgf",
    "C:/Comet/spectra/C24_2_JSP_JLN_UPLIFT.mgf",
    "C:/Comet/spectra/Ox1_JSP_JLN_UPLIFT.mgf",
    "C:/Comet/spectra/Ox2_JSP_JLN_UPLIFT.mgf",
    "C:/Comet/spectra/Re1_JSP_JLN_UPLIFT.mgf"]


files=["C:/LinuxDeepNovo/MP_AM27072018_S1SC_No2_DDA01_nodeisotoping.mgf"]

for file in files:


    with open(file) as f:
        lines=f.readlines()
    
    
        #FROM (format)
        # BEGIN ION
        # TITLE=Re2_JSP_JLN_UPLIFT.2079.2079.2 File:"Re2_JSP_JLN_UPLIFT.raw", NativeID:"controllerType=0 controllerNumber=1 scan=2079"
        # RTINSECONDS=957.43086
        # PEPMASS=550.217956542969 529711.127929699956
        # CHARGE=2+
        # END ION
        
        #TO (format)
        # BEGIN IONS
        # TITLE=C:\Users\nh2tran\WORKING\DeepNovo\DeepDB\PEAKS\yeast.low.coon_2013\run_ALL_C:\Users\nh2tran\WORKING\DeepNovo\DeepDB\data\yeast.low.coon_2013\singleShot_Fusion-1493228696289\10sep2013_yeast_control_1.raw_SCANS_1393
        # PEPMASS=304.494
        # CHARGE=3+
        # SCANS=F1:1393
        # RTINSECONDS=131.85599
        # SEQ=QIVHDSGR
        # END IONS
        
        #lines=[l[:-2] for l in lines]
        lines=[l.splitlines()[0] for l in lines]
        lines=np.array(lines)
        lines=np.array(np.split(lines,np.argwhere(lines=="BEGIN IONS").flatten()[1:]))
        
        ls=[]
        for ix,l in enumerate(lines):
            l=list(l)
        
            s=l[3].split()
            l[3]=s[0]
            rt=l.pop(2)
            # l[3]+="+"
            
            if "scan" in l[1]:
                l.insert(4,"SCANS="+str(l[1].split("scan=")[1].split(".")[0]))
            else:
                l.insert(4,"SCANS="+str(ix))
                
                
            l.insert(5,rt)
            l.insert(6,"SEQ=QIVHDSGR") #"MAAAAAAACK") #mock peptide sequence
            # l[0]+="S"
            # l[-1]+="S"
            l.append("")
            ls.extend(l)
            
        ls="\n".join(ls)+"\n"
        with open(file.replace(".mgf","_rf.mgf"), "w") as w:
            w.write(ls)
    