# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:19:03 2022

@author: hbckleikamp
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
import re
#%%


folder="" #full filepath to folder

mgf_files=[str(Path(folder,f)) for f in os.listdir(folder) if f.endswith(".mgf")]
idXML_files=[str(Path(folder,f)) for f in os.listdir(folder) if f.endswith(".idXML")]



for file in mgf_files:

    
    with open(file) as f:
        lines=f.readlines()
    
    
        if not "SEQ=" in lines:
       
            print(file)
            # parse idXML
            idXML_file=file[:-3]+"idXML"
            if Path(idXML_file).name in os.listdir(folder):

            
                with open (idXML_file,"r") as f:
                    xml_string=f.read()
    
             
        
        
                #%% parse xml
                
                ps=[i.split("</PeptideHit>")[0] for i in xml_string.split('<PeptideIdentification')]
                seqs=[i.split('sequence="')[1].split('"')[0] for i in ps] 
            
                scans=[i.split('scan=')[1].split('"')[0] if "scan=" in i else "" for i in ps ] 
                df=pd.DataFrame(zip(seqs,scans),columns=["seqs","scans"])
                df=df[df.scans!=""]
                
                df["seqs"]=df.seqs.apply(lambda x: re.sub("[\(\[].*?[\)\]]", "mod", x))
                df.scans=df.scans.astype(str)
                
            
            
            
                #%% parse mgf
                
                lines=[l.splitlines()[0] for l in lines]
                lines=np.array(lines)
                lines=np.array(np.split(lines,np.argwhere(lines=="BEGIN IONS").flatten()[1:]))
                
                scans=[]
                
                ls=[]
                for ix,l in enumerate(lines):
                    l=list(l)
                
                    s=l[3].split()
                    l[3]=s[0]
                    rt=l.pop(2)
       
                    
                    if "scan" in l[1]:
                        scan=str(l[1].split("scan=")[1].split(".")[0])
                        l.insert(4,"SCANS="+scan)
                        l.insert(5,rt)
                        scans.append(scan)
                        
                        if scan in df.scans.values:
                
                            l.insert(6,"SEQ="+df[df.scans.values==scan].seqs.tolist()[0]) #"MAAAAAAACK") #mock peptide sequence
                            l.append("")
                            ls.extend(l)
                    
                ls="\n".join(ls)+"\n"
                with open(file.replace(".mgf","_scan.mgf"), "w") as w:
                    w.write(ls)
                    

                
                if "scan" in l[1]:
                    scan=str(l[1].split("scan=")[1].split(".")[0])
                    l.insert(4,"SCANS="+scan)
                    l.insert(5,rt)
                    scans.append(scan)
                    
                    if scan in df.scans.values:
            
                        l.insert(6,"SEQ="+df[df.scans.values==scan].seqs.tolist()[0]) #"MAAAAAAACK") #mock peptide sequence
                        l.append("")
                        ls.extend(l)
                
            ls="\n".join(ls)+"\n"
            with open(file.replace(".mgf","_scan.mgf"), "w") as w:
                w.write(ls)
                
