# DeepNovo-mgf-fileprep
2 python scripts and one bash for prepping raw files to deepnovo MGF format, and using idXML to add sequence information for training your own datasets.

<br>
<br>msconvert_mgf_arg.bash: simple bash script for msconvert from raw files to .mgf<br>
<br>reformat_mgf.py: reformat msconvert .mgf files to format used by DeepNovo (annotation only) <br> 
<br>mzXML_idXML2mgf.py: reformat msconvert .mgf files to format used by DeepNovo together with idXML files to add annotated sequences (for training your own model)<br><br>
make_trainingsets.py: concatenates a number of .mgf files with sequences and randomly divide evenly into train.dup valid.dup and test.dup

